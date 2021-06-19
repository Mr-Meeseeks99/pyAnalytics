# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:25:46 2021

@author: SAHIL
"""
import pandas as pd

student = pd.read_csv('https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk' + '/export?gid=1858159025&format=csv',  index_col=0 )
student.head(5)
student.shape
type(student)
