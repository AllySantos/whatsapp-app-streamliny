import streamlit as st
from src.service import url_service as url

if 'phone_number' not in st.session_state:
    st.session_state['phone_number'] = ''


def set_link_button():
    new_url = url.create_new_url(phone_number)
    st.session_state.phone_number = new_url


## Interface

st.title("WhatsApp Add")
st.write(
    "Start chats without need to create a contact."
)
phone_number = st.text_input("Phone Number", on_change=set_link_button)



st.link_button('click', url=st.session_state.phone_number)
# if clicked_send_number:
#     new_url = url.create_new_url(phone_number)
#
#     st.write(new_url)
#
