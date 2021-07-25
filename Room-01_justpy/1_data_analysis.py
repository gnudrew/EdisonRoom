import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
# Aggregate and average data by week
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()
# .. by month
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()

chart_def = """
{

    title: {
        text: 'Average Course Rating by Week'
    },

    subtitle: {
        text: 'Source: reviews.csv'
    },

    yAxis: {
        title: {
            text: 'Rating'
        }
    },

    xAxis: {
        title: {
            text: 'Week'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
        }
    },

    series: [{
        name: 'data',
        data: []
        }, 
    ],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
}
"""
chart_def2 = """
{

    title: {
        text: 'Average Course Rating by Month'
    },

    subtitle: {
        text: 'Source: reviews.csv'
    },

    yAxis: {
        title: {
            text: 'Rating'
        }
    },

    xAxis: {
        title: {
            text: 'Month'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
        }
    },

    series: [{
        name: 'data',
        data: []
        }, 
    ],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h4 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])

    hc2 = jp.HighCharts(a=wp, options=chart_def2)
    hc2.options.xAxis.categories = list(month_average.index)
    hc2.options.series[0].data = list(month_average['Rating'])

    return wp

jp.justpy(app)