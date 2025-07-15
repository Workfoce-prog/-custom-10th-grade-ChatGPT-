
def generate_example(topic):
    topic = topic.lower()
    examples = {
        "biology": "### Example: Biology\nThe mitochondria is known as the powerhouse of the cell.",
        "geometry": "### Example: Geometry\nIn a triangle with angles 50° and 60°, the third angle is 70°.",
        "algebra": "### Example: Algebra\nx + 5 = 10 → x = 10 - 5 → x = 5",
        "chemistry": "### Example: Chemistry\nBalancing H2 + O2 → H2O: Balanced form is 2H2 + O2 → 2H2O",
        "civics": "### Example: Civics\nThe First Amendment protects freedom of speech.",
        "statistics": "### Example: Statistics\nMean of 2, 4, 6: (2+4+6)/3 = 4",
        "social science": "### Example: Social Science\nCulture includes beliefs, traditions, and language."
    }
    return examples.get(topic, f"### Example for {topic.title()}\nComing soon...")
