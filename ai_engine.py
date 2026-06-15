def ask_ai(prompt):
    prompt = prompt.lower()

    if "study plan" in prompt:
        return "Study 2 hours daily and revise every weekend."

    elif "quiz" in prompt:
        return "1. What is AI? A) Artificial Intelligence"

    elif "career" in prompt:
        return "Learn Python, Machine Learning and AI Projects."

    else:
        return f"You asked: {prompt}"
