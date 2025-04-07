# List of countries and their capitals
quiz_questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Greece": "Athens"
}

# Welcome message
print("Welcome to the European Capitals Quiz!\n")

# Score tracker
score = 0

# Ask each question
for country, capital in quiz_questions.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.\n")

# Final score
print(f"You got {score} out of {len(quiz_questions)} correct.")
