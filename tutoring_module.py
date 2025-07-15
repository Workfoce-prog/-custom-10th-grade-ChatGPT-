
def tutor_response(subject, question):
    subject = subject.lower().strip()
    answers = {
        "biology": "Biology is the study of living organisms. Key areas include cells (the basic unit of life), genetics (DNA, heredity), and ecosystems. Example: Mitosis is a process where a cell divides into two identical daughter cells.",
        "geometry": "Geometry involves the study of shapes and their properties. A triangle has 3 angles that always sum to 180°. The Pythagorean theorem relates the sides of a right triangle: a² + b² = c².",
        "algebra": "Algebra uses symbols to solve equations. Example: To solve 2x + 3 = 11, subtract 3 and divide by 2: x = 4.",
        "chemistry": "Chemistry studies matter and its interactions. An atom has protons, neutrons, and electrons. Water (H₂O) is made of 2 hydrogen and 1 oxygen atom.",
        "civics": "Civics teaches how government works. The U.S. has 3 branches: Legislative (makes laws), Executive (enforces laws), Judicial (interprets laws).",
        "statistics": "Statistics involves collecting and analyzing data. Example: The mean of 5, 7, and 9 is (5+7+9)/3 = 7.",
        "social science": "Social science explores human society. Topics include culture, economics, and history. Sociology is the study of social behavior and institutions."
    }
    return answers.get(subject, "That's a great question. Let’s explore that topic together.")
