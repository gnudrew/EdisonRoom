import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
# Aggregate and average data by month
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg_crs = data.groupby(['Month','Course Name']).mean().unstack()

    # chart: {
    #     type: 'spline'
    # },
    
chart_def = """
{
    title: {
        text: 'Average Rating by Month by Course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 0,
        y: 50,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h4 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    month_crs_series = [{'name':course_name, 'data':[r for r in month_avg_crs[course_name]]} for course_name in month_avg_crs.columns]
    hc.options.xAxis.categories = list(month_avg_crs.index)
    hc.options.series = month_crs_series
    return wp

jp.justpy(app)