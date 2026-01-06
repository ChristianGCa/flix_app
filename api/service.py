import os
import requests
from dotenv import load_dotenv

load_dotenv()


# Esse será o cliente de autenticação
class Auth:

    def __init__(self):
        # os dois underscores indicam que são atributos privados
        self.__base_url = os.getenv('API_URL')
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
