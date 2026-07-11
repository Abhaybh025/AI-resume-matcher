from modules.parser import extract_text_from_pdf, is_resume_empty

resume_text = extract_text_from_pdf(r"data\sample_resume.pdf")

if is_resume_empty(resume_text):
    print("The resume is empty.") 

print(resume_text)