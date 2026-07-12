from modules.matcher import analyze_resume
from modules.parser import extract_text_from_pdf, extract_text_from_txt
from modules.cleaner import clean_resume_text
from modules.skill_extractor import load_skills

resume = extract_text_from_pdf("./data/sample_resume.pdf")
resume_text = clean_resume_text(resume)
print("Cleaned Resume Text: ", resume_text)

jd = extract_text_from_txt("./data/jd.txt")
jd_text= clean_resume_text(jd)
print("Cleaned Job Description Text: ", jd_text)

skills_set = load_skills("./data/skills.csv")

result = analyze_resume(resume_text, jd_text, skills_set)
print("Resume Analysis Result:")

for key, value in result.items():
    print(f"{key}: {value}")