import requests
def get_login_info(url, login_data) :
    return requests.post(url+"/user", json=login_data)

url = "https://dorandoran.site/api"

def login():
    login_data = {
    "id" : "어드민",
    "email" : "admin@test.com",
    "userRole" : "PARENT"
    }
    response = get_login_info(url, login_data)
    return response.headers.get("AccessToken")