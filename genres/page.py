import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    # Buscando os dados reais
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')
        # Tranformar json para dataframe
        genres_df = pd.json_normalize(genres)

        AgGrid(
            data=genres_df,  # DataFrame do Pandas para o AgGrid
            reload_data=True,  # Força recarregar os dados
            key='genres_grid',  # Para identificar
        )
    else:
        st.warning('Nenhum Gênero encontrado.')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(
            name=name
        )
        if new_genre:
            st.rerun()  # refresh na página de generos, buscando de novo os gêneros
        else:
            st.error('Erro ao cadastrar o Gênero. Verifique os campos.')
