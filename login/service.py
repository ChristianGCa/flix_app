import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password
    )
    # Se existe algum erro na resposta
    if response.get('error'):
        st.error(f'Falha ao realizar o login: {response.get("error")}')
    # Se não, armazenar o token na sessão
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    # Limpar todas as variáveis de ambiente da seção do usuário
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()
