import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    # Buscando os dados reais
    movies = movie_service.get_movies()
    if movies:

        st.write('Lista de Filmes')

        movies_df = pd.json_normalize(movies)
        # Remover colunas desnecessárias. Actors apareceria como objeto
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        AgGrid(
            data=movies_df,
            reload_data=True,  # Força recarregar os dados
            key='movies_grid',  # Para identificar
        )
    else:
        st.warning('Nenhum Filme encontrado.')

    st.title('Cadastrar novo Filme')

    title = st.text_input('Título do Filme')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',  # Formato visual, não o que mandamos pra API
    )

    # Buscar os gêneros disponíveis usando o serviço de Gêneros
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
        label='Gênero',
        options=list(genre_names.keys()),
    )

    # Buscar os atores disponíveis usando o serviço de Atores
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actor_names = st.multiselect(
        label='Atores/Atrizes',
        options=list(actor_names.keys()),
    )
    selected_actors_ids = [actor_names[name] for name in selected_actor_names]  # [1, 3, 4] por exemplo

    resume = st.text_area('Resumo do Filme')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o Filme. Verifique os campos.')
