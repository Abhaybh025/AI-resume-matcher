from modules.embeddings import *
from modules.parser import extract_text_from_pdf, extract_text_from_txt
from modules.cleaner import clean_resume_text

resume_text = extract_text_from_pdf("./data/sample_resume.pdf")
resume = clean_resume_text(resume_text)

jd_text = extract_text_from_txt("./data/jd.txt")
jd = clean_resume_text(jd_text)

resume_embedding = generate_embedding(resume)
print("Resume Embedding: ", resume_embedding, "\nShape: ", resume_embedding.shape)

jd_embedding = generate_embedding(jd)
print("Job Description Embedding: ", jd_embedding, "\nShape: ", jd_embedding.shape)

score = semantic_match_score(
    resume_embedding,
    jd_embedding
)

print("Semantic Match Score: ", score)