# 🤖 AI Anomaly Agent

An AI-powered business analytics project that detects unusual patterns in sales data, monitors revenue and refunds, and generates actionable business insights through an interactive dashboard.

## 📌 Project Overview

The AI Anomaly Agent analyzes business sales data to identify unusual changes in key performance metrics. It combines Machine Learning, data visualization, and automated reporting to help businesses monitor performance and investigate potential issues.

## ✨ Features

- 📊 **Business KPI Monitoring** — Track revenue, orders, costs, and refunds.
- 🤖 **Machine Learning Anomaly Detection** — Use Isolation Forest to identify unusual data patterns.
- 📈 **Interactive Dashboard** — Visualize business performance using Streamlit and Plotly.
- 🚨 **Anomaly Alerts** — Highlight unusual revenue and refund activity.
- 💡 **Business Insights** — Generate summaries to support business analysis.
- 📧 **Email Notifications** — Send anomaly-related alerts through email.
- 🧪 **Sample Data Generation** — Generate sample sales data for testing.

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Plotly
- Streamlit
- OpenPyXL

## 📂 Project Structure

```text
AI-Anomaly-Agent/
│
├── main.py
├── dashboard.py
├── generate_data.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── sales_data.xlsx  # Generated locally; optional
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Anomaly-Agent.git
cd AI-Anomaly-Agent
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Generate sample data

```bash
python generate_data.py
```

If your generator creates `sales_data.xlsx`, keep it in the project folder.

### 5. Launch the interactive dashboard

```bash
python -m streamlit run dashboard.py
```

Streamlit will provide a local URL that you can open in your browser.

### 6. Run the anomaly analysis

```bash
python main.py
```

## 🧠 How It Works

1. **Data Generation:** Create or load sample business sales data.
2. **Data Processing:** Prepare revenue, order, cost, and refund metrics.
3. **Anomaly Detection:** Apply the Isolation Forest algorithm to flag unusual records.
4. **Visualization:** Display KPIs and trends in an interactive dashboard.
5. **Business Reporting:** Summarize detected patterns for further investigation.
6. **Email Alerts:** Notify the intended recipient when configured anomaly alerts are generated.

## 📊 Dashboard Preview

Add a screenshot of your Streamlit dashboard here after running the project.

Example:

`![AI Anomaly Agent Dashboard](screenshots/dashboard.png)`

## 🔐 Security Notes

- Never commit passwords, API keys, email credentials, or `.env` files.
- Do not upload private or confidential business datasets.
- Keep your `.venv/` folder out of version control.
- Use environment variables for email credentials.

## ⚠️ Limitations

Anomalies indicate unusual patterns and do not automatically prove that a business problem exists. Results should be reviewed before taking action.

## 🚀 Future Improvements

- Add more advanced anomaly detection algorithms.
- Include configurable alert thresholds.
- Add interactive date and metric filters.
- Deploy the dashboard online.
- Improve automated business insight generation.

## 👨‍💻 Author

**YOUR NAME**

Aspiring Data Analyst / Data Science professional interested in Machine Learning, Python, and business analytics.

---

⭐ If you find this project interesting, consider starring the repository!
