
import random

def generate_quiz(topic, num_questions=3):
    topic = topic.lower()
    questions = {
        "biology": [
            {"question": "What is the basic unit of life?", "options": ["Cell", "Atom", "Organ", "Tissue"]},
            {"question": "Where does photosynthesis occur?", "options": ["Chloroplast", "Mitochondria", "Nucleus", "Ribosome"]}
        ],
        "geometry": [
            {"question": "Sum of angles in a triangle?", "options": ["180°", "90°", "360°", "270°"]},
            {"question": "Which shape has four equal sides?", "options": ["Square", "Rectangle", "Trapezoid", "Circle"]}
        ],
        "algebra": [
            {"question": "Solve for x: x + 5 = 10", "options": ["5", "15", "0", "10"]},
            {"question": "What is the slope in y = 2x + 3?", "options": ["2", "3", "5", "x"]}
        ],
        "chemistry": [
            {"question": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen", "Salt"]},
            {"question": "What’s the atomic number of Carbon?", "options": ["6", "12", "8", "4"]}
        ],
        "civics": [
            {"question": "How many branches of government?", "options": ["3", "2", "4", "5"]},
            {"question": "What is the Bill of Rights?", "options": ["First 10 amendments", "Declaration", "Articles", "Preamble"]}
        ],
        "statistics": [
            {"question": "What is the mean of 2, 4, 6?", "options": ["4", "6", "5", "2"]},
            {"question": "Mode of 1,2,2,3,4?", "options": ["2", "1", "3", "4"]}
        ],
        "social science": [
            {"question": "What is culture?", "options": ["Shared beliefs", "DNA", "Weather", "Currency"]},
            {"question": "What is sociology?", "options": ["Study of society", "Study of atoms", "Math field", "Map making"]}
        ]
    }
    return random.sample(questions.get(topic, []), k=min(num_questions, len(questions.get(topic, []))))
