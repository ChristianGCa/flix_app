import os
import requests
import streamlit as st
from dotenv import load_dotenv
from login.service import logout

load_dotenv()


class MovieRepository:

    def __init__(self):
        self.__base_url = os.getenv('API_URL')
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            json=movie,
        )
        if response.status_code == 201:  # 201 -> Criado com sucesso
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Erro ao obter dados da API. Status code: {response.status_code}. Body: {response.text}'
        )

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
