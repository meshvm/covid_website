import json
import requests
import re, datetime, string
import pandas as pd

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv("covid19india.csv")

# rename the columns of the census DataFrame
print(census_df.columns)
# response = requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges")
# todos = json.loads(response.text)
# pr=todos['data']['medicalColleges']
# for i in pr:
#     for key,value in i.items():
#         print(value)
# pr=todos['data']['medicalCollages']
# n=6
# for i in pr:
#     for key,value in i.items():
#         for ij in range(7):
#             print(value)

# pra=todos['data']['regional']
# print(pra)
# s = "I have a meeting on 2018-12-10 in New York"
# match = re.search('\d{4}-\d{2}-\d{2}', s)
# date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
# print date
match=' '
# from flask import Flask, render_template
# response = requests.get("https://api.rootnet.in/covid19-in/notifications")
# todos = json.loads(response.text)
# def Filter(string, substr): 
#     return [str for str in string  
#     if re.match(r'[^\d]+|^', str).group(0) in substr]
# try:
#     pr=todos['data']['notifications']
#     for dic in pr:
#         for val in dic.values():
#             urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', val)
#             dates = re.findall(r"[\d]{1,2}.[\d]{1,2}.[\d]{4}", val)
#             print(Filter(val,urls))
#             print("*"**10)
#             print(Filter(val,dates))
# except:
#     print("Nothing")
#     pass        

# print(todos['success']['data']['notifications'])
# a=todos['data']['contacts']['regional']s
# for dic in a:
#     for val in dic.values():
#         print(val,end="")
# ​ https://api.rootnet.in/covid19-in/notifications
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)
# # app = Flask(__name__)

# # @app.route('/json-example', methods=['POST']) #GET requests will be blocked
# # def json_example():
# #     req_data = request.get_json()

# #     language = req_data['language']
# #     framework = req_data['framework']
# #     python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
# #     example = req_data['examples'][0] #an index is needed because of the array
# #     boolean_test = req_data['boolean_test']

# #     return '''
# #            The language value is: {}
# #            The framework value is: {}
# #            The Python version is: {}
# #            The item at index 0 in the example list is: {}
# #            The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# Write your code here
# class Movie():
#     def __init__(self,name,n,cost):
#         self.name = name
#         self.n = n
#         self.cost= cost
#     def __str__(self):
#         return "Movie : {}\nNumber of Tickets :{}\nTotal Cost :{}".format(self.name,self.n,self.cost)

# if __name__ == '__main__':
#     name = input()
#     n = int(input().strip())
#     cost = int(input().strip())
    
#     p1 = Movie(name,n,cost)
#     print(p1,str())
