
import random

def generate_quiz(topic, num_questions=2):
    topic = topic.lower()
    quiz_bank = {
        "biology": [
            {"question": "What is the basic unit of life?", "options": ["Tissue", "Organ", "Cell", "Organism"], "answer": "Cell"},
            {"question": "Where does photosynthesis occur?", "options": ["Mitochondria", "Chloroplast", "Nucleus", "Ribosome"], "answer": "Chloroplast"}
        ],
        "geometry": [
            {"question": "Sum of angles in a triangle?", "options": ["180°", "90°", "360°", "270°"], "answer": "180°"},
            {"question": "What is the area of a circle with radius 2?", "options": ["4π", "2π", "π", "8π"], "answer": "4π"}
        ],
        "algebra": [
            {"question": "Solve: 2x = 10", "options": ["4", "5", "6", "10"], "answer": "5"},
            {"question": "What is the slope of y = 3x + 2?", "options": ["3", "2", "5", "0"], "answer": "3"}
        ],
        "chemistry": [
            {"question": "What is the symbol for water?", "options": ["H2O", "O2", "CO2", "H2"], "answer": "H2O"},
            {"question": "What charge do protons carry?", "options": ["Positive", "Negative", "Neutral", "None"], "answer": "Positive"}
        ],
        "civics": [
            {"question": "Who makes federal laws?", "options": ["Congress", "President", "Courts", "States"], "answer": "Congress"},
            {"question": "What does the Judicial branch do?", "options": ["Interpret laws", "Make laws", "Enforce laws", "Elect leaders"], "answer": "Interpret laws"}
        ],
        "statistics": [
            {"question": "Mean of 2, 4, 6?", "options": ["4", "5", "6", "3"], "answer": "4"},
            {"question": "What is the mode of 2, 2, 3, 4?", "options": ["2", "3", "4", "none"], "answer": "2"}
        ],
        "social science": [
            {"question": "What does sociology study?", "options": ["Atoms", "Maps", "Society", "Cells"], "answer": "Society"},
            {"question": "Which is a cultural element?", "options": ["Language", "Wind", "Height", "Metal"], "answer": "Language"}
        ]
    }
    return random.sample(quiz_bank.get(topic, []), k=min(num_questions, len(quiz_bank.get(topic, []))))
