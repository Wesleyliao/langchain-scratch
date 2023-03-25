import streamlit as st

from main import query_agent


def run_query(query: str) -> None:
    if query:
        output = query_agent(query)
        st.session_state.result = output


if "result" not in st.session_state:
    st.session_state["result"] = ""

st.title("🗃️ Dropbox Organizer 🗃️")
query = st.text_input("Enter a command for the organizer to execute.")
st.button("Submit", on_click=run_query, args=(query,))
st.write(st.session_state.result)
