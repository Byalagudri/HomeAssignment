import requests

def get_cad_api_data():
    url = "https://ssd-api.jpl.nasa.gov/cad.api"
    return requests.get(url)
