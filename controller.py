import json
import requests

endpoint = 'http://10.0.0.40/api/hRFZTQbeAwXBKBvP4OT5mRCDvRXYMmDIearvljNK/lights/1/state' 

agent_red =    {"on":True, "hue":0}
agent_blue =   {"on":True, "hue":46920}
agent_yellow = {"on":True, "hue":11000}
agent_white =  {"on":True, "xy":[0.4,0.35]}
agent_green =  {"on":True, "hue":25500}
agent_orange = {"on":True, "xy":[0.59,0.38]}
agent_off    = {"on":False}

dispatch = {
  'red': agent_red,
  'blue': agent_blue,
  'yellow': agent_yellow,
  'white': agent_white,
  'green': agent_green,
  'orange': agent_orange,
  'off': agent_off
}

while True:
  print "Color?"
  color = raw_input()
  if color == 'exit':
    exit()

  try:
    val = int(color)
    print "integer"
    r = requests.put(endpoint, data = json.dumps({"on":True, "sat":250, "bri":250, "hue":val}))
  except ValueError:
    r = requests.put(endpoint, data = json.dumps(dispatch[color]))


