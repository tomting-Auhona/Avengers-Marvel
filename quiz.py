import streamlit as st

# Define the questions and options
questions = [
    "Which superpower would you choose?",
    "What is your preferred weapon?",
    "Which word describes you best?",
    "How do you handle challenges?",
    "What is your favorite color?",
    "What is your ideal team size?",
    "What is your favorite hobby?",
    "How do you make decisions?",
    "What is your preferred mode of transportation?",
    "How do you handle responsibility?"
]

options = [
    ["Super strength", "Flight", "Telepathy", "Invisibility"],
    ["Sword", "Shield", "Bow and arrows", "Guns"],
    ["Brave", "Intelligent", "Determined", "Mysterious"],
    ["Face them head-on", "Analyze and strategize", "Seek help from others", "Adapt and improvise"],
    ["Red", "Blue", "Green", "Yellow"],
    ["Alone", "Small group", "Large team", "No preference"],
    ["Sports", "Reading", "Gaming", "Outdoor activities"],
    ["Trust your instincts", "Analyze pros and cons", "Seek advice from others", "Go with the flow"],
    ["Sports car", "Motorcycle", "Jet", "Public transportation"],
    ["Take charge", "Delegate tasks", "Work as a team", "Depends on the situation"]
]

# Avengers Characters with broader score ranges
avengers_characters = {
    "Iron Man": [70, 100],
    "Captain America": [50, 69],
    "Black Widow": [40, 49],
    "Thor": [90, 100],
    "Hulk": [60, 89],
    "Black Panther": [40, 59],
    "Spider-Man": [50, 69],
    "Doctor Strange": [80, 100],
    "Captain Marvel": [70, 100],
    "Scarlet Witch": [60, 79],
    "Hawkeye": [40, 59],
    "Nick Fury": [60, 79],
    "Ant-Man": [50, 69],
    "Wasp": [40, 59],
    "Vision": [80, 100],
    "Falcon": [50, 69],
    "War Machine": [60, 79],
    # Add more characters here
}

# Avenger character explanations
explanations = {
    "Iron Man": "You have a strong sense of innovation and are a natural leader.",
    "Captain America": "You value justice, honor, and teamwork above all else.",
    "Black Widow": "You are highly skilled, adaptable, and resourceful.",
    "Thor": "You possess great strength, courage, and a strong sense of duty.",
    "Hulk": "You are powerful and have a tendency to let your emotions get the best of you.",
    "Black Panther": "You are wise, noble, and deeply connected to your heritage.",
    "Spider-Man": "You are smart, witty, and always strive to do the right thing.",
    "Doctor Strange": "You are intelligent, mystical, and have a deep understanding of the universe.",
    "Captain Marvel": "You are confident, determined, and possess immense power.",
    "Scarlet Witch": "You are complex, with a deep well of power and emotion.",
    "Hawkeye": "You are skilled, focused, and fiercely loyal to your friends.",
    "Nick Fury": "You are strategic, resourceful, and always stay one step ahead.",
    "Ant-Man": "You are inventive, quick-witted, and love a good challenge.",
    "Wasp": "You are bold, adventurous, and always ready to take on the world.",
    "Vision": "You are intelligent, compassionate, and seek to understand humanity.",
    "Falcon": "You are loyal, courageous, and always willing to fight for what's right.",
    "War Machine": "You are reliable, disciplined, and a true team player.",
    # Add more character explanations here
}

# Function to calculate the Avenger character based on user's answers
def calculate_avenger(answers):
    scores = {avenger: 0 for avenger in avengers_characters}
    for i, answer in enumerate(answers):
        for avenger, score_range in avengers_characters.items():
            scores[avenger] += score_range[min(len(score_range) - 1, answer - 1)]

    return max(scores, key=scores.get), scores[max(scores, key=scores.get)]

# Streamlit app
def main():
    st.title("Which Avenger Are You?")
    st.write("Answer the following questions to find out!")

    answers = []

    # Display questions and collect answers
    for i in range(len(questions)):
        st.write(f"**Question {i+1}:** {questions[i]}")
        option = st.radio("Choose one:", options[i], key=i)
        answers.append(options[i].index(option) + 1)  # Index starts from 1

    # Calculate Avenger character
    avenger, total_score = calculate_avenger(answers)

    # Display result and explanation
    st.write(f"You are {avenger}!")
    st.write(f"Explanation: {explanations[avenger]}")
    st.write(f"Total score: {total_score}")

if __name__ == "__main__":
    main()
