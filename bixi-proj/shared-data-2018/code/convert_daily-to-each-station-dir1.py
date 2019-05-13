import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import datetime
import glob
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
from matplotlib.axes import Axes

stations = 'data\\2018\\Stations_2018.csv'
cats=pd.read_csv(stations,header=0)
#output0=output1=output2=pd.read_csv(stations,header=0,index_col='code').transpose()

station_list = np.array(cats['code'])

def find(station,weekday):

    a = np.array([0,1,2,3,4,5])

    filenames = sorted(glob.glob('from-daily\\2018\\*-'+str(weekday)+'.csv'))
    #filenames = sorted(glob.glob(str(path)+str(year)+'\\*-'+str(weekday)+'.csv'))
    #filenames = sorted(glob.glob('from-daily\\2018\\*-1.csv'))

    for file in filenames:
        #print(file)
        data=pd.read_csv(file,header=0)

        #y=np.array(data.iloc[0][4:])

        y=np.array(data.loc[data.iloc[:,0]==station])
        a=np.vstack((a,y))

    return a[1:]


for weekday in range(7,8,1):

    for station in station_list:
        station_data = find(station,weekday)
        daily_dir = pd.DataFrame(station_data).sort_values(by=[3])

        output0=output1=output2=pd.read_csv(stations,header=0,index_col='code').transpose()

        for t in range(24):

            sel = daily_dir.loc[(daily_dir.iloc[:,3]>t*60)&(daily_dir.iloc[:,3]<(t+1)*60)]
            count=[]
            time=[]
            mbr=[]

            for station_code in station_list:

                df = sel.loc[sel.iloc[:,1]==station_code]
                count.append(df.shape[0])
                time.append(df.iloc[:,4].mean(skipna = True))
                mbr.append(df.iloc[:,5].sum(skipna = True))

            dir=pd.DataFrame(pd.Series(count,index=station_list)).transpose()
            time=pd.DataFrame(pd.Series(time,index=station_list)).transpose()
            mbr=pd.DataFrame(pd.Series(mbr,index=station_list)).transpose()
            output0=output0.append(dir,ignore_index=True)
            output1=output1.append(time,ignore_index=True)
            output2=output2.append(mbr,ignore_index=True)

        output0.transpose().to_csv('from-dir\\2018\\Dir\\from-'+str(station)+'-D'+str(weekday)+'.csv')
        output1.transpose().to_csv('from-dir\\2018\\Time\\from-'+str(station)+'-T'+str(weekday)+'.csv')
        output2.transpose().to_csv('from-dir\\2018\\Member\\from-'+str(station)+'-M'+str(weekday)+'.csv')
        print(str(station)+'-'+str(weekday))



