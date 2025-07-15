
import streamlit as st
from lesson_generator import generate_lesson
from quiz_generator import generate_quiz
from example_generator import generate_example
from tutoring_module import tutor_response

st.set_page_config(page_title="10th Grade AI Tutor", layout="wide")

st.title("📘 10th Grade AI Tutor Assistant")
st.write("Choose a feature below to get started:")

tab1, tab2, tab3, tab4 = st.tabs(["📚 Lesson Generator", "🧠 Quiz Generator", "📝 Example Help", "👩‍🏫 Tutor Chat"])

with tab1:
    topic = st.text_input("Enter a topic (e.g., 'Photosynthesis', 'Triangles', 'Bill of Rights'):")
    if st.button("Generate Lesson") and topic:
        lesson = generate_lesson(topic)
        st.markdown(lesson)

with tab2:
    quiz_topic = st.text_input("Quiz Topic:")
    num_questions = st.slider("Number of Questions", 1, 10, 5)
    if st.button("Generate Quiz"):
        quiz = generate_quiz(quiz_topic, num_questions)
        for q in quiz:
            st.write(f"**Q:** {q['question']}")
            for i, option in enumerate(q["options"]):
                st.write(f"{chr(65+i)}. {option}")
            st.write("---")

with tab3:
    example_topic = st.text_input("Example Topic (e.g., 'Solve x^2 = 9'):")
    if st.button("Show Example") and example_topic:
        example = generate_example(example_topic)
        st.markdown(example)

with tab4:
    question = st.text_input("Ask a question (any subject):")
    if st.button("Get Answer") and question:
        answer = tutor_response(question)
        st.markdown(answer)
