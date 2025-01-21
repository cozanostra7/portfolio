import streamlit as st
import pandas as pd

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('data.csv',sep=";")
with col3:
    for index, row in df[0:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

# with col4:
#     for index,row in df[10:].iterrows():
#         st.header(row['title'])
#         st.write(row['description'])
#         st.image("images/" + row['image'])
