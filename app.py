import re
import streamlit as st
from utils.resume_parser import extract_resume_text


# Skills to detect
SKILLS = [
    "python",
    "java",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "spring boot",
    "selenium",
    "git",
    "github",
    "machine learning",
    "artificial intelligence",
    "excel",
    "linux",
    "aws",
    "azure"
]


def find_skills(text):
    """
    Find skills mentioned in the given text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters in skill name
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# -----------------------------
# Streamlit App
# -----------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description."
)


# -----------------------------
# Upload Resume
# -----------------------------

resume_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# -----------------------------
# Job Description
# -----------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=200
)


# -----------------------------
# Resume Analysis
# -----------------------------

if resume_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_resume_text(resume_file)


    # Show extracted text
    with st.expander("View Extracted Resume Text"):

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )


    # -----------------------------
    # Analyze Job Description
    # -----------------------------

    if job_description.strip():

        resume_skills = find_skills(resume_text)

        job_skills = find_skills(job_description)


        # Matching skills
        matching_skills = [
            skill
            for skill in job_skills
            if skill in resume_skills
        ]


        # Missing skills
        missing_skills = [
            skill
            for skill in job_skills
            if skill not in resume_skills
        ]


        # -----------------------------
        # Match Percentage
        # -----------------------------

        if job_skills:

            match_percentage = (
                len(matching_skills)
                / len(job_skills)
            ) * 100

        else:

            match_percentage = 0


        # -----------------------------
        # Results
        # -----------------------------

        st.divider()

        st.header("📊 Resume Analysis")


        # Score
        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Match Score",
                f"{match_percentage:.0f}%"
            )


        with col2:

            st.metric(
                "Matching Skills",
                len(matching_skills)
            )


        with col3:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # -----------------------------
        # Matching Skills
        # -----------------------------

        st.subheader("✅ Matching Skills")


        if matching_skills:

            for skill in matching_skills:

                st.write(
                    f"✅ {skill.title()}"
                )

        else:

            st.info(
                "No matching skills found."
            )


        # -----------------------------
        # Missing Skills
        # -----------------------------

        st.subheader("❌ Missing Skills")


        if missing_skills:

            for skill in missing_skills:

                st.write(
                    f"❌ {skill.title()}"
                )

        else:

            st.success(
                "No missing skills found!"
            )


        # -----------------------------
        # Required Skills
        # -----------------------------

        st.subheader("🎯 Skills Found in Job Description")


        if job_skills:

            for skill in job_skills:

                st.write(
                    f"• {skill.title()}"
                )

        else:

            st.info(
                "No predefined skills were detected."
            )


        # -----------------------------
        # Recommendations
        # -----------------------------

        st.subheader("💡 Recommendations")


        if missing_skills:

            st.write(
                "Consider highlighting or learning these "
                "skills if they are relevant to your experience:"
            )

            for skill in missing_skills:

                st.write(
                    f"• {skill.title()}"
                )

        else:

            st.success(
                "Your resume contains all detected "
                "skills from this job description!"
            )
                    # -----------------------------
        # Resume Quality Check
        # -----------------------------

        st.divider()

        st.header("📋 Resume Quality Check")

        resume_text_lower = resume_text.lower()


        # Check important resume sections

        checks = {
            "Contact Information": [
                "@",
                "phone",
                "mobile"
            ],

            "Education": [
                "education",
                "b.tech",
                "bachelor",
                "degree"
            ],

            "Skills": [
                "skills",
                "technical skills"
            ],

            "Projects": [
                "project",
                "projects"
            ],

            "Internship / Experience": [
                "internship",
                "experience",
                "work experience"
            ],

            "Certifications": [
                "certification",
                "certifications",
                "certificate"
            ]
        }


        for section, keywords in checks.items():

            found = False

            for keyword in keywords:

                if keyword in resume_text_lower:

                    found = True
                    break


            if found:

                st.write(
                    f"✅ {section}"
                )

            else:

                st.write(
                    f"⚠️ {section} - Not detected"
                )


        # -----------------------------
        # General Suggestions
        # -----------------------------

        st.subheader("💡 Resume Suggestions")


        suggestions = []


        if "project" not in resume_text_lower:

            suggestions.append(
                "Add a Projects section describing your technical projects."
            )


        if "certification" not in resume_text_lower:

            suggestions.append(
                "Add relevant certifications, courses, or internships if available."
            )


        if "skills" not in resume_text_lower:

            suggestions.append(
                "Add a clearly labelled Technical Skills section."
            )


        if len(resume_text) < 1000:

            suggestions.append(
                "Your resume appears to contain limited text. "
                "Consider adding relevant project or internship details."
            )


        if suggestions:

            for suggestion in suggestions:

                st.write(
                    f"• {suggestion}"
                )

        else:

            st.success(
                "Your resume contains the main sections we checked."
            )