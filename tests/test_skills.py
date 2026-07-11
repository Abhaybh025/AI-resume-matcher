from modules.skill_extractor import *
from modules.cleaner import clean_resume_text
from modules.parser import extract_text_from_pdf

resume_text = extract_text_from_pdf(r"data\sample_resume.pdf")

cleaned_text = clean_resume_text(resume_text)
# print(type(cleaned_text))

def extract_text_from_txt(file_path = r"data\jd.txt"):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

jd_text = extract_text_from_txt(r'data\jd.txt')

skills_set = load_skills()
# print("Skills Set Loaded:", skills_set)
resume_skills = extract_skills(cleaned_text, skills_set)

print("Extracted resume Skills:", resume_skills)

jd_text = clean_resume_text(jd_text)
# print("Cleaned JD Text:", jd_text)
jd_skills = extract_skills(jd_text, skills_set)

print("JD Skills:", jd_skills)

result = compare_skills(resume_skills, jd_skills)
score = skill_match_score(resume_skills, jd_skills)

print(f"Comparison Result: {result}")
print(f"Skill Match Score: {score:.2f}%")