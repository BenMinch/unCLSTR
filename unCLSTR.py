#unCLSTR - a script to parse the output of CD-HIT- clstr files into a csv file

import sys,re,os,subprocess
import pandas as pd

input= sys.argv[1]
output= sys.argv[2]

#read in the clstr file
data= pd.read_csv(input, header=None)
data.columns= ['cluster','length','member']
#make a new column with cluster membership
for i in range(len(data)):
    number= data['cluster'][i]
    if number[0]=='>':
        number= number[1:]
        data['cluster'][i]= number
    else:
        data['cluster'][i]= data['cluster'][i-1]
data= data.dropna()
data.to_csv(output+'_total_members.csv')

#only get the representative sequences from each cluster
clusterdf= pd.DataFrame()
clusterdf['cluster']= data['cluster'].unique()

#get the representative sequence for each cluster
clusterdf['rep']= ''
for i in range(len(data)):
    if '*' in data['member'][i]:
        clusterdf['rep'][clusterdf['cluster']==data['cluster'][i]]= data['member'][i]

clusterdf.to_csv(output+'_rep_members.csv')
