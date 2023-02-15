import requests
from datetime import datetime

graph="graph1"
params = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph1 = f"{pixal}/{user}/graphs"
graph_param = {
    "id": "graph1",
    "name": "Coing Graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}

header = {
    "X-USER-TOKEN": token
}

time=datetime.now()
var=(time.strftime("%Y%m%d"))

habit_add={
    "date":var,
    "quantity":input("ENTER HERE")
}

update_pixal=f"{graph1}/{graph}/{var}"
response=requests.post(url=update_pixal,json=habit_add,headers=header)
print(response.text)
