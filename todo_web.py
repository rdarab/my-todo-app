# to run the dode: in terminal write streamlit run file_name.py
import streamlit as st
from modules import functions

todos =  functions.read_file()

def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_to_file(todos)



st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input("Enter your productivity here", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
# The label is require element so in case we dont want it, it'll stay empty string

