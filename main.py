import streamlit as st

st.set_page_config(layout='wide')

col1,col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png")
    content = """
    Hi, Im Bekhzod. Im a python developer!
    """
    st.write(content)