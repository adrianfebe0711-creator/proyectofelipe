import streamlit as st

st.title("mi proyecto")

import streamlit as st

# Diccionario de usuarios de ejemplo
USERS = {
    "admin": "1234",
    "usuario": "abcd"
}

def login():
    

    # Formulario de login
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Ingresar")

    # Validación
    if submit:
        if username in USERS and USERS[username] == password:
            st.success(f"Bienvenido, {username}")
            st.write("Acceso concedido a la aplicación.")
        else:
            st.error("Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    login()
