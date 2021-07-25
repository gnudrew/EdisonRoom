import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
# Aggregate and average data by weekday
data['Weekday'] = data['Timestamp'].dt.strftime('%a')  
def map_weekday_order(s):
    # s is a string
    if s == 'Sun':
        return 0
    elif s == 'Mon':
        return 1
    elif s == 'Tue':
        return 2
    elif s == 'Wed':
        return 3
    elif s == 'Thu':
        return 4
    elif s == 'Fri':
        return 5
    elif s == 'Sat':
        return 6
data['Weekday_order'] = data['Weekday'].apply(map_weekday_order)
avg_rating_weekday = data.groupby(['Weekday_order','Weekday']).mean()
    
chart_def = """
{
    title: {
        text: 'Average Rating by Weekday'
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
        categories: [],
    },
    yAxis: {
        title: {
            text: 'Rating'
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
    series: [
        {
            name: '',
            data: []
        }
    ]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Happiness across Weekdays", classes="text-h4 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    x = [avg_rating_weekday.index[i][1] for i in range(7)]
    print(x)
    y = list(avg_rating_weekday['Rating'])
    print(y)
    hc.options.xAxis.categories = x
    hc.options.series[0].name = "all courses"
    hc.options.series[0].data = y
    return wp

jp.justpy(app)