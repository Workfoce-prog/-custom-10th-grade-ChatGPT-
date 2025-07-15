
def generate_lesson(topic):
    topic = topic.lower()
    content = {
        "biology": "### 🧬 Biology Lesson\nBiology is the study of life and living organisms...",
        "geometry": "### 📐 Geometry Lesson\nGeometry involves the study of shapes, sizes, and properties of space...",
        "algebra": "### ➕ Algebra Lesson\nAlgebra deals with symbols and rules for manipulating those symbols...",
        "chemistry": "### ⚗️ Chemistry Lesson\nChemistry is the science of matter and the changes it undergoes...",
        "civics": "### 🏛️ Civics Lesson\nCivics is the study of the rights and duties of citizenship...",
        "statistics": "### 📊 Statistics Lesson\nStatistics involves collecting, analyzing, and interpreting data...",
        "social science": "### 🌍 Social Science Lesson\nSocial science explores society and human relationships..."
    }
    return content.get(topic, f"### {topic.title()}\nLesson content coming soon.")
