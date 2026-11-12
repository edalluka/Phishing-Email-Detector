# 🛡️ Phishing Email Detector
A Python-based cybersecurity application designed to identify potential phishing emails through suspicious keyword detection, URL extraction, and risk classification.

The project combines a Python detection engine with an interactive Streamlit dashboard to make email security analysis more accessible and understandable.

### 🚀 Live Demo

[**Open Phishing Email Detector**](https://phishing-email-detector-8xp...streamlit.app/)

### Technologies
- Python
- Streamlit
- Regular Expressions (re)
- Git & GitHub

### Features
- Suspicious keyword detection
- URL extraction
- Risk scoring system
- Phishing risk classification
- Interactive dashboard

## 📌 Project Overview

Phishing is one of the most common cybersecurity threats. Attackers use deceptive emails to trick individuals into revealing sensitive information, clicking malicious links, or accessing fraudulent websites.

**Phishing Email Detector** aims to identify potential phishing indicators in email messages and assign a risk classification based on the results of its analysis.

## ✨ Features

- **Suspicious Keyword Detection:** Identifies potentially dangerous phrases such as "verify your account", "urgent", and "account suspended".
- **URL Extraction:** Detects and extracts HTTP and HTTPS links found in email messages.
- **Risk Scoring:** Assigns points for detected suspicious keywords.
- **Risk Classification:** Categorizes emails into three levels:
  - 🟢 Low Risk
  - 🟡 Suspicious
  - 🔴 Phishing
- **Interactive Dashboard:** Provides a graphical interface for submitting and analyzing email messages.
- **Detection Findings:** Displays the suspicious keywords and URLs identified during analysis.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Regular Expressions (re) | URL extraction and text pattern detection |
| Streamlit | Interactive dashboard development |
| Plotly | Data visualization |
| Git & GitHub | Version control and project management |

## 📂 Project Structure

```text
PhishingEmailDetector/
│
├── app.py              # Streamlit dashboard
├── detector.py         # Email detection engine
├── main.py             # Initial testing script
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/edalluka/Phishing-Email-Detector.git
```

### 2. Navigate to the project directory

```bash
cd Phishing-Email-Detector
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

### 5. Open the dashboard

Open the following address in your browser:

```text
http://localhost:8501
```

## 🔍 How It Works

1. The user enters an email message into the dashboard.
2. The application processes the email using the Python detection engine.
3. Suspicious keywords are identified using predefined patterns.
4. URLs are extracted using regular expressions.
5. A risk score is calculated based on detected keywords.
6. The email receives a risk classification.
7. The dashboard displays the analysis results and detected indicators.

## 📊 Risk Classification

| Risk Score | Classification |
|---|---|
| 0–19 | Low Risk |
| 20–39 | Suspicious |
| 40–100 | Phishing |

Each detected suspicious keyword contributes 10 points to the risk score.

## 🚀 Future Development

The project is actively being developed. Planned improvements include:

- Advanced URL and domain analysis.
- Sender email address verification.
- Email header analysis.
- SPF, DKIM, and DMARC authentication checks.
- Circular risk gauges and interactive threat visualization.
- Scan history and statistical reporting.
- Improved phishing detection techniques.

## ⚠️ Disclaimer

This application is an educational cybersecurity project and currently uses heuristic, keyword-based detection.

A low-risk classification does not guarantee that an email is safe. The current version does not independently verify URLs, domains, sender identities, or email authentication records.

## 👩‍💻 Author
