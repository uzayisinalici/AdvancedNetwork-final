import csv
import requests


host = "192.168.110.129"
port = "8181"
username = "karaf"
password = "karaf"
url = f"http://192.168.110.129:8181/onos/v1/acl/rules"
headers = {'Content-type': 'application/json'}


policyFile = "firewall-policies.csv"
firewall_rules = []
with open(policyFile, 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in rows:
        if line_count == 0:
            line_count += 1
            continue
        firewall_rules.append((row[1], row[2]))
        line_count += 1


# Define the flow rule payload
flow_rule = {
    "priority": 10,
    "timeout": 0,
    "isPermanent": True,
    "deviceId": "switch1",  
    "treatment": {
        "instructions": [
            {
                "type": "OUTPUT",
                "port": 2  
            }
        ]
    },
    "selector": {
        "criteria": [
            {
                "type": "IN_PORT",
                "port": 1 
            }
        ]
    }
}


# Send the REST API request to add the flow rule
response = requests.post("http://192.168.110.129:8181/onos/v1/acl/rules", data=csv.dumps(flow_rule))

for rule in firewall_rules:
    resp = requests.post(
        url,
        json={
            "srcIp": "10.0.0.0/24",
            "srcMac": rule[0],
            "dstMac": rule[1]
        },
        auth=(username, password)
    )
    print(resp.text)
