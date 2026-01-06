import streamlit as st
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state:  # Já existe atores salvos na sessão?
            return st.session_state.actors
        # Se não existir, busca e salva
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        # Quando criar um ator novo, salva ele na sessão também
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
