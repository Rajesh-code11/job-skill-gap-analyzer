import re


def extract_skills(text, skill_dictionary):
    """
    Extract technical skills from text using boundary-aware matching.
    """

    text_lower = text.lower()
    found_skills = []

    for skill in skill_dictionary:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills


def analyze_skill_gap(user_skills, required_skills):
    """
    Compare user skills with required job skills.

    Returns:
        matched skills
        missing skills
        match percentage
    """

    user_set = {skill.lower() for skill in user_skills}
    required_set = {skill.lower() for skill in required_skills}

    matched = user_set.intersection(required_set)
    missing = required_set - user_set

    match_percentage = (
        len(matched) / len(required_set) * 100
        if required_set
        else 0
    )

    return matched, missing, match_percentage