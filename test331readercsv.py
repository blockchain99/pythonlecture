import pandas as pd 
import numpy as np 
from csv import reader, DictReader


with open("test331_Per the World Bank (2018).csv", "r") as file:
    # csv_reader = reader(file)
    csv_dictreader = DictReader(file)

    # for row in csv_dictreader:
    #     if len(row['Country/Territory']) > 11 :
    #         print(row['Country/Territory'])

    print("-----------GDP more than 106472------------------------")
    for row in csv_dictreader:
        try:  #Error not convert string to float
           if float(row['GDP(US$million)'].replace(',','').replace('"','')) > 106472 :
            print(row['Country/Territory'])
        except ValueError as err:
            pass
            print(err)
        
    # print("---GDP amount to integer---")
    # for row in csv_dictreader:
    #     print(row['GDP(US$million)'])

    # print("---rank---")
    # for row in csv_dictreader:
    #     print(row['Rank'])
    
print("##########currency to integer convert ########")
from re import sub
from decimal import Decimal

money = '$6,150,593.22'
value = Decimal(sub(r'[^\d.]', '', money))
print(money)
print(value)