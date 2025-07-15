
def tutor_response(subject, question):
    subject = subject.lower()
    answers = {
        "biology": "Biology studies living organisms, cells, and ecosystems.",
        "geometry": "Geometry involves shapes, lines, and angles. A triangle's angles always add to 180°.",
        "algebra": "Algebra includes solving equations like x + 2 = 5.",
        "chemistry": "Chemistry focuses on elements, atoms, and chemical reactions.",
        "civics": "Civics teaches how government works, including rights and laws.",
        "statistics": "Statistics analyzes data using mean, median, and mode.",
        "social science": "Social science explores how societies work, including history and sociology."
    }
    return f"**{subject.title()} Help:**\n\n{answers.get(subject, 'Answer coming soon.')}"
