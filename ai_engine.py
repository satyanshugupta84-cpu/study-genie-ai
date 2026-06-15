def ask_ai(prompt):
    if "study plan" in prompt.lower():
        return "Study 2 hours daily and revise every weekend."

    elif "quiz" in prompt.lower():
        return "1. What is AI? A) Artificial Intelligence"

    elif "career" in prompt.lower():
        return "Learn Python, Machine Learning and AI Projects."

    else:
        return "I am StudyGenie AI. Ask me about studies, quizzes or careers."
