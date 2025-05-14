from itertools import count
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from kmodes.kprototypes import KPrototypes
from rest_framework.response import Response
from config import PATH_TO_DATASET

# Create your views here.
@api_view(['GET'])
def SegmentedCustomers(request):
    response = {}
    countData = { 
        "cluster0":0,
        "cluster1":0,
        "cluster2":0,
        "cluster3":0,
        "cluster4":0   
    }
    series = [
        {"name":"cluster 0", "data" :[] },
        {"name":"cluster 1", "data" :[]},
        {"name":"cluster 2", "data" :[]},
        {"name":"cluster 3", "data" :[]},
        {"name":"cluster 4", "data" :[]}   
    ]
    df = pd.read_csv(PATH_TO_DATASET)
    df = df.drop(['CustomerID'],axis = 1)
    df = df.drop(['Profession'],axis = 1)
    df = df.drop(['location'],axis = 1)
    df = df.drop(['Family_Size'],axis = 1)
    df = df.drop(['Total'],axis = 1)
    df = df.drop(['email_id'],axis = 1)
    df_array = np.array(df)
    kproto = KPrototypes(n_clusters=5, verbose = 2, max_iter = 20)
    clusters = kproto.fit_predict(df_array, categorical =[0])
    cluster_dict = []
    for c in clusters:
       cluster_dict.append(c)
    df['cluster'] = cluster_dict
    temp_cordinate_list = []
    for index,data in df.iterrows():
        if data['cluster'] == 0:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[0]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []
        elif data['cluster'] == 1:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[1]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []   
        elif data['cluster'] == 2:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[2]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []   
        elif data['cluster'] == 3:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[3]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []
        else:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[4]['data'].append(temp_cordinate_list)
            temp_cordinate_list = [] 
    response['series'] = series
    response['status'] = 1 
    countData['cluster0'] = len(df[(df['cluster']==0)])
    countData['cluster1'] = len(df[(df['cluster']==1)])
    countData['cluster2'] = len(df[(df['cluster']==2)])
    countData['cluster3'] = len(df[(df['cluster']==3)])
    countData['cluster4'] = len(df[(df['cluster']==4)])
    response['counts'] = countData          

    return Response(response)



@api_view(['GET'])
def Customers(request):
    response = {"status":1, "data" : [] ,"message":""}
    df = pd.read_csv(PATH_TO_DATASET)
    temp_tuple = ()
    for data in df.itertuples():
        response['data'].append(data)
    response['message'] = "success"    
    return Response(response)    