from modules.cleaner import clean_resume_text
from modules.parser import extract_text_from_pdf, extract_text_from_txt

# resume_text = extract_text_from_pdf(r"data\sample_resume.pdf")

# cleaned_text = clean_resume_text(resume_text)

# print(cleaned_text)

# from modules.cleaner import count_words
# word_count = count_words(cleaned_text)
# print(f"Word Count: {word_count}")

# from modules.cleaner import get_top_n_words
# top_words = get_top_n_words(cleaned_text, n=10)
# print(f"Top Words: {top_words}")

jd = extract_text_from_txt('./data/jd.txt')
jd_text = clean_resume_text(jd)

print("Cleaned jd text:", jd_text)