import requests
import credentials

dashboard_api = 'https://api.signalfx.com/v2/dashboard/'
chart_api = 'https://api.signalfx.com/v2/chart/'

sfx_headers = {
    'X-SF-TOKEN': credentials.token,
    'Content-Type': 'application/json'
}

# TODO make these helpers private if this becomes a class
def sfx_get(url, id):
    response = requests.get(url + str(id), headers=sfx_headers)
    if response.status_code != 200:
        raise Exception("Failed to retrieve: {}, Response body: {}".format(response.status_code, response.text))
    else:
        return response.text

def sfx_post(url, payload):
    response = requests.post(url, headers=sfx_headers, json=payload)
    if response.status_code != 200:
        raise Exception("Failed to create: {}, Response body: {}".format(response.status_code, response.text))
    else:
        return response.text


# TODO: proper exception handling
def get_dashboard(id):
    return sfx_get(dashboard_api, id)

def get_chart(id):
    return sfx_get(chart_api, id)

def post_dashboard(payload):
    return sfx_post(dashboard_api, payload)

def post_chart(payload):
    return sfx_post(chart_api, payload)