#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import pylab
import numpy as np
import pandas as pd
import csv

# サーバに送るhtmlを作成し、printで表示

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>WebApp for Python3</title>
</head>
<body>
<img src="../ThreeDaysChart.png">
<img src="../OneDayChart.png">
</body></html>"""

print(html_body)

# 変数の定義

OneDay = 288 # 一日のデータに必要な要素の数
ThreeDays = 864 # 三日のデータに必要な要素の数
Determine = ['400'] #在籍判定に用いるデータ
OneDay_x = []
OneDay_y = []
ThreeDays_x = []
ThreeDays_y = []

#　csvからデータを読み込みheaderと各列の要素をリスト型で返す関数

def read_csv(csv_name,until_day):
    x = []
    y = []
    count = 0
    with open(csv_name) as f: # csvからデータを読み込む、headerは最初の一行に入っているものとする
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if len(row) == 0: # 空行だったらもう一回読み込む
                continue
            elif count > until_day: # 必要なデータ量を格納できていたらリストを返す
                return header,x,y
            elif row[-1:] < Determine: # センサー値から在籍しているのかを判定(0:不在席,1:在籍)
                row[-1:] = '0'
            else:
                row[-1:] = '1'
                
            if count % OneDay == 0: # データ取得日から一日毎に日時を取得し、x軸のリスト型に格納
                x += row[:1]
                
            y += row[-1:]
            count += 1

# 受け取ったリストから折れ線グラフの画像を作成する関数

def Make_Chart(make_chart_name,method_list_header,method_list_x,method_list_y,which_day):
    pylab.figure(figsize=(10, 4)) # グラフのサイズ指定
    plt.plot(method_list_y)
    if which_day == "OneDay": # x軸の調整
        plt.xticks([0,OneDay],method_list_x)
    else:    
        plt.xticks([0,OneDay,OneDay*2,OneDay*3],method_list_x)
    plt.title('In Nationality Data '+ make_chart_name)
    plt.xlabel(method_list_header[:1]) # x軸とy軸の名前をheaderから取得
    plt.ylabel(method_list_header[-1:])
    plt.savefig(make_chart_name)

#　関数の実行に必要な引数を渡す処理

header,OneDay_x,OneDay_y = read_csv('sensorData.csv',OneDay)    
header,ThreeDays_x,ThreeDays_y = read_csv('sensorData.csv',ThreeDays)    
Make_Chart("OneDayChart.png",header,OneDay_x,OneDay_y,'OneDay')
Make_Chart("ThreeDaysChart.png",header,ThreeDays_x,ThreeDays_y,'ThreeDay')
