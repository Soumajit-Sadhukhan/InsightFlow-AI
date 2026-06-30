# 🎨 UI Wireframe Documentation

> **InsightFlow AI - User Interface Architecture**

---

# 📖 Overview

This document defines the UI structure, navigation flow, screen hierarchy, and user experience (UX) of InsightFlow AI.

The interface follows modern SaaS design principles inspired by Apple, Vercel, Linear, and Notion with a clean, minimal, and responsive layout.

---

# 🎯 Design Principles

* Minimal UI
* Clean Layout
* Responsive Design
* Mobile First
* Dark Mode First
* Accessible Components
* Fast Navigation
* Consistent Spacing
* Modern Typography
* Reusable Components

---

# 🌍 Application Structure

```text
Landing Page
      │
      ▼
Authentication
      │
      ▼
Dashboard
      │
      ▼
Project Workspace
      │
      ├── Dataset
      ├── Data Cleaning
      ├── EDA
      ├── Machine Learning
      ├── Prediction
      ├── AI Assistant
      ├── Reports
      └── Settings
```

---

# 🏠 Landing Page

```
-------------------------------------------------------
 Navbar
-------------------------------------------------------

Logo

Features

Solutions

Pricing

Documentation

GitHub

Login

Get Started

-------------------------------------------------------

Hero Section

Headline

Subheadline

CTA Buttons

Dashboard Preview

-------------------------------------------------------

Feature Cards

-------------------------------------------------------

Workflow

-------------------------------------------------------

Statistics

-------------------------------------------------------

Dashboard Preview

-------------------------------------------------------

Testimonials

-------------------------------------------------------

Pricing

-------------------------------------------------------

FAQ

-------------------------------------------------------

Footer
```

---

# 🔐 Authentication

## Login Page

```
+--------------------------------------+

Logo

Welcome Back

Email

Password

Remember Me

Forgot Password

Login Button

Google Login

GitHub Login

Register Link

+--------------------------------------+
```

---

## Register Page

```
Full Name

Email

Password

Confirm Password

Create Account
```

---

# 📊 Dashboard

```
---------------------------------------------------

Sidebar

Top Navbar

---------------------------------------------------

Recent Projects

Quick Statistics

Recent Activity

Recent Reports

Recent Predictions

Recent AI Chats

---------------------------------------------------
```

---

# 📁 Project Workspace

```
-----------------------------------------------------

Sidebar

Project Header

-----------------------------------------------------

Overview

Dataset

Cleaning

EDA

ML Models

Prediction

AI Chat

Reports

Settings

-----------------------------------------------------
```

---

# 📂 Dataset Page

```
---------------------------------------------------

Upload Dataset

Dataset Table

Dataset Information

Preview

Columns

Rows

Data Types

Missing Values

Duplicates

---------------------------------------------------
```

---

# 🧹 Data Cleaning

```
---------------------------------------------------

Cleaning Options

Missing Values

Outliers

Encoding

Scaling

Normalize

Preview

Run Cleaning

---------------------------------------------------
```

---

# 📈 Exploratory Data Analysis

```
---------------------------------------------------

Statistics Cards

Charts Grid

Correlation Matrix

Distribution Charts

Summary

---------------------------------------------------
```

---

# 🤖 Machine Learning

```
---------------------------------------------------

Target Selection

Problem Type

Algorithm Selection

Training Configuration

Train Button

Progress

Evaluation Metrics

Best Model

---------------------------------------------------
```

---

# 🔮 Prediction

```
---------------------------------------------------

Model Selection

Input Form

Predict Button

Prediction Result

Confidence Score

Prediction History

---------------------------------------------------
```

---

# 🧠 AI Assistant

```
---------------------------------------------------

Conversation Panel

Dataset Context

Prompt Input

Suggested Questions

AI Response

Export Conversation

---------------------------------------------------
```

---

# 📄 Reports

```
---------------------------------------------------

Generate Report

PDF

CSV

Excel

Download

History

---------------------------------------------------
```

---

# ⚙ Settings

```
---------------------------------------------------

Profile

Password

Notifications

Appearance

API Keys

Danger Zone

---------------------------------------------------
```

---

# 🧭 Navigation Structure

```
Landing

↓

Authentication

↓

Dashboard

↓

Project Workspace

↓

Dataset

↓

Cleaning

↓

EDA

↓

ML

↓

Prediction

↓

AI Chat

↓

Reports

↓

Settings
```

---

# 🎨 Color System

| Purpose        | Color   |
| -------------- | ------- |
| Primary        | #2563EB |
| Secondary      | #06B6D4 |
| Accent         | #7C3AED |
| Success        | #10B981 |
| Background     | #0B1220 |
| Surface        | #111827 |
| Card           | #1F2937 |
| Text           | #FFFFFF |
| Secondary Text | #94A3B8 |

---

# 🔤 Typography

* Font: Inter
* Headings: Bold
* Body: Medium
* Large spacing
* Rounded UI
* Soft shadows

---

# 📱 Responsive Breakpoints

| Device        | Width          |
| ------------- | -------------- |
| Mobile        | < 640px        |
| Tablet        | 640px – 1024px |
| Desktop       | > 1024px       |
| Large Desktop | > 1440px       |

---

# 🧩 Reusable Components

* Navbar
* Sidebar
* Card
* Modal
* Button
* Badge
* Table
* Chart Container
* File Upload
* KPI Card
* Search Bar
* Notification Toast
* Pagination
* Breadcrumb
* Loader
* Empty State

---

# ✨ Animations

* Fade In
* Slide Up
* Hover Elevation
* Floating Cards
* Loading Skeletons
* Smooth Page Transition

---

# 📌 User Experience Goals

* Simple navigation
* Maximum 3 clicks to reach any feature
* Consistent layout across pages
* Fast page load
* Clear visual hierarchy
* Mobile-friendly design
* Accessible interface
* Professional SaaS appearance

---

# 🏛 UI Architecture Summary

```
Landing Page
      │
      ▼
Authentication
      │
      ▼
Dashboard
      │
      ▼
Project Workspace
      │
      ├── Dataset Management
      ├── Data Cleaning
      ├── EDA Dashboard
      ├── ML Training
      ├── Prediction
      ├── AI Assistant
      ├── Reports
      └── Settings
```

---

# 🎯 Design Goal

Build a modern enterprise-grade AI SaaS platform with an intuitive user experience, scalable component architecture, and production-ready interface suitable for data scientists, machine learning engineers, analysts, startups, and enterprise users.
