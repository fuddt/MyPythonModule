import requests


auth_url = "https://api.box.com/oauth2/token"
data = {
    'grant_type': 'client_credentials',
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET'
}

response = requests.post(auth_url, data=data)
access_token = response.json()['access_token']

# Box API呼び出し
headers = {"Authorization": f"Bearer {access_token}"}
res = requests.get("https://api.box.com/2.0/users/me", headers=headers)