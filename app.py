import streamlit as st

# Fonction pour créer un fichier .txt
def create_file():
    with open("new_file.txt", "w") as file:
        file.write("This is a new file created by Streamlit.")

# Application Streamlit
st.write('hello')

# Ajouter un bouton pour créer le fichier
if st.button('Create File'):
    create_file()
    st.success('File created successfully!')
