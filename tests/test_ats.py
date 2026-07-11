from modules.parser import extract_text_from_pdf, extract_text_from_txt
from modules.skill_extractor import load_skills, extract_skills, compare_skills

resume = extract_text_from_pdf("./data/sample_resume.pdf")
print("Extracted resume text:", resume)

jd  = extract_text_from_txt("./data/jd.txt")

skills = load_skills("./data/skills.csv")

extracted_resume_skills = extract_skills(resume, skills)
extracted_jd_skills = extract_skills(jd, skills)

matched_skills = set(extracted_resume_skills) & set(extracted_jd_skills)
missing_skills = set(extracted_resume_skills) - set(extracted_jd_skills)

from modules.ats import ats_analysis

result = ats_analysis(resume, matched_skills, missing_skills)
print(result)