# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#https://data.ibb.gov.tr/dataset/atik-tesisleri
data = pd.read_csv("waste_facility.csv")
print(data)


name= data[['facility_name']]
print(name)

name_address = data[["facility_name","address"]]
print(name_address)

address= data[['address']]
print(address)

#https://data.ibb.gov.tr/dataset/ibb-lokasyon-verileri
data2 = pd.read_csv("ibb_lokasyon.csv")
print(data2)



