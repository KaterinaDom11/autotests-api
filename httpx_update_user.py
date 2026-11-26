import httpx
from tools.fakers import get_random_email

create_users = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_users_response = httpx.post("http://localhost:8000/api/v1/users", json=create_users)
create_users_response_data = create_users_response.json()

print(create_users_response_data)
print(create_users_response.status_code)

login_users = {
    "email": create_users["email"],
    "password": create_users["password"],
}

login_users_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_users)
login_users_response_data = login_users_response.json()

print(login_users_response_data)
print(login_users_response.status_code)

update_users_authorization = {
    "Authorization": f"Bearer {login_users_response_data["token"]["accessToken"]}"
}
update_users = {
    "email": get_random_email(),
    "lastName": create_users["lastName"],
    "firstName": create_users["firstName"],
    "middleName": create_users["middleName"]
}

update_users_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_users_response_data["user"]["id"]}",
                                    headers=update_users_authorization, json=update_users)

print(update_users_response.json())
print(update_users_response.status_code)
