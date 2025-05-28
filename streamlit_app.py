import streamlit as st
from src.service import url_service as url

# Inicializa o session state
if 'phone_number' not in st.session_state:
    st.session_state['phone_number'] = ''

if 'whatsapp_url' not in st.session_state:
    st.session_state['whatsapp_url'] = ''

def update_whatsapp_url():
    new_url = url.create_new_url(st.session_state.phone_input)
    st.session_state.whatsapp_url = new_url

def create_whatsapp_url(phone_number):
    if phone_number:
        return url.create_new_url(phone_number)
    return ''

## Interface
st.title("WhatsApp Add")
st.write("Start chats without need to create a contact.")

phone_number = st.text_input(
    "Phone Number",
    key="phone_input",
    on_change=update_whatsapp_url,
    placeholder="Ex: +5511999999999"
)

# Botão só aparece se houver URL válida
if st.session_state.whatsapp_url:
    st.link_button('Open WhatsApp Chat', url=st.session_state.whatsapp_url)
else:
    st.info("Digite um número de telefone para abrir o chat no WhatsApp")