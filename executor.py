import requests
from cortex import new_client

# URL format: http://*****.elb.us-east-2.amazonaws.com/multiarmed-bandit
URL = "http://*****.elb.us-east-2.amazonaws.com/multiarmed-bandit"

# cluster name is regulary – "cortex"
# you can get operator_endpoint using cli command: cortex cluster info
# operator_endpoint="https://*****.elb.us-east-2.amazonaws.com"
cx = new_client(
    name="cortex",
    operator_endpoint="https://*****.elb.us-east-2.amazonaws.com",
)
# we will use two static configurations:
# configuration 1 – only positive numbers
new_traffic_splitter_spec_positive = {
    "name": "multiarmed-bandit",
    "kind": "TrafficSplitter",
    "apis": [
        {"name": "model-a", "weight": 100},
        {"name": "model-b", "weight": 0},
    ],
}
# configuration 2  – only negative numbers
new_traffic_splitter_spec_negative = {
    "name": "multiarmed-bandit",
    "kind": "TrafficSplitter",
    "apis": [
        {"name": "model-a", "weight": 0},
        {"name": "model-b", "weight": 100},
    ],
}
# let's initiate our bandit with "only positive" configuration
cx.deploy(new_traffic_splitter_spec_positive)

while True:
    response = requests.post(URL, json={"msg": "bla-bla"})
    print(response.text)
    implicit_feedback = ""
    while implicit_feedback.lower() not in ("y", "n"):
        implicit_feedback = input("do you like it? (y/n)\nYour answer is: ")
    if implicit_feedback == "y":
        continue
    else:
        if int(response.text) >= 0:
            # switch model to negative one
            cx.deploy(new_traffic_splitter_spec_negative)
        else:
            # switch model to positive one
            cx.deploy(new_traffic_splitter_spec_positive)
