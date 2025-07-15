
import streamlit as st

def init_review_session():
    if "review_history" not in st.session_state:
        st.session_state.review_history = []

def save_to_review(question, answer):
    st.session_state.review_history.append({"question": question, "answer": answer})

def display_review():
    st.subheader("🔁 Review Mode")
    if not st.session_state.review_history:
        st.info("No reviewed items yet.")
    else:
        for i, item in enumerate(st.session_state.review_history[::-1], 1):
            st.markdown(f"**{i}. Q:** {item['question']}\n**A:** {item['answer']}")
