import streamlit as st

st.set_page_config(layout='wide')

col1,col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png")
    content = """
    Hi, Im Bekhzod. Im a python developer!
    Ambitious and knowledge-thirsty person, team player and
    game-changer in this rapidly developing world.

    """
    st.write(content)

content2= """
Below you can find app developed by me in Python. Feel free to send me a message!
"""
st.write(content2)