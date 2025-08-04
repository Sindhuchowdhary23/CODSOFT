import streamlit as st
from datetime import datetime, date

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "new_task" not in st.session_state:
    st.session_state.new_task = ""
if "new_due_date" not in st.session_state:
    st.session_state.new_due_date = date.today()

# Function to add a new task
def add_task():
    if st.session_state.new_task:
        st.session_state.tasks.append({
            "task": st.session_state.new_task,
            "done": False,
            "due_date": st.session_state.new_due_date
        })
        st.session_state.new_task = ""
        st.session_state.new_due_date = date.today()

# Function to mark a task as done
def mark_done(index):
    st.session_state.tasks[index]["done"] = True

# Function to delete a task
def delete_task(index):
    st.session_state.tasks.pop(index)

# Helper to calculate time remaining
def get_time_remaining(due_date):
    today = date.today()
    delta = (due_date - today).days
    if delta > 0:
        return f"🕒 {delta} day(s) left"
    elif delta == 0:
        return "⚠️ Due Today"
    else:
        return f"❗ Overdue by {-delta} day(s)"

# Page layout
st.set_page_config(page_title="To-Do App", layout="centered")
st.title("📝 To-Do List")
st.markdown("Manage your tasks efficiently with deadlines and a clean interface.")

# Add new task section
with st.container():
    st.subheader("➕ Add Task")
    st.text_input("Enter a task", key="new_task", placeholder="e.g. Finish homework")
    st.date_input("Select due date", key="new_due_date")
    st.button("Add Task", on_click=add_task)

# Show tasks
st.subheader("📋 Your Tasks")
if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")
else:
    for index, task in enumerate(st.session_state.tasks):
        with st.container(border=True):
            col1, col2, col3 = st.columns([6, 1.5, 1.5])
            status = "✅ Done" if task["done"] else "❌ Not Done"
            due_date_str = task["due_date"].strftime("%Y-%m-%d")
            time_remaining = get_time_remaining(task["due_date"])
            col1.markdown(
                f"**{index+1}. {task['task']}**  \n"
                f"_Status: `{status}`_  \n"
                f"📅 Due: `{due_date_str}`  \n"
                f"{time_remaining}"
            )
            if not task["done"]:
                col2.button("✔️ Done", key=f"done_{index}", on_click=mark_done, args=(index,))
            col3.button("🗑️ Delete", key=f"delete_{index}", on_click=delete_task, args=(index,))

