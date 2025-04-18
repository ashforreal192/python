import requests

def fetch_user_api():
    url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url) # Fetches data from url
    data = response.json() # COnverts data in response to json format and holding it in data variable.

    if data["success"] and "data" in data:
        userdata = data["data"]
        username = userdata["login"]["username"]
        country = userdata["location"]["country"]
        return username, country
    
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fetch_user_api()
        print(f"Username: {username}\nCountry of residence: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()