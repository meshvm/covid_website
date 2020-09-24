'''Confirmed Cases API: ​ https://api.rootnet.in/covid19-in/stats/history
Sample Tested API: ​ https://api.rootnet.in/covid19-in/stats/testing/history
Consider the “totalConfirmed” field from the ​ Confirmed Cases API​ and “totalSamplesTested”
field from the ​ Sample Tested API​ for stats comparison.
● Create a line graph showing the daily statistics comparison between both the sample
●
tests and confirmed cases.
Create a dropdown bar named as “States” to select any State or Union Territory from a
list of all the States & Union Territories and text boxes to select date range.'''

import json
import requests
import re, datetime, string
confm = requests.get("https://api.rootnet.in/covid19-in/stats/history")
todos = json.loads(confm.text)
print(todos['totalSamplesTested'])
responses = requests.get("https://api.rootnet.in/covid19-in/stats/testing/history")
todos_grp = json.loads(responses.text)
print(todos_grp['totalSamplesTested'])