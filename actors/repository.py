import os
import requests
import streamlit as st
from dotenv import load_dotenv
from login.service import logout

load_dotenv()


class ActorRepository:

    def __init__(self):
        self.__base_url = os.getenv('API_URL')
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')
