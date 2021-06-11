import plotly.express as px
import csv
from datetime import datetime
import pandas as pd

dates=[]
t_avg=[]
t_min=[]
t_max=[]

#['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']                #THis is the table headings in order
filename='data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)                    #read the csv file and stor its contents in the form of an object in reader that can be read from like a list
    header=next(reader)                     #gets the line to be read next and stores in header. This takes the first line such that from the rnext reading, the header isn't read 

    for row in reader:                      #loops each row in reader. row is a list here
        t_min.append(int(row[5]))               
        t_max.append(int(row[6]))
        avg=int(row[5]) + int(row[6])
        t_avg.append(avg//2)
        cur_date=datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(cur_date)


d={'t_avg':t_avg, 't_min': t_min, 't_max':t_max}
df=pd.DataFrame(data=d)
fig=px.line(df, x=dates, y=['t_avg','t_min','t_max'], title='Temperature in Sitka 2018',

            labels={
                'x':'Dates',            #label for x-axis
                'value':'Temperature Readings',     #label for y-axis
                'variable':'Line Description'           # When you hover over the line the Legend title comes as 'Line description'
            })



fig.update_layout(                              #changing layout
    font_family="Courier New",
    font_color="blue",
    font_size=20,
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="purple",
    legend_title='Line descripions',
    legend_title_font_size=15,
    legend_font_size=10)


fig.write_html('Sitka_temp.html')
fig.show()
