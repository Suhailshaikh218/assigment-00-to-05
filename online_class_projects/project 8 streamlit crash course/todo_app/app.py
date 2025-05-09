import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title('📝 To-Do List Web App')

# Input for new task
new_task = st.text_input('Enter a new task:')
if st.button('Add Task'):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success('✅ Task added!')

# Display tasks
if st.session_state.tasks:
    st.subheader('Your Tasks:')
    for index, task in enumerate(st.session_state.tasks):
        st.write(f"{index + 1}. {task}")
        if st.button(f'Delete {index + 1}', key=f"del_{index}"):
            st.session_state.tasks.pop(index)
            st.experimental_rerun()
else:
    st.info("No tasks yet. Add a task to get started.")
