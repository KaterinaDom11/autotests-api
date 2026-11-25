import httpx

login = {"email": "user11@example.com",
         "password": "string"}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login)
login_response_data = login_response.json()

print(login_response_data)
print(login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(user_response.json())
print(user_response.status_code)
