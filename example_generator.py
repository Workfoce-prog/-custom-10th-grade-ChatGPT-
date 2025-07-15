
def generate_example(topic):
    topic = topic.lower()
    examples = {
        "biology": "### Example: Mitosis\nA cell with 46 chromosomes divides into two cells, each with 46 chromosomes. This ensures identical genetic info.",
        "geometry": "### Example: Triangle\nIf angles are 50° and 60°, the third angle = 180 - (50 + 60) = 70°.",
        "algebra": "### Example: Solve 2x + 3 = 9\nStep 1: Subtract 3 → 2x = 6\nStep 2: Divide by 2 → x = 3",
        "chemistry": "### Example: Balance H₂ + O₂ → H₂O\nBalanced: 2H₂ + O₂ → 2H₂O",
        "civics": "### Example: Branches of Government\nThe President enforces laws (Executive), Congress makes laws (Legislative), Courts interpret laws (Judicial).",
        "statistics": "### Example: Mean\nSet: 4, 6, 8 → (4+6+8)/3 = 6",
        "social science": "### Example: Cultural Trait\nCelebrating holidays like Ramadan or Thanksgiving reflects cultural values."
    }
    return examples.get(topic, f"Example for {topic.title()} coming soon.")
