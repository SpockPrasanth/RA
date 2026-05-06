import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Miracle Recruitment Portal",
    page_icon="📘",
    layout="wide"
)

# =========================================================
# THEME TOGGLE
# =========================================================

theme = st.sidebar.toggle("🌙 Dark Mode", value=False)

if theme:

    background = "#0E1117"
    text = "white"
    card = "#1E1E1E"
    border = "#3A3A3A"

else:

    background = "#F4F5F7"
    text = "#111111"
    card = "white"
    border = "#D9D9D9"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(f"""
<style>

.stApp {{
    background-color: {background};
    color: {text};
}}

.question-card {{
    background-color: {card};
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #0D5EA6;
    margin-bottom: 20px;
    border: 1px solid {border};
}}

.main-title {{
    font-size: 42px;
    font-weight: bold;
    color: #0D5EA6;
}}

.sub-title {{
    font-size: 18px;
    color: gray;
}}

.stButton button {{
    background-color: #0D5EA6;
    color: white;
    border-radius: 6px;
    border: none;
    height: 40px;
}}

.stButton button:hover {{
    background-color: #084B87;
    color: white;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
🚀 Miracle Recruitment Interview Assistant
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Interview Portal for Data Engineers & Power BI Developers
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# QUESTION BANK
# =========================================================

question_bank = {

    "Data Engineer": {

        "SQL": {

            "Fresher": [

                {
                    "question": "What is SQL?",
                    "answer": "SQL is Structured Query Language used to manage relational databases."
                },

                {
                    "question": "What is Primary Key?",
                    "answer": "Primary Key uniquely identifies rows in a table."
                },

                {
                    "question": "Difference between DELETE and TRUNCATE?",
                    "answer": """
DELETE removes rows one by one.

TRUNCATE removes all rows quickly.
"""
                },

                {
                    "question": "What is normalization?",
                    "answer": "Normalization reduces redundancy."
                },

                {
                    "question": "What is JOIN?",
                    "answer": "JOIN combines data from multiple tables."
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
                    "answer": "Loads only changed records."
                },

                {
                    "question": "Difference between UNION and UNION ALL?",
                    "answer": """
UNION removes duplicates.

UNION ALL keeps duplicates.
"""
                },

                {
                    "question": "What is CTE?",
                    "answer": "CTE is Common Table Expression."
                },

                {
                    "question": "What are indexes?",
                    "answer": "Indexes improve query performance."
                }

            ],

            "5-8 Years": [

                {
                    "question": "How do you optimize SQL queries?",
                    "answer": """
Use indexes, partitioning,
optimize joins,
and avoid SELECT *.
"""
                },

                {
                    "question": "Explain table partitioning.",
                    "answer": "Partitioning divides tables into smaller pieces."
                },

                {
                    "question": "Explain execution plans.",
                    "answer": "Execution plans show how query executes."
                },

                {
                    "question": "What is CDC?",
                    "answer": "CDC captures changed data."
                },

                {
                    "question": "Explain SCD Types.",
                    "answer": """
SCD handles historical changes.

SCD1
SCD2
SCD3
"""
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design enterprise ETL frameworks?",
                    "answer": """
Using metadata-driven pipelines,
logging, auditing,
and parameterization.
"""
                },

                {
                    "question": "Explain enterprise CDC handling.",
                    "answer": """
Using timestamps,
logs,
and watermark strategies.
"""
                },

                {
                    "question": "How do you design scalable warehouse architecture?",
                    "answer": """
Using partitioning,
star schema,
aggregations,
and optimized storage.
"""
                },

                {
                    "question": "Explain distributed query processing.",
                    "answer": "Queries execute across multiple nodes."
                },

                {
                    "question": "How do you manage data governance?",
                    "answer": """
Using security,
auditing,
lineage,
and quality checks.
"""
                }

            ]
        },

        "ADF": {

            "Fresher": [

                {
                    "question": "What is Azure Data Factory?",
                    "answer": "ADF is cloud ETL service."
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is Integration Runtime?",
                    "answer": "Integration Runtime is compute infrastructure."
                },

                {
                    "question": "What is Copy Activity?",
                    "answer": "Copy Activity transfers data."
                }

            ],

            "5-8 Years": [

                {
                    "question": "What is parameterization in ADF?",
                    "answer": "Parameterization allows dynamic pipelines."
                },

                {
                    "question": "Explain Mapping Data Flow.",
                    "answer": "Data Flow performs transformations visually."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design enterprise reusable pipelines?",
                    "answer": """
Using metadata-driven architecture
and dynamic frameworks.
"""
                }

            ]
        }
    },

    "Power BI Developer": {

        "DAX": {

            "Fresher": [

                {
                    "question": "What is Measure?",
                    "answer": "Measure performs dynamic calculation."
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is CALCULATE function?",
                    "answer": "CALCULATE modifies filter context."
                },

                {
                    "question": "Difference between SUM and SUMX?",
                    "answer": """
SUM aggregates directly.

SUMX iterates row by row.
"""
                }

            ],

            "5-8 Years": [

                {
                    "question": "Explain context transition.",
                    "answer": "Context transition converts row to filter context."
                },

                {
                    "question": "How do you optimize Power BI reports?",
                    "answer": """
Use star schema,
optimize DAX,
reduce visuals.
"""
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you architect enterprise Power BI solutions?",
                    "answer": """
Using governance,
security,
deployment pipelines,
and semantic models.
"""
                }

            ]
        }
    }
}

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("⚙️ Interview Setup")

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

# =========================================================
# GET QUESTIONS
# =========================================================

questions = question_bank[role][technology][experience]

# =========================================================
# SEARCH
# =========================================================

search = st.text_input(
    "🔍 Search Questions",
    placeholder="Search by keyword..."
)

filtered_questions = [
    q for q in questions
    if search.lower() in q["question"].lower()
]

# =========================================================
# SCORE
# =========================================================

score = 0

# =========================================================
# DISPLAY QUESTIONS
# =========================================================

st.subheader(f"{role} → {technology} → {experience}")

for index, item in enumerate(filtered_questions):

    with st.container():

        st.markdown(
            f"""
            <div class="question-card">

            <h3 style="color:#0D5EA6;">
            Question {index + 1}
            </h3>

            <p style="font-size:18px;">
            {item['question']}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1, 3])

        with col1:

            if st.button(
                f"Show Answer {index}",
                key=f"answer_{index}"
            ):
                st.success(item["answer"])

        with col2:

            correct = st.checkbox(
                "✅ Candidate Answered Correctly",
                key=f"correct_{index}"
            )

            if correct:
                score += 1

# =========================================================
# RESULT
# =========================================================

st.divider()

st.subheader("📊 Candidate Evaluation")

st.metric(
    label="Candidate Score",
    value=f"{score} / {len(filtered_questions)}"
)

if score >= 10:
    st.success("✅ Candidate Selected for Next Round")

elif score >= 5:
    st.warning("⚠️ Candidate Needs Further Evaluation")

else:
    st.error("❌ Candidate Not Selected")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption("Developed for Miracle Software Systems Recruitment Team")
