
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd
from lesson_generator import generate_lesson
from quiz_generator import generate_quiz
from example_generator import generate_example
from tutoring_module import tutor_response
from translator import translate_text
from gamification import update_points_and_badges, get_user_progress
from pathlib import Path
from datetime import datetime

# --- Auth Setup ---
with open("config.yaml") as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, auth_status, username = authenticator.login("main")

if auth_status is False:
    st.error("Incorrect username or password")
elif auth_status is None:
    st.warning("Please enter your username and password")
elif auth_status:
    st.sidebar.title("🧭 Subject Menu")
    subject = st.sidebar.selectbox("Choose a subject", [
        "Biology", "Geometry", "Algebra", "Chemistry", "Civics",
        "Statistics", "Social Science"
    ])
    st.sidebar.markdown("---")
    tab = st.sidebar.radio("Select Feature", ["📚 Lesson", "🧠 Quiz", "📝 Example", "👩‍🏫 Tutor Chat"])

    language = st.sidebar.selectbox("🌍 Language", ["English", "Spanish", "French", "Swahili", "Arabic", "Bambara"])
    st.sidebar.markdown("---")
    authenticator.logout("Logout", "sidebar")

    st.title(f"📘 10th Grade AI Tutor – {subject}")

    points, badges = get_user_progress(username)
    st.sidebar.info(f"**Points:** {int(points)}\n**Badges:** {badges}")

    if tab == "📚 Lesson":
        lesson = generate_lesson(subject)
        lesson = translate_text(lesson, language)
        st.markdown(lesson)
        st.session_state[f"{username}_{subject}_lesson_viewed"] = True

    elif tab == "🧠 Quiz":
        update_points_and_badges(username, "🧠 Quiz")
        num_questions = st.slider("Number of Questions", 1, 5, 3)
        quiz = generate_quiz(subject, num_questions)
        score = 0
        for q in quiz:
            st.write(f"**Q:** {translate_text(q['question'], language)}")
            for i, option in enumerate(q["options"]):
                st.write(f"{chr(65+i)}. {translate_text(option, language)}")
            st.write("---")
        st.session_state[f"{username}_{subject}_quiz"] = True

    elif tab == "📝 Example":
        update_points_and_badges(username, "📝 Example")
        example = generate_example(subject)
        example = translate_text(example, language)
        st.markdown(example)
        st.session_state[f"{username}_{subject}_example"] = True

    elif tab == "👩‍🏫 Tutor Chat":
        update_points_and_badges(username, "👩‍🏫 Tutor Chat")
        question = st.text_input("Ask a question about this subject:")
        if st.button("Get Answer") and question:
            answer = tutor_response(subject, question)
            answer = translate_text(answer, language)
            st.markdown(answer)

    # Progress Tracking
    log_data = {
        "user": username,
        "subject": subject,
        "feature": tab,
        "timestamp": datetime.now().isoformat()
    }
    log_path = Path("progress_log.csv")
    df = pd.DataFrame([log_data])
    if log_path.exists():
        df.to_csv(log_path, mode='a', header=False, index=False)
    else:
        df.to_csv(log_path, index=False)
