import streamlit as st
from career_data import career_roles


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Career Path Finder",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🎯 AI Career Path Finder")

st.write(
    "Find suitable career roles based on your skills, education, "
    "experience and interests."
)

st.divider()


# -----------------------------
# User Profile
# -----------------------------

st.header("👤 Enter Your Profile")

education = st.text_input(
    "Education",
    placeholder="Example: B.Tech CSE"
)

experience = st.text_input(
    "Experience",
    placeholder="Example: Fresher / Internship"
)

skills_input = st.text_input(
    "Your Skills",
    placeholder="Example: Python, SQL, HTML"
)

interests_input = st.text_input(
    "Your Interests",
    placeholder="Example: Python, Data, Web Development"
)

resume = st.text_area(
    "Paste Your Resume / Additional Information",
    placeholder="Enter your resume details here..."
)


# -----------------------------
# Convert input into list
# -----------------------------

def convert_to_list(text):

    return [
        item.strip().lower()
        for item in text.split(",")
        if item.strip()
    ]


# -----------------------------
# Career Matching Function
# -----------------------------

def calculate_match(user_skills, user_interests, resume_text):

    results = []

    resume_text = resume_text.lower()

    for role, data in career_roles.items():

        role_skills = set(data["skills"])

        role_interests = set(data["interests"])

        user_skill_set = set(user_skills)

        user_interest_set = set(user_interests)

        # Skill matching
        skill_matches = user_skill_set.intersection(role_skills)

        # Interest matching
        interest_matches = user_interest_set.intersection(
            role_interests
        )

        # Resume matching
        resume_matches = []

        for skill in role_skills:

            if skill in resume_text:
                resume_matches.append(skill)

        # Calculate score
        skill_score = len(skill_matches)

        interest_score = len(interest_matches)

        resume_score = len(set(resume_matches))

        total_possible = (
            len(role_skills) +
            len(role_interests) +
            len(role_skills)
        )

        score = (
            skill_score +
            interest_score +
            resume_score
        )

        percentage = int(
            (score / total_possible) * 100
        )

        results.append({
            "role": role,
            "score": percentage,
            "matched_skills": list(skill_matches),
            "matched_interests": list(interest_matches),
            "resume_matches": resume_matches
        })

    # Sort by score
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# -----------------------------
# Find Career Button
# -----------------------------

if st.button("🔍 Find My Career Path"):

    if not skills_input:

        st.warning(
            "Please enter at least your skills."
        )

    else:

        user_skills = convert_to_list(
            skills_input
        )

        user_interests = convert_to_list(
            interests_input
        )

        results = calculate_match(
            user_skills,
            user_interests,
            resume
        )

        st.success(
            "Career analysis completed!"
        )

        st.divider()

        # -----------------------------
        # Career Recommendations
        # -----------------------------

        st.header("🎯 Recommended Career Roles")

        for result in results[:3]:

            st.subheader(
                f"{result['role']} - "
                f"{result['score']}% Match"
            )

            st.progress(
                result["score"] / 100
            )

            if result["matched_skills"]:

                st.write(
                    "**Skills you already have:**"
                )

                st.write(
                    ", ".join(
                        result["matched_skills"]
                    )
                )

            else:

                st.write(
                    "No matching skills found."
                )


        # -----------------------------
        # Selected Career
        # -----------------------------

        st.divider()

        st.header("🚀 Career Roadmap")

        selected_role = st.selectbox(
            "Select a career role",
            [result["role"] for result in results]
        )

        role_data = career_roles[selected_role]

        # -----------------------------
        # Skill Gap
        # -----------------------------

        user_skill_set = set(user_skills)

        required_skills = set(
            role_data["skills"]
        )

        skill_gaps = (
            required_skills -
            user_skill_set
        )

        st.subheader("📌 Skill Gap Analysis")

        if skill_gaps:

            st.write(
                "Skills you need to learn:"
            )

            for skill in skill_gaps:

                st.write(
                    f"🔹 {skill.title()}"
                )

        else:

            st.success(
                "You have all the required skills!"
            )


        # -----------------------------
        # Roadmap
        # -----------------------------

        st.subheader("🗺️ Personalized Learning Roadmap")

        for i, step in enumerate(
            role_data["roadmap"],
            start=1
        ):

            st.write(
                f"**Step {i}:** {step}"
            )


        # -----------------------------
        # Projects
        # -----------------------------

        st.subheader("💻 Recommended Projects")

        for project in role_data["projects"]:

            st.write(
                f"🔹 {project}"
            )


        # -----------------------------
        # Interview Preparation
        # -----------------------------

        st.subheader(
            "🎤 Interview Preparation"
        )

        for topic in role_data["interview"]:

            st.write(
                f"🔹 {topic}"
            )


        # -----------------------------
        # Final Message
        # -----------------------------

        st.divider()

        st.info(
            f"Your recommended career path is based "
            f"on your current profile and selected role: "
            f"**{selected_role}**."
        )