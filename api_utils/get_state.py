import requests
import json

from errors.BadResponse import BadResponse
from errors.StateError import StateError
from credentials import ip, octo_api

def get_state():
    SUCCESS_CODE = 200
    COOLED_TEMP = 30
    api_url = f'http://{ip}/api/printer'

    headers = {
        'X-Api-Key': octo_api
    }

    response = requests.get(api_url, headers=headers)

    if(response.status_code != SUCCESS_CODE):
        raise BadResponse(response.status_code, "Bad response code")
    
    data = json.loads(response.content)

    if('error' in data):
        raise StateError(data['error'])
    
    bed_act = data['temperature']['bed']['actual']
    bed_trg = data['temperature']['bed']['target']

    tool_act = data['temperature']['tool0']['actual']
    tool_trg = data['temperature']['tool0']['target']

    bed_heating = bed_act <= bed_trg    # check if the bed is heating
    if not bed_heating:
        if bed_act <= COOLED_TEMP:               # check if the bed is cooled down
            bed_heating = 0
        else: bed_heating = -1          # the bed is cooling down

    tool_heating = tool_act <= tool_trg # check if the tool is heating
    if not tool_heating:
        if tool_act <= COOLED_TEMP:              # check if the tool is cooled down
            tool_heating = 0
        else: tool_heating = -1         # the tool is cooling down

    return (bed_heating, bed_act, bed_trg), (tool_heating, tool_act, tool_trg)
