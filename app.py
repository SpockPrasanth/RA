import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Miracle Recruitment Portal",
    page_icon="📘",
    layout="wide"
)

st.title("📘 Miracle Recruitment Interview Assistant")

# =====================================================
# QUESTION BANK WITH EXPERIENCE LEVELS
# =====================================================

question_bank = {

    "Data Engineer": {

        "SQL": {

            "Fresher": [

                {
                    "question": "What is the difference between DELETE and TRUNCATE?",
                    "answer": """
DELETE removes rows one by one.

TRUNCATE removes all rows quickly.
"""
                },

                {
                    "question": "What is a Primary Key?",
                    "answer": """
Primary Key uniquely identifies a row in a table.
"""
                }

            ],

            "2-4 Years": [

                {
                    "question": "Explain Window Functions.",
                    "answer": """
Window functions perform calculations across rows.

Examples:
ROW_NUMBER()
RANK()
LEAD()
LAG()
"""
                },

                {
                    "question": "What is Incremental Loading?",
                    "answer": """
Incremental loading loads only changed or new records.
"""
                }

            ],

            "5-8 Years": [

                {
                    "question": "How do you optimize SQL queries?",
                    "answer": """
Methods:
- Use indexes
- Avoid SELECT *
- Partition tables
- Optimize joins
"""
                },

                {
                    "question": "Explain table partitioning.",
                    "answer": """
Partitioning divides large tables into smaller pieces for performance.
"""
                }

            ],

            "10+ Years": [

                {
                    "question": "How would you design a scalable ETL framework?",
                    "answer": """
Use metadata-driven pipelines, incremental loads,
logging, auditing, retry mechanisms, and parameterization.
"""
                },

                {
                    "question": "Explain handling CDC in enterprise data warehouse.",
                    "answer": """
CDC captures changed records using timestamps,
logs, or change tracking mechanisms.
"""
                }

            ]

        },

        "ADF": {

            "Fresher": [

                {
                    "question": "What is Azure Data Factory?",
                    "answer": """
ADF is a cloud ETL and orchestration service.
"""
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is Integration Runtime?",
                    "answer": """
Integration Runtime is compute infrastructure in ADF.
"""
                }

            ],

            "5-8 Years": [

                {
                    "question": "Explain parameterization in ADF.",
                    "answer": """
Parameterization allows dynamic values in pipelines.
"""
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design reusable enterprise pipelines?",
                    "answer": """
Using metadata-driven frameworks and dynamic pipelines.
"""
                }

            ]
        }
    },

    "Power BI Developer": {

        "DAX": {

            "Fresher": [

                {
                    "question": "What is a Measure?",
                    "answer": """
Measure performs dynamic calculations in Power BI.
"""
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is CALCULATE function?",
                    "answer": """
CALCULATE modifies filter context.
"""
                }

            ],

            "5-8 Years": [

                {
                    "question": "Difference between SUM and SUMX?",
                    "answer": """
SUM directly aggregates.

SUMX iterates row by row.
"""
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you optimize Power BI performance?",
                    "answer": """
Methods:
- Star schema
- Aggregations
- Optimize DAX
- Reduce visuals
"""
                }

            ]
        }
    }
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("Interview Setup")

role = st.sidebar.selectbox(
    "Select Role",
    list(question_bank.keys())
)

technology = st.sidebar.selectbox(
    "Select Technology",
    list(question_bank[role].keys())
)

experience = st.sidebar.selectbox(
    "Experience Level",
    ["Fresher", "2-4 Years", "5-8 Years", "10+ Years"]
)

# =====================================================
# GET QUESTIONS BASED ON EXPERIENCE
# =====================================================

questions = question_bank[role][technology][experience]

# =====================================================
# SEARCH
# =====================================================

search = st.text_input(
    "🔍 Search Questions",
    placeholder="Search by keyword..."
)

filtered_questions = [
    q for q in questions
    if search.lower() in q["question"].lower()
]

# =====================================================
# SCORE TRACKER
# =====================================================

score = 0

st.subheader(f"{role} → {technology} → {experience}")

# =====================================================
# QUESTION DISPLAY
# =====================================================

for index, item in enumerate(filtered_questions):

    with st.expander(f"Question {index + 1}"):

        st.markdown(f"### ❓ {item['question']}")

        if st.button(
            f"Show Answer {index}",
            key=f"answer_{index}"
        ):
            st.success(item['answer'])

        correct = st.checkbox(
            "✅ Candidate Answered Correctly",
            key=f"correct_{index}"
        )

        if correct:
            score += 1

# =====================================================
# FINAL RESULT
# =====================================================

st.divider()

st.subheader("📊 Candidate Evaluation")

st.metric(
    label="Candidate Score",
    value=f"{score} / {len(filtered_questions)}"
)

# =====================================================
# INTERVIEW RESULT
# =====================================================

if score >= 10:
    st.success("✅ Candidate Selected for Next Round")

elif score >= 5:
    st.warning("⚠ Candidate Needs Further Evaluation")

else:
    st.error("❌ Candidate Not Selected")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption("Developed for Miracle Software Systems Recruitment Team")
