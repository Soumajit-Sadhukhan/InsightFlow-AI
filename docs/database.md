# 🗄️ Database Design

> **InsightFlow AI - Database Documentation**

---

# 📖 Overview

InsightFlow AI follows a relational database architecture using **PostgreSQL**.

The database is designed to support:

- Multi-user SaaS architecture
- Project-based workspaces
- Dataset management
- Machine Learning pipelines
- AI conversations
- Reports
- Workflow automation
- Future scalability

---

# 🏗 Database Architecture

```
User
 │
 ├── Projects
 │      │
 │      ├── Datasets
 │      │      │
 │      │      ├── Data Cleaning
 │      │      ├── EDA Results
 │      │      ├── ML Models
 │      │      ├── Predictions
 │      │      ├── Reports
 │      │      └── AI Chats
 │      │
 │      └── Automation Workflows
 │
 └── User Settings
```

---

# 📌 Database Tables

## 1. Users

Stores account information.

| Field | Type |
|--------|------|
| id | UUID |
| full_name | VARCHAR |
| email | VARCHAR |
| password | HASHED |
| profile_image | TEXT |
| is_verified | BOOLEAN |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 2. Projects

Each user can own multiple projects.

| Field | Type |
|--------|------|
| id | UUID |
| user_id | FK |
| name | VARCHAR |
| description | TEXT |
| task_type | VARCHAR |
| status | VARCHAR |
| created_at | TIMESTAMP |

Task Types

- Regression
- Classification
- Clustering
- Auto Detect

---

## 3. Datasets

Stores uploaded datasets.

| Field | Type |
|--------|------|
| id | UUID |
| project_id | FK |
| file_name | VARCHAR |
| file_size | INTEGER |
| file_type | VARCHAR |
| rows | INTEGER |
| columns | INTEGER |
| uploaded_at | TIMESTAMP |

---

## 4. Dataset Metadata

Automatically generated information.

| Field | Type |
|--------|------|
| id | UUID |
| dataset_id | FK |
| column_names | JSON |
| data_types | JSON |
| missing_values | JSON |
| duplicates | INTEGER |
| target_column | VARCHAR |

---

## 5. Data Cleaning History

Stores every cleaning operation.

| Field | Type |
|--------|------|
| id | UUID |
| dataset_id | FK |
| operation | VARCHAR |
| details | JSON |
| executed_at | TIMESTAMP |

Example Operations

- Missing Value Removal
- Encoding
- Scaling
- Outlier Removal

---

## 6. EDA Results

Stores generated analytics.

| Field | Type |
|--------|------|
| id | UUID |
| dataset_id | FK |
| summary | JSON |
| statistics | JSON |
| correlations | JSON |
| generated_at | TIMESTAMP |

---

## 7. Charts

Stores visualization metadata.

| Field | Type |
|--------|------|
| id | UUID |
| eda_id | FK |
| chart_type | VARCHAR |
| chart_data | JSON |
| created_at | TIMESTAMP |

Supported Charts

- Histogram
- Heatmap
- Scatter Plot
- Line Chart
- Box Plot
- Pie Chart

---

## 8. ML Models

Stores trained machine learning models.

| Field | Type |
|--------|------|
| id | UUID |
| project_id | FK |
| model_name | VARCHAR |
| algorithm | VARCHAR |
| problem_type | VARCHAR |
| accuracy | FLOAT |
| precision | FLOAT |
| recall | FLOAT |
| f1_score | FLOAT |
| model_path | TEXT |
| trained_at | TIMESTAMP |

---

## 9. Predictions

Prediction history.

| Field | Type |
|--------|------|
| id | UUID |
| model_id | FK |
| input_data | JSON |
| prediction | JSON |
| confidence | FLOAT |
| predicted_at | TIMESTAMP |

---

## 10. AI Conversations

Stores AI chat history.

| Field | Type |
|--------|------|
| id | UUID |
| project_id | FK |
| user_message | TEXT |
| ai_response | TEXT |
| model | VARCHAR |
| created_at | TIMESTAMP |

---

## 11. Reports

Generated reports.

| Field | Type |
|--------|------|
| id | UUID |
| project_id | FK |
| report_name | VARCHAR |
| report_type | VARCHAR |
| file_path | TEXT |
| generated_at | TIMESTAMP |

Supported Formats

- PDF
- CSV
- Excel

---

## 12. Automation Workflows

Stores automation configurations.

| Field | Type |
|--------|------|
| id | UUID |
| project_id | FK |
| workflow_name | VARCHAR |
| trigger | VARCHAR |
| status | VARCHAR |
| created_at | TIMESTAMP |

Example Triggers

- Dataset Uploaded
- Training Completed
- Report Generated

---

## 13. Workflow Logs

Execution history.

| Field | Type |
|--------|------|
| id | UUID |
| workflow_id | FK |
| status | VARCHAR |
| started_at | TIMESTAMP |
| completed_at | TIMESTAMP |

---

## 14. Notifications

Stores user notifications.

| Field | Type |
|--------|------|
| id | UUID |
| user_id | FK |
| title | VARCHAR |
| message | TEXT |
| is_read | BOOLEAN |
| created_at | TIMESTAMP |

---

# 🔗 Entity Relationships

```
User
 ├── Projects
 │      ├── Datasets
 │      │      ├── Metadata
 │      │      ├── Cleaning History
 │      │      ├── EDA Results
 │      │      │      └── Charts
 │      │
 │      ├── ML Models
 │      │      └── Predictions
 │      │
 │      ├── Reports
 │      ├── AI Conversations
 │      ├── Automation Workflows
 │      │      └── Workflow Logs
 │      └── Notifications
```

---

# 📈 Database Indexing

Recommended indexes:

- email
- project_id
- dataset_id
- model_id
- created_at
- uploaded_at

---

# 🔒 Security Considerations

- Store hashed passwords only
- Never store API keys in plaintext
- Validate uploaded files
- Enforce foreign key constraints
- Enable cascading deletes where appropriate
- Use UUID as primary keys
- Apply database indexing
- Use transactions for critical operations

---

# 🚀 Future Database Extensions

- Team Members
- Organizations
- API Keys
- Billing
- Subscription Plans
- Audit Logs
- Model Registry
- Model Versioning
- Dataset Versioning
- Experiment Tracking
- Feature Store
- Cloud Storage

---

# 📊 Estimated Database Growth

| Resource | Estimated Size |
|----------|----------------|
| Users | 100K+ |
| Projects | 1M+ |
| Datasets | 5M+ |
| Models | 500K+ |
| Predictions | 20M+ |
| Reports | 2M+ |

---

# ✅ Database Design Principles

- Multi-tenant SaaS architecture
- Normalized relational schema
- Scalable design
- Secure by default
- Modular entities
- Optimized relationships
- ML pipeline support
- AI workflow support
- Automation ready
- Production-ready PostgreSQL architecture