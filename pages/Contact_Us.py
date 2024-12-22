import streamlit as st

st.header("Contact us")

contact_form = """
<form action="https://usebasin.com/f/c5589e8160f1" method = "POST">
    <input type = "text" name ="name" placeholder="Your name" required>
    <input type = "email" name ="email" placeholder="Your email" required>
    <textarea name="message" placeholder=""Your message here> </textarea>
    <button type="submit">Send </button>
</form>
"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>f{f.read()}</style>',unsafe_allow_html=True)

local_css("style/style.css")

col1,col2 = st.columns(2)

with col1:
    st.image("images/gmail.png", width=100)
    st.markdown("Contact me! muminov.b0509@gmail.com")

with col2:
    st.image("images/linkedin.png",width=100)
    st.markdown("Reach me out on LinkedIn https://www.linkedin.com/in/bekhzod-muminov-756a75172/" )

