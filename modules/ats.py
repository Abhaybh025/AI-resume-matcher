from config.logging_config import get_logger

logger = get_logger(__name__)

import re

def ats_analysis(resume_text, matched_skills, missing_skills):
    """
    Perform ATS analysis on the resume text.

    Args:
        resume_text(str): Cleaned resume text.
        matched_skills(list): List of skills matched in the resume.
        missing_skills(list): List of skills missing in the resume.

    Returns:
        dict: A dictionary containing the analysis results.
    """

    logger.info("Performing ATS analysis")

    try: 
        score = 0
        feedback = []

        # Check email
        email_pattern = r'\S+@\S+'

        if re.search(email_pattern, resume_text):
            score += 10

        else:
            feedback.append("Email not found.")

        # Check Phone
        phone_pattern = r'(\+?\d[\d\s-]{8,}\d)'

        if re.search(phone_pattern, resume_text):
            score += 10
        
        else:
            feedback.append("Phone not found.")

        # Check linkdln 
        if "linkedin" in resume_text.lower():
            score += 5
        
        else:
            feedback.append("Linkdln profile missing.")
        
        # Check github
        if "github" in resume_text.lower():
            score += 5

        else:
            feedback.append("GitHub profile missing.")

        # Section Detection 
        sections = {
            "skills":10,
            "experience":15,
            "education":10,
            "projects":15
        }

        for section, marks in sections.items():
            if section in resume_text.lower():
                score += marks
            
            else:
                feedback.append(f"{section.title()} section missing.")
        
        # Resume Length 
        words = len(resume_text.split())

        if words >= 300:
            score += 5
        
        else:
            feedback.append("Resume is too short.")

        # Action words 
        verbs = [
            "developed", "implemented", "designed", "optimized", "created", "built", "deployed"
        ]
        count = 0
        
        resume_lower = resume_text.lower()

        for verb in verbs:

            if verb in verbs:
                count += 1
        
        if count >= 3:
            score += 5
        
        else:
            feedback.append("Use more action words.")

        # Keyword Coverage
        if len(missing_skills) <= 2:
            score += 10
        
        else:
            feedback.append("Many required keywords are missing.")

        return {
            "ats_score": score,
            "feedback": feedback
        }

    except Exception as e:
        logger.error('Failed to perform ATS analysis')
        raise