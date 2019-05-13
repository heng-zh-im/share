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

#x-axis with 24h
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
fig, ax = plt.subplots()
#ax.set_ylim([0, 50])
#Axes.autoscale(ax,enable=False)


year=2018
weekday=1
station=7030
path="from-station\\"

def get_ydata():

    global year
    global weekday
    global station

    global x
    a=x

    filenames = sorted(glob.glob(str(path)+str(year)+'\\*-'+str(weekday)+'.csv'))

    for file in filenames:
        #print(file)
        data=pd.read_csv(file,header=0)

        #y=np.array(data.iloc[0][4:])

        y=np.array(data.loc[data.iloc[:,0]==station])[0][4:]
        a=np.vstack((a,y))

        #ax.plot(x,data.iloc[0][4:])
        #plt.scatter(x, y, alpha=0.5)
    return a[1:]

y0=get_ydata()
ax.boxplot(y0)


axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.02, 0.5, 0.07, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('2018', '2017', '2016', '2015', '2014'))


def yearfunc(label):
    global year
    year=label
    ax.clear()
    ax.boxplot(get_ydata())
    plt.show()
radio.on_clicked(yearfunc)

rax = plt.axes([0.02, 0.275, 0.07, 0.175], facecolor=axcolor)
radio2 = RadioButtons(rax, ('Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'))


def dayfunc(label):
    global weekday
    dict = {'Monday':'1', 'Tuesday':'2', 'Wednesday':'3','Thursday':'4','Friday':'5','Saturday':'6','Sunday':'7'}
    weekday = dict[label]
    ax.clear()
    ax.boxplot(get_ydata())
    plt.show()

radio2.on_clicked(dayfunc)

def submit(text):
    global station
    station=int(text)
    ax.clear()
    ax.boxplot(get_ydata())
    plt.show()

axbox = plt.axes([0.125, 0.9, 0.775, 0.075])
text_box = TextBox(axbox, 'Station', initial="7030")
text_box.on_submit(submit)

class Click(object):
    def departure(self, event):
        global path
        path="from-station\\"
        ax.clear()
        ax.boxplot(get_ydata())
        plt.show()

    def arrival(self, event):
        global path
        path="to-station\\"
        ax.clear()
        ax.boxplot(get_ydata())
        plt.show()

callback = Click()
axdep = plt.axes([0.02, 0.8, 0.07, 0.05])
axarr = plt.axes([0.02, 0.7, 0.07, 0.05])
bdep = Button(axdep, 'Departure')
bdep.on_clicked(callback.departure)
barr = Button(axarr, 'Arrival')
barr.on_clicked(callback.arrival)

plt.show()


