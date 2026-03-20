import re

# 🧹 Clean text input
def clean_text(text):
    if not text:
        return ""

    text = text.lower()                      # lowercase
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars
    text = re.sub(r"\s+", " ", text)         # remove extra spaces

    return text.strip()


# 🔗 Combine all inputs into one string
def combine_inputs(interests, skills, personality):
    interests = clean_text(interests)
    skills = clean_text(skills)
    personality = clean_text(personality)

    return f"{interests} {skills} {personality}"


# ⚠️ Validate input fields
def validate_input(interests, skills, personality):
    if not interests or not skills or not personality:
        return False, "All fields are required!"

    if len(interests) < 2 or len(skills) < 2:
        return False, "Input too short!"

    return True, "Valid input"