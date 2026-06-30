# 🌐 API Documentation

> **InsightFlow AI REST API Design**

---

# 📖 Overview

InsightFlow AI follows a RESTful API architecture built with **Django REST Framework (DRF)**.

The API is designed to be:

- RESTful
- Stateless
- Secure
- JWT Authenticated
- Scalable
- Versioned
- Production Ready

---

# 🏗 API Base URL

```
Development

http://localhost:8000/api/v1/

Production

https://api.insightflow.ai/api/v1/
```

---

# 🔐 Authentication

Authentication Method

```
JWT (JSON Web Token)
```

Headers

```
Authorization: Bearer <access_token>
```

---

# 📂 API Modules

```
Authentication
Users
Projects
Datasets
Data Cleaning
EDA
Machine Learning
Predictions
AI Assistant
Reports
Automation
Dashboard
Notifications
Settings
```

---

# 🔑 Authentication APIs

## Register

```
POST /auth/register/
```

Create a new user account.

---

## Login

```
POST /auth/login/
```

Returns

- Access Token
- Refresh Token

---

## Refresh Token

```
POST /auth/token/refresh/
```

---

## Logout

```
POST /auth/logout/
```

---

## Forgot Password

```
POST /auth/forgot-password/
```

---

## Reset Password

```
POST /auth/reset-password/
```

---

# 👤 User APIs

## Get Profile

```
GET /users/profile/
```

---

## Update Profile

```
PUT /users/profile/
```

---

## Change Password

```
PUT /users/change-password/
```

---

# 📁 Project APIs

## Get Projects

```
GET /projects/
```

---

## Create Project

```
POST /projects/
```

---

## Get Project

```
GET /projects/{id}/
```

---

## Update Project

```
PUT /projects/{id}/
```

---

## Delete Project

```
DELETE /projects/{id}/
```

---

# 📂 Dataset APIs

## Upload Dataset

```
POST /datasets/upload/
```

Supports

- CSV
- XLSX

---

## List Datasets

```
GET /datasets/
```

---

## Dataset Details

```
GET /datasets/{id}/
```

---

## Delete Dataset

```
DELETE /datasets/{id}/
```

---

## Dataset Preview

```
GET /datasets/{id}/preview/
```

---

## Dataset Metadata

```
GET /datasets/{id}/metadata/
```

---

# 🧹 Data Cleaning APIs

## Analyze Dataset

```
POST /cleaning/analyze/
```

---

## Clean Dataset

```
POST /cleaning/process/
```

---

## Cleaning History

```
GET /cleaning/history/
```

---

# 📊 EDA APIs

## Generate Summary

```
POST /eda/summary/
```

---

## Statistics

```
GET /eda/statistics/
```

---

## Correlation Matrix

```
GET /eda/correlation/
```

---

## Charts

```
GET /eda/charts/
```

Returns

- Histogram
- Heatmap
- Scatter Plot
- Box Plot
- Line Chart

---

# 🤖 Machine Learning APIs

## Detect ML Task

```
POST /ml/detect-task/
```

---

## Train Model

```
POST /ml/train/
```

---

## Model Comparison

```
GET /ml/models/
```

---

## Model Details

```
GET /ml/models/{id}/
```

---

## Save Model

```
POST /ml/save/
```

---

## Load Model

```
POST /ml/load/
```

---

# 🔮 Prediction APIs

## Predict

```
POST /prediction/
```

---

## Batch Prediction

```
POST /prediction/batch/
```

---

## Prediction History

```
GET /prediction/history/
```

---

# 🧠 AI Assistant APIs

## AI Chat

```
POST /ai/chat/
```

---

## Dataset Insights

```
POST /ai/insights/
```

---

## Business Recommendations

```
POST /ai/recommendations/
```

---

## Report Summary

```
POST /ai/report-summary/
```

---

# 📄 Report APIs

## Generate Report

```
POST /reports/generate/
```

---

## Download Report

```
GET /reports/{id}/download/
```

---

## Report History

```
GET /reports/
```

---

# 🔄 Automation APIs

## Create Workflow

```
POST /automation/workflows/
```

---

## Execute Workflow

```
POST /automation/run/
```

---

## Workflow Logs

```
GET /automation/logs/
```

---

# 📊 Dashboard APIs

## Dashboard Overview

```
GET /dashboard/
```

Returns

- Projects
- Datasets
- Models
- Reports
- Predictions

---

# 🔔 Notification APIs

## Get Notifications

```
GET /notifications/
```

---

## Mark As Read

```
PUT /notifications/{id}/
```

---

# ⚙ Settings APIs

## User Settings

```
GET /settings/
```

---

## Update Settings

```
PUT /settings/
```

---

# 📦 Standard API Response

Success Response

```json
{
  "success": true,
  "message": "Request completed successfully.",
  "data": {}
}
```

---

Error Response

```json
{
  "success": false,
  "message": "Invalid request.",
  "errors": {}
}
```

---

# 🔒 Security

- JWT Authentication
- Password Hashing
- Secure File Upload
- API Validation
- Permission Classes
- Rate Limiting
- CORS Protection
- HTTPS Only (Production)

---

# 📌 HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# 🚀 Future APIs

- Team Management
- Organization APIs
- Billing APIs
- Subscription APIs
- API Keys
- Webhooks
- AutoML APIs
- Model Registry APIs
- Experiment Tracking APIs

---

# 🏛 API Design Principles

- RESTful Architecture
- Resource-Oriented URLs
- Stateless Communication
- JWT Authentication
- Consistent Response Format
- Versioned Endpoints
- Secure by Default
- Production-Ready Design
- Scalable Architecture
- Clean API Structure