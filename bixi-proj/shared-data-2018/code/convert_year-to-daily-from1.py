import numpy as np
import pandas as pd
import datetime
import dateparser
import csv
import glob

start_weekday0=start_weekday=6
start_week0=start_week=15

lable_str=['From','To','Time','Delta','Duration','User']
lable=pd.DataFrame(pd.Series(lable_str)).transpose();
new_day_start=lable

filenames = sorted(glob.glob('data\\2017\\2017.csv'))

for file in filenames:
    #print('processing '+file)
    data_source=pd.read_csv(file,header=0)
    data=data_source.sort_values(by=['start_date'])
    print(data.shape)

    for row in range(data.shape[0]):
        #start_time=dateparser.parse(data.iloc[row,0])
        print(data.iloc[row,0])
        start_time=datetime.datetime.strptime(str(data.iloc[row,0]), '%Y-%m-%d %H:%M')
        start_year,start_week,start_weekday=start_time.isocalendar()
        start_date=start_time.strftime('%Y-%m-%d')
        start_moment=int(start_time.strftime('%H'))*60+int(start_time.strftime('%M'))
        #print(start_year,start_week,start_weekday,start_moment)


        if start_weekday!=start_weekday0:
            path_start=("from-daily\\2017\\from-"+str(start_date)+"-"+str(start_week0)+"-"+str(start_weekday0)+".csv")
            new_day_start[1:].to_csv(path_start,index=False)
            new_day_start=lable

            print(start_date)

        new_row_start=pd.DataFrame(pd.Series([data.iloc[row,1],data.iloc[row,3],start_time,int(start_moment),data.iloc[row,4],data.iloc[row,5]])).transpose()
        new_day_start=new_day_start.append(new_row_start,ignore_index=True)

        start_weekday0=start_weekday
        start_week0=start_week


