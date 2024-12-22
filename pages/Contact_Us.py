import streamlit as st

st.header("Contact us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message= st.text_area("Your message")
    button = st.form_submit_button("Send")



# col1,col2 = st.columns(2)
#
# with col1:
#     st.image("images/gmail.png")
#     content = """Contact me via gmail!"""
#     st.write(content)

icon_path = "images/gmail.png"

st.markdown(
    f"""
    <a href="mailto:muminov.b0509@gmail.com" target="_blank">
    <img src="{icon_path}" style="width:20px; height:20px; margin-right:5px;"> 
    Send us a message!
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    
    """
)
