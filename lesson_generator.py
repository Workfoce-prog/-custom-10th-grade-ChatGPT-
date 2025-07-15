
def generate_lesson(topic):
    topic = topic.lower()
    lessons = {
        "biology": """
### 🧬 Lesson: Biology Basics

Biology is the science of life. It includes:

- **Cell Theory**: All living things are made of cells.
- **Genetics**: DNA carries genetic information.
- **Evolution**: Populations change over generations.
- **Ecology**: Interactions between organisms and environment.

Real Example: Mitosis is the process by which cells divide to create new cells.

Practice: What organelle is the control center of the cell?
""",
        "geometry": """
### 📐 Lesson: Geometry Essentials

- **Triangles**: Angles sum to 180°.
- **Types**: Equilateral, isosceles, scalene
- **Circles**: Radius, diameter, area = πr²
- **Theorems**: Pythagorean (a² + b² = c²)

Real Example: In a right triangle with legs 3 and 4, the hypotenuse is √(3² + 4²) = 5.

Practice: What is the area of a circle with radius 3?
""",
        "algebra": """
### ➕ Lesson: Algebra Fundamentals

- **Expressions**: 2x + 3
- **Equations**: Solve for x in 3x = 12 → x = 4
- **Inequalities**: x > 5
- **Functions**: f(x) = 2x + 1

Real Example: Graph y = 2x + 1 shows a line with slope 2 and y-intercept 1.

Practice: Solve 2x - 4 = 6
""",
        "chemistry": """
### ⚗️ Lesson: Chemistry Overview

- **Atoms**: Smallest unit of matter
- **Periodic Table**: Organizes elements
- **Bonds**: Ionic, covalent
- **Chemical Reactions**: Reactants → Products

Example: 2H₂ + O₂ → 2H₂O

Practice: What subatomic particles are in the nucleus?
""",
        "civics": """
### 🏛️ Lesson: Civics and Government

- **Constitution**: Supreme law
- **Branches**: Legislative, Executive, Judicial
- **Bill of Rights**: Protects freedoms
- **Civic Duties**: Voting, obeying laws

Practice: What branch interprets laws?
""",
        "statistics": """
### 📊 Lesson: Statistics Basics

- **Mean**: Average
- **Median**: Middle value
- **Mode**: Most frequent
- **Range**: Max - Min

Practice: What is the mean of 10, 20, 30?
""",
        "social science": """
### 🌍 Lesson: Social Science Concepts

- **Culture**: Shared beliefs and practices
- **Economics**: Study of choices and trade
- **Sociology**: Study of society
- **History**: Study of the past

Practice: What is an example of a cultural practice?
"""
    }
    return lessons.get(topic, f"Lesson for {topic.title()} coming soon.")
