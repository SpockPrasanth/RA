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

dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

if dark_mode:

    background = "#0E1117"
    text = "white"
    card = "#1E1E1E"
    border = "#333333"

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
    border: 1px solid {border};
    margin-bottom: 20px;
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
    border: none;
    border-radius: 6px;
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
                    "answer": "SQL is Structured Query Language used to manage databases."
                },

                {
                    "question": "What is Primary Key?",
                    "answer": "Primary Key uniquely identifies rows in a table."
                },

                {
                    "question": "Difference between DELETE and TRUNCATE?",
                    "answer": "DELETE removes rows one by one. TRUNCATE removes all rows quickly."
                },

                {
                    "question": "What is normalization?",
                    "answer": "Normalization reduces redundancy in databases."
                },

                {
                    "question": "What is JOIN?",
                    "answer": "JOIN combines rows from multiple tables."
                }

            ],

            "2-4 Years": [

                {
                    "question": "Explain Window Functions.",
                    "answer": "Window functions perform calculations across rows."
                },

                {
                    "question": "What is Incremental Loading?",
                    "answer": "Incremental loading loads only changed records."
                },

                {
                    "question": "Difference between UNION and UNION ALL?",
                    "answer": "UNION removes duplicates. UNION ALL keeps duplicates."
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
                    "answer": "Use indexes, partitions, optimized joins, and avoid SELECT *."
                },

                {
                    "question": "Explain table partitioning.",
                    "answer": "Partitioning divides tables into smaller pieces."
                },

                {
                    "question": "Explain execution plans.",
                    "answer": "Execution plans show how queries execute."
                },

                {
                    "question": "What is CDC?",
                    "answer": "CDC captures changed data."
                },

                {
                    "question": "Explain SCD Types.",
                    "answer": "SCD handles historical changes in dimensions."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design enterprise ETL frameworks?",
                    "answer": "Using metadata-driven pipelines, logging, and auditing."
                },

                {
                    "question": "Explain enterprise CDC handling.",
                    "answer": "Using timestamps, logs, and watermark strategies."
                },

                {
                    "question": "How do you design scalable warehouse architecture?",
                    "answer": "Using star schema, partitions, and aggregations."
                },

                {
                    "question": "Explain distributed query processing.",
                    "answer": "Queries execute across multiple nodes."
                },

                {
                    "question": "How do you manage data governance?",
                    "answer": "Using security, lineage, auditing, and policies."
                }

            ]
        },

        "ADF": {

            "Fresher": [

                {
                    "question": "What is Azure Data Factory?",
                    "answer": "ADF is cloud ETL service."
                },

                {
                    "question": "What is pipeline?",
                    "answer": "Pipeline is logical grouping of activities."
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
                },

                {
                    "question": "What are Linked Services?",
                    "answer": "Linked Services connect external systems."
                }

            ],

            "5-8 Years": [

                {
                    "question": "What is parameterization in ADF?",
                    "answer": "Parameterization allows dynamic pipelines."
                },

                {
                    "question": "Explain Mapping Data Flow.",
                    "answer": "Data Flow performs graphical transformations."
                },

                {
                    "question": "How do you optimize ADF pipelines?",
                    "answer": "Use parallelism, partitioning, and incremental loads."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design reusable enterprise pipelines?",
                    "answer": "Using metadata-driven dynamic architecture."
                },

                {
                    "question": "How do you implement enterprise monitoring?",
                    "answer": "Using logging, alerts, dashboards, and auditing."
                }

            ]
        },

        "PySpark": {

            "Fresher": [

                {
                    "question": "What is PySpark?",
                    "answer": "PySpark is Python API for Apache Spark."
                },

                {
                    "question": "What is SparkContext?",
                    "answer": "SparkContext connects application to cluster."
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is lazy evaluation?",
                    "answer": "Transformations execute only during actions."
                },

                {
                    "question": "Difference between transformation and action?",
                    "answer": "Transformation creates dataframe. Action executes job."
                },

                {
                    "question": "What is repartition?",
                    "answer": "Repartition changes partitions with shuffle."
                }

            ],

            "5-8 Years": [

                {
                    "question": "How do you optimize Spark jobs?",
                    "answer": "Use partitioning, cache, and broadcast joins."
                },

                {
                    "question": "Explain Spark DAG.",
                    "answer": "DAG is execution plan for Spark jobs."
                },

                {
                    "question": "What causes data skew?",
                    "answer": "Uneven distribution causes skew."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you tune enterprise Spark workloads?",
                    "answer": "Optimize partitions, shuffle, memory, and serialization."
                },

                {
                    "question": "Explain Catalyst Optimizer.",
                    "answer": "Catalyst Optimizer optimizes Spark SQL queries."
                }

            ]
        },

        "Fabric": {

            "Fresher": [

                {
                    "question": "What is Microsoft Fabric?",
                    "answer": "Fabric is unified analytics platform."
                },

                {
                    "question": "What is OneLake?",
                    "answer": "OneLake is unified storage in Fabric."
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is Lakehouse?",
                    "answer": "Lakehouse combines lake and warehouse."
                },

                {
                    "question": "What is Direct Lake?",
                    "answer": "Direct Lake queries Fabric data directly."
                }

            ],

            "5-8 Years": [

                {
                    "question": "Explain Medallion Architecture.",
                    "answer": "Bronze, Silver, Gold layered architecture."
                },

                {
                    "question": "What are Delta Tables?",
                    "answer": "Delta tables support ACID transactions."
                },

                {
                    "question": "How do you optimize Fabric pipelines?",
                    "answer": "Use partitioning, parallelism, and incremental loads."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you design enterprise Fabric architecture?",
                    "answer": "Using governance, OneLake strategy, and workspace isolation."
                },

                {
                    "question": "How do you implement governance in Fabric?",
                    "answer": "Using RBAC, auditing, Purview, and lineage."
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
                },

                {
                    "question": "What is calculated column?",
                    "answer": "Calculated column stores calculated values."
                }

            ],

            "2-4 Years": [

                {
                    "question": "What is CALCULATE function?",
                    "answer": "CALCULATE modifies filter context."
                },

                {
                    "question": "Difference between SUM and SUMX?",
                    "answer": "SUM aggregates directly. SUMX iterates rows."
                },

                {
                    "question": "What is FILTER function?",
                    "answer": "FILTER returns filtered table."
                }

            ],

            "5-8 Years": [

                {
                    "question": "Explain context transition.",
                    "answer": "Context transition converts row context into filter context."
                },

                {
                    "question": "How do you optimize Power BI reports?",
                    "answer": "Use star schema, optimized DAX, and reduce visuals."
                },

                {
                    "question": "What is time intelligence?",
                    "answer": "Time intelligence performs date-based calculations."
                }

            ],

            "10+ Years": [

                {
                    "question": "How do you architect enterprise Power BI solutions?",
                    "answer": "Using governance, security, deployment pipelines, and semantic models."
                },

                {
                    "question": "How do you implement RLS?",
                    "answer": "Using row-level security filters."
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
# QUESTIONS
# =========================================================

st.subheader(f"{role} → {technology} → {experience}")

for index, item in enumerate(filtered_questions):

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
            f"Show Answer {index + 1}",
            key=f"answer_{index}"
        ):
            st.success(item["answer"])

    with col2:

        correct = st.checkbox(
            "Candidate Answered Correctly",
            key=f"correct_{index}",
            value=False
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

percentage = 0

if len(filtered_questions) > 0:
    percentage = (score / len(filtered_questions)) * 100

st.progress(int(percentage))

st.write(f"### Score Percentage: {round(percentage, 2)}%")

# =========================================================
# FINAL DECISION
# =========================================================

if percentage >= 80:
    st.success("✅ Candidate Selected for Next Round")

elif percentage >= 50:
    st.warning("⚠️ Candidate Needs Further Evaluation")

else:
    st.error("❌ Candidate Not Selected")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption("Developed for Miracle Software Systems Recruitment Team")
