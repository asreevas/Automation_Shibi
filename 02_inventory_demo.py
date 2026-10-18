import yaml
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

INVENTORY_FILE = "Inventory-clab.yaml"

with open(INVENTORY_FILE, "r") as f:
   yaml_raw = f.read()
   
#pprint(yaml_raw)

    
inventory = yaml.safe_load(yaml_raw)
#pprint(inventory)

for device_name, details in inventory['devices'].items():
    # print(device_name)
    # pprint(details)
    # print("--------------------------------------------------")
    for key, value in details.items():
        # pprint(key)
        # pprint(value)
        if isinstance(value, str):
            details[key] = os.path.expandvars(value)

pprint(inventory)
        
