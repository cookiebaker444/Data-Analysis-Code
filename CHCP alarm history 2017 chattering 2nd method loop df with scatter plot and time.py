import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as plta
os.getcwd()
os.chdir('C:/D drive/Research/CHCP-Alarms')
df = pd.read_csv('HC Alarm History 2017.csv',header = None,error_bad_lines=False)
df.columns = ['Date1', 'AlmAck','Type','Name','Area','DSC','7','8','9','10','11','12','13','14','15','16','17','AlmCond','Date2','20','21']
df['Date1'] = pd.to_datetime(df['Date1'], errors = 'coerce')
df['Date2'] = pd.to_datetime(df['Date2'], errors = 'coerce')
file =df.sort_values(['Date1'], ascending=[True]).iloc[:df.shape[0],0:4].reset_index()
file2 = file.iloc[:df.shape[0],1:4]
file2.columns = ['Date1', 'AlmAck','Type']
file2['Date1'] = pd.to_datetime(file['Date1'],errors = 'ignore')
t=2
alarmcount = {}
alarmtime = {}
df2 = pd.DataFrame(columns=['Name','Result','Indicator','Indicator2','Name2'])
df2 = df2.astype('object')
file3 = file2[file2['AlmAck'].str.contains('_ALM')==True]
file3.reset_index(drop=True, inplace=True)
file3["Type2"] = file3["Date1"].map(str)+file3["Type"]
def plot():
    resultplot = plt.scatter(x=df2.loc[a-5:a,'Indicator2'],y=df2.loc[a-5:a,'Indicator'])
    plt.title('Result Graph',fontsize = 30)
    plt.ylabel('Result', fontsize = 30)
    plt.xlabel('Alarm Type', fontsize =30)
    y=[0,1]
    labelsy = ['Not a Chattering alarm', 'Chattering Alarm']
    plt.yticks(y,labelsy)
    x=[a-5,a-4,a-3,a-2,a-1,a]
    labelsx = df2.loc[a-5:a,'Name']
    plt.xticks(x,labelsx,rotation = 90)
    plt.pause(0.1)
    plt.draw()
    plt.clf()
alarmcount = {}
alarmfir = {}
alarmsec = {}
alarmthi = {}
name = file3.iloc[0,2]
name2= file3.iloc[0,3]
df2.loc[0,'Name'] = name2
df2.loc[0,'Result'] = 'Not a Chattering Alarm'
df2.loc[0,'Indicator'] = 0
df2.loc[0,'Indicator2'] = 0
print ("0, CHCP_STM4#PSLROU1T.STSwitch, Not a Chattering Alarm")
alarmcount[name] = 1
alarmfir[name] = file3.iloc[0,0]
for a in range (1,1000):
    name = file3.iloc[a,2]
    name2 = file3.iloc[a,3]
    df2.loc[a,'Name'] = name2
    if name in alarmcount:
        alarmcount[name] += 1
        if alarmcount[name] is 2:
            alarmsec[name] = file3.iloc[a,0]
            print( a, name2, 'Not a Chattering Alarm')
            df2.loc[a,'Result'] = "Not a Chattering Alarm"
            df2.loc[a,'Indicator'] = 0
            df2.loc[a,'Indicator2'] = a
            plot()
        if alarmcount[name] is 3:
            alarmthi[name] = file3.iloc[a,0]
            if pd.Timedelta(alarmthi[name]-alarmfir[name]) <= pd.Timedelta(seconds=60) :
                print (a, name2, 'Chattering Alarm')
                df2.iloc[a,1] = 'Chattering Alarm'
                df2.loc[a,'Indicator'] = 1
                df2.loc[a,'Indicator2'] = a
                plot()
                alarmfir[name] = alarmsec[name]
                alarmsec[name] = alarmthi[name]
                alarmcount[name] = 2
            else:
                print( a, name2, 'Not a Chattering Alarm')
                df2.loc[a,'Result'] = "Not a Chattering Alarm"
                df2.loc[a,'Indicator'] = 0
                df2.loc[a,'Indicator2'] = a
                plot()
                alarmfir[name] = alarmsec[name]
                alarmsec[name] = alarmthi[name]
                alarmcount[name] = 2
    else:
        alarmcount[name] = 1
        alarmfir[name] = file3.iloc[a,0]
        print (a, name2, 'Not a Chattering Alarm')
        df2.loc[a,'Result'] = "Not a Chattering Alarm"
        df2.loc[a,'Indicator'] = 0
        df2.loc[a,'Indicator2'] = a
        plot()
