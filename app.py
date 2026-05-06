# =====================================================
# ADD THESE QUESTIONS INSIDE question_bank
# =====================================================

# =====================================================
# DATA ENGINEER -> SQL
# =====================================================

"SQL": {

    "Fresher": [

        {
            "question": "What is SQL?",
            "answer": "SQL is Structured Query Language used to manage relational databases."
        },

        {
            "question": "What is the difference between DELETE and TRUNCATE?",
            "answer": """
DELETE removes rows one by one.

TRUNCATE removes all rows quickly.
"""
        },

        {
            "question": "What is a Primary Key?",
            "answer": "Primary Key uniquely identifies rows in a table."
        },

        {
            "question": "What is a Foreign Key?",
            "answer": "Foreign Key creates relationship between tables."
        },

        {
            "question": "What is normalization?",
            "answer": "Normalization reduces redundancy and improves data integrity."
        },

        {
            "question": "Difference between WHERE and HAVING?",
            "answer": """
WHERE filters rows before aggregation.

HAVING filters after aggregation.
"""
        },

        {
            "question": "What are joins?",
            "answer": "Joins combine data from multiple tables."
        },

        {
            "question": "Difference between INNER JOIN and LEFT JOIN?",
            "answer": """
INNER JOIN returns matching records.

LEFT JOIN returns all left table rows and matching right rows.
"""
        },

        {
            "question": "What is GROUP BY?",
            "answer": "GROUP BY groups rows sharing same values."
        },

        {
            "question": "What is ORDER BY?",
            "answer": "ORDER BY sorts query results."
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
            "answer": "Incremental loading loads only changed records."
        },

        {
            "question": "Difference between UNION and UNION ALL?",
            "answer": """
UNION removes duplicates.

UNION ALL keeps duplicates.
"""
        },

        {
            "question": "What is a CTE?",
            "answer": "CTE is Common Table Expression used as temporary result set."
        },

        {
            "question": "What are indexes?",
            "answer": "Indexes improve query performance."
        },

        {
            "question": "What is a stored procedure?",
            "answer": "Stored Procedure is a reusable SQL program."
        },

        {
            "question": "What are views?",
            "answer": "Views are virtual tables created from queries."
        },

        {
            "question": "Explain clustered and non-clustered indexes.",
            "answer": """
Clustered index changes physical storage order.

Non-clustered index creates separate lookup structure.
"""
        },

        {
            "question": "What is denormalization?",
            "answer": "Denormalization improves performance by reducing joins."
        },

        {
            "question": "What is query optimization?",
            "answer": "Query optimization improves SQL execution performance."
        }

    ],

    "5-8 Years": [

        {
            "question": "How do you optimize SQL queries?",
            "answer": """
Use indexes, avoid SELECT *, optimize joins,
partition large tables, and analyze execution plans.
"""
        },

        {
            "question": "Explain table partitioning.",
            "answer": "Partitioning divides large tables into smaller logical pieces."
        },

        {
            "question": "Explain execution plans.",
            "answer": "Execution plans show how SQL engine executes queries."
        },

        {
            "question": "What are materialized views?",
            "answer": "Materialized views physically store query results."
        },

        {
            "question": "Explain deadlocks.",
            "answer": "Deadlocks occur when processes wait indefinitely for resources."
        },

        {
            "question": "How do you handle duplicate records?",
            "answer": """
Using ROW_NUMBER(), DISTINCT,
primary keys, or merge strategies.
"""
        },

        {
            "question": "Explain CDC.",
            "answer": "CDC captures changed data for incremental processing."
        },

        {
            "question": "Difference between OLTP and OLAP?",
            "answer": """
OLTP handles transactional systems.

OLAP handles analytical processing.
"""
        },

        {
            "question": "What are surrogate keys?",
            "answer": "Surrogate keys are system-generated unique identifiers."
        },

        {
            "question": "Explain SCD Types.",
            "answer": """
SCD handles historical dimension changes.

Types:
SCD1
SCD2
SCD3
"""
        }

    ],

    "10+ Years": [

        {
            "question": "How would you design scalable ETL frameworks?",
            "answer": """
Use metadata-driven architecture,
logging, auditing, retry mechanisms,
dynamic pipelines, and parameterization.
"""
        },

        {
            "question": "How do you handle enterprise CDC?",
            "answer": """
Using timestamps, log-based CDC,
watermarks, and streaming frameworks.
"""
        },

        {
            "question": "Explain database sharding.",
            "answer": "Sharding distributes database across multiple servers."
        },

        {
            "question": "How do you design high-performance warehouse?",
            "answer": """
Using partitioning, indexing,
star schema, aggregations,
and optimized storage.
"""
        },

        {
            "question": "Explain distributed query processing.",
            "answer": "Distributed processing executes queries across multiple nodes."
        },

        {
            "question": "How do you manage SQL security?",
            "answer": """
Using RBAC, encryption,
auditing, masking, and access control.
"""
        },

        {
            "question": "How do you tune enterprise ETL jobs?",
            "answer": """
Optimize transformations,
parallelism, partitioning,
and incremental strategies.
"""
        },

        {
            "question": "How do you design disaster recovery for databases?",
            "answer": """
Using backups, replication,
geo-redundancy, and failover strategies.
"""
        },

        {
            "question": "How do you monitor data quality?",
            "answer": """
Using validation frameworks,
audits, reconciliation,
and profiling techniques.
"""
        },

        {
            "question": "Explain enterprise data governance.",
            "answer": """
Data governance ensures
security, quality, lineage,
and compliance.
"""
        }

    ]
}

# =====================================================
# ADD MORE POWER BI QUESTIONS
# =====================================================

"Performance Tuning": {

    "Fresher": [

        {
            "question": "What is Power BI?",
            "answer": "Power BI is a business intelligence and reporting tool."
        }

    ],

    "2-4 Years": [

        {
            "question": "What is Import Mode?",
            "answer": "Import Mode stores data inside Power BI model."
        },

        {
            "question": "What is DirectQuery?",
            "answer": "DirectQuery queries source system directly."
        }

    ],

    "5-8 Years": [

        {
            "question": "How do you optimize DAX queries?",
            "answer": """
Use variables, reduce iterators,
optimize filter context,
and avoid unnecessary calculations.
"""
        },

        {
            "question": "What is VertiPaq engine?",
            "answer": "VertiPaq is Power BI in-memory engine."
        }

    ],

    "10+ Years": [

        {
            "question": "How do you architect enterprise Power BI solutions?",
            "answer": """
Using governance, deployment pipelines,
RLS, semantic models,
and scalable architecture.
"""
        },

        {
            "question": "How do you implement Power BI governance?",
            "answer": """
Using workspace management,
security policies,
certified datasets,
and auditing.
"""
        }

    ]
}
