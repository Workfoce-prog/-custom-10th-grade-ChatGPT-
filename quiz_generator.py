
import random

def generate_quiz(topic, num_questions=5):
    sample_questions = [
        {
            "question": f"What is the main idea of {topic}?",
            "options": ["Definition", "Cause", "Effect", "None of the above"]
        },
        {
            "question": f"Which of the following relates to {topic}?",
            "options": ["Option A", "Option B", "Option C", "Option D"]
        }
    ]
    return random.choices(sample_questions, k=num_questions)
