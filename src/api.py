import requests

class UserAPI:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/auth/"

    @staticmethod
    def create_user(email, password, name):
        headers = {
            "Content-Type": "application/json",
            # Дополнительные заголовки, если нужно
        }
        try:
            response = requests.post(
                UserAPI.BASE_URL + "register",
                json={"name": name, "email": email, "password": password},
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err.response.status_code} - {err.response.text}")
            raise
        except requests.exceptions.RequestException as err:
            print(f"Request failed: {err}")
            raise
