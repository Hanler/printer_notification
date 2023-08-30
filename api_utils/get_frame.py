import requests

from errors.BadResponse import BadResponse
from credentials import ip

def get_frame():
    SUCCESS_CODE = 200
    api_url = f'http://{ip}/webcam/?action=snapshot'

    response = requests.get(api_url)

    if(response.status_code == SUCCESS_CODE):
        return response.content
    else:
        raise BadResponse(response.status_code, "Bad response code")
