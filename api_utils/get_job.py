import requests
import json

from errors.BadResponse import BadResponse
from errors.JobError import JobError
from credentials import ip, octo_api

def get_job():
    SUCCESS_CODE = 200
    api_url = f'http://{ip}/api/job'
    
    headers = {
        'X-Api-Key': octo_api
    }

    response = requests.get(api_url, headers=headers)

    if(response.status_code != SUCCESS_CODE):
        raise BadResponse(response.status_code, "Bad response code")
    
    data = json.loads(response.content)
    
    if('error' in data):
        raise JobError(data['state'], data['error'])

    return data['state'], \
        [
            data['job']['file']['name'],        # name of file to print
            data['job']['estimatedPrintTime'],  # estimated print time
            data['progress']['printTime'],      # print time
            data['progress']['printTimeLeft']   # print time left
        ]
