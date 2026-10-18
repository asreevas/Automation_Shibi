import os
import yaml
from pprint import pprint
from dotenv import load_dotenv 
from netmiko import ConnectHandler

load_dotenv()

with open("Inventory-clab.yaml", "r") as f:
    inventory = yaml.safe_load(f.read())
    
pprint(inventory)

print("--------------------------------------------------")

for device_name, details in inventory['devices'].items():
    SW1 = inventory['devices']['sw01']

pprint(SW1)

print("--------------------------------------------------")

for key, value in SW1.items():  
    if isinstance(value, str):
        SW1[key] = os.path.expandvars(value)
        
pprint(SW1)

print("--------------------------------------------------")

connection = ConnectHandler(
    device_type=SW1["device_type"],
    host=SW1["host"],
    username=SW1["username"],
    password=SW1["password"],
    port=SW1["port"],
)

print(connection.send_command("show version"))





