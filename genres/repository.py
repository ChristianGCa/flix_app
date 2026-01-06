import os
import requests
import streamlit as st
from dotenv import load_dotenv
from login.service import logout

load_dotenv()


class GenreRepository:

    def __init__(self):
        self.__base_url = os.getenv('API_URL')
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # Se o token expirar, jogue o usuário pra fora do sistema
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:  # 201 -> Criado com sucesso
            return response.json()
        # Se o token expirar, jogue o usuário pra fora do sistema
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
