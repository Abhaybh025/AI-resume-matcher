from modules.parser import extract_text_from_pdf, extract_text_from_txt
from modules.skill_extractor import load_skills, extract_skills, compare_skills
from modules.ats import ats_analysis
from modules.matcher import analyze_resume
from modules.cleaner import clean_resume_text

resume = extract_text_from_pdf("./data/sample_resume.pdf")
print("Extracted resume text:", resume)
resume_text = clean_resume_text(resume)

jd  = extract_text_from_txt("./data/jd.txt")
jd_text= clean_resume_text(jd)

skills_set = load_skills("./data/skills.csv")

extracted_resume_skills = extract_skills(resume, skills_set)
extracted_jd_skills = extract_skills(jd, skills_set)

analysis_result = analyze_resume(resume_text, jd_text, skills_set)

matched_skills = analysis_result["matched_skills"]
missing_skills = analysis_result["missing_skills"]

ats_result = ats_analysis(resume, matched_skills, missing_skills)

from modules.llm_analyzer import generate_llm_feedback
response = generate_llm_feedback(
    resume,
    jd,
    analysis_result,
    ats_result
)

print(response)