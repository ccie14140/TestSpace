import json
from pprint import pprint

with open("FMG_data.json") as data_file:
    data = json.load(data_file)
    
FMG_IP = data["FMG_IP"]
FMG_API_USER = data["API-username"]
FMG_API_PASSWORD = data["API-password"]

print("The target IP is: " + FMG_IP)
print("The API username is: " + FMG_API_USER + ", using password: " + FMG_API_PASSWORD)
