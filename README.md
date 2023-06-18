# Mininet Remote Controller Project
This project demonstrates the integration of Mininet, a network emulator, with a remote controller using OpenFlow. It allows you to add OpenFlow rules to switches deployed in the Mininet environment through various methods such as Mininet CLI, UI, and REST API. Additionally, it provides an example of building a custom application code to find the shortest path based on packet statistics.

# Project Structure
The project is organized as follows:

topology.py: Python script for setting up the Mininet environment and creating the desired network topology.
controller.py: Python script for the remote controller application.
traffic_generator.py: Python script for generating network traffic using D-ITG.
README.md: Documentation file explaining the project and its usage.
Prerequisites
Before running this project, ensure that you have the following software and dependencies installed:

# Mininet: Install Mininet using the instructions provided in the Mininet website.
D-ITG: Install D-ITG for network traffic generation. You can find it at D-ITG.
Usage
Setting up the Mininet environment:

Run the topology.py script to set up the desired network topology in Mininet.
Modify the script to define your specific topology by using the Mininet API.
Ensure that the remote controller IP and port are correctly set for the switches.
Save the file and execute it using the Python interpreter.
Embedding OpenFlow rules using Mininet CLI:

Once the Mininet environment is running, access the Mininet CLI.
Use the provided commands in the CLI to add OpenFlow rules to the switches.
Modify the commands according to your specific flow rule requirements.
Generating traffic:

Run the traffic_generator.py script to generate network traffic using D-ITG.
Customize the script to define your specific traffic workload or use D-ITG parameters.
Simulating link failure:

Use Mininet CLI commands to bring down specific links in the network.
Observe the behavior of the remote controller and the network using Wireshark.
Embedding OpenFlow rules using UI:

Use the UI of the remote controller to add OpenFlow rules to the switches.
Repeat the traffic generation and link failure steps to observe the behavior.
Embedding OpenFlow rules using REST API:

Send HTTP requests to the remote controller's REST API to add OpenFlow rules.
Implement a requester client in your preferred programming language to handle the requests.
Repeat the traffic generation and link failure steps to observe the behavior.
Building and activating the custom application code:

Identify the services responsible for layer2/layer3 forwarding in the remote controller.
Deactivate the relevant service and extract the code to a development environment.
Implement your custom service that finds the shortest path based on packet statistics.
Embed OpenFlow layer2/layer3 rules to the switches on the shortest path.
Activate your custom service on the remote controller.

# STEPS

![mininetg](https://github.com/uzayisinalici/final-project/assets/91671512/0b9c0bdc-285a-4c1d-9b7b-8fcf5711c4ed)
![m](https://github.com/uzayisinalici/final-project/assets/91671512/433bb791-59c2-499d-bf57-b090fc9a98cd)
Mininet Machine

![onos](https://github.com/uzayisinalici/final-project/assets/91671512/40133c3e-0e91-470e-8724-7e3a0674b084)

![dfgdfgfd](https://github.com/uzayisinalici/final-project/assets/91671512/4cf2bfa4-3a07-412c-9f56-818684e6c330)![dsfd](https://github.com/uzayisinalici/final-project/assets/91671512/d051c114-5be2-4299-8e42-c6cdf621332d)

![f](https://github.com/uzayisinalici/final-project/assets/91671512/62453615-81ab-4a02-a92f-fc3411ff31d8)
