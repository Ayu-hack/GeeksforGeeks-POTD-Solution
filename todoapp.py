import streamlit as st
import pandas as pd

# Initialize session state
if 'todos' not in st.session_state:
    st.session_state.todos = pd.DataFrame(columns=['Task', 'Status'])

def add_todo():
    if st.session_state.new_todo:
        new_todo = pd.DataFrame({'Task': [st.session_state.new_todo], 'Status': ['Pending']})
        st.session_state.todos = pd.concat([st.session_state.todos, new_todo], ignore_index=True)
        st.session_state.new_todo = ""

def delete_todo(index):
    st.session_state.todos = st.session_state.todos.drop(index).reset_index(drop=True)

def toggle_status(index):
    current_status = st.session_state.todos.loc[index, 'Status']
    st.session_state.todos.loc[index, 'Status'] = 'Completed' if current_status == 'Pending' else 'Pending'

st.title("To-Do List App")

# Input for new todo
st.text_input("Add a new todo", key="new_todo", on_change=add_todo)

# Display todos
for index, todo in st.session_state.todos.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.write(f"{todo['Task']} - {todo['Status']}")
    
    with col2:
        st.button("Toggle", key=f"toggle_{index}", on_click=toggle_status, args=(index,))
    
    with col3:
        st.button("Delete", key=f"delete_{index}", on_click=delete_todo, args=(index,))

# Display dataframe (optional, for debugging)
st.write(st.session_state.todos)