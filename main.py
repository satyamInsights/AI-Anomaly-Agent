import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

if EMAIL_ADDRESS and EMAIL_APP_PASSWORD:
    print("Gmail credentials loaded successfully!")
else:
    print("Email credentials missing. Check your .env file.")

from sklearn.ensemble import IsolationForest

import pandas as pd
# read excel file
df = pd.read_excel("sales_data.xlsx")
#display first 5 rows
print("OUR SALES DATA:")
print(df.head())
#Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)
#check missing values
print("\Missing values:")
print(df.isnull().sum())
# calculated average revenue
average_revenue = df["Revenue"].mean()
# Calculated average refunds
average_refunds = df["Refunds"].mean()

print("\nAVERAGE REVENUE:", round(average_revenue,2))
print("AVERAGE REFUNDS:",round(average_refunds,2))

#find ususally low revenue 
low_revenue = df[df["Revenue"] < average_revenue *80]
# find usually high refunds
high_refunds = df[df["Refunds"] > average_refunds *1.50]

print("\nANOMALY REPORT")

if not low_revenue.empty:
    print("\nWARING: Unsually low revenue detected!")
    print(low_revenue[["Date","Revenue"]])
else:
    print("\nNO unsually low revenue detected.") 

if not high_refunds.empty:
    print("\nWARNING: Unusually high refunds detected!") 
    print(high_refunds[["Date","Refunds"]])
else:
    print("\nNO unsually high refunds detected.") 
    
print("\n"+"="*45)
print(" BUSINESS INSIGHT REPORT")
print("="*45)

#Revenue Insights
if not low_revenue.empty:
    for _, row in low_revenue.iterrows():
        percentage_drop = (
            (average_revenue-row["Revenue"]) / average_revenue
        ) *100
        print(f"\nDate:{row['Date'].date()}")
        print(f"Issue:Revenue is unusually low.")
        print(f"Revenue : {row['Revenue']}")
        print(f"Average Revenue:{average_revenue: .2f}")
        print(f"Drop from average: {percentage_drop:.1f}%")
        print(
            "Buisness Action :Check orders,traffic and possible sales issues."
        )
#Refund insights
if not high_refunds.empty:
    for _, row in  high_refunds.iterrows():
        print(f"\nDate: {row['Date'].date()}")
        print("Issue:Refunds are unusually high.")
        print(f"Refunds:{row['Refunds']}")
        print("Average Refunds:{average_refunds:.2f}")
        print("Buisness Action : Review refund reasons and recent customer complaints.")
if low_revenue.empty and high_refunds.empty:
    print("\nNo anomalies detected in the selection metrices.")
print("\nReport complete.")             
  
# Save anomalies to a CSV report 
reports=[]
for _,row in low_revenue.iterrows():
    percentage_drop=(
            (average_revenue-row["Revenue"]) / average_revenue
        ) *100
    
    reports.append({
        "Date":"Revenue",
        "Actual value":row["Revenue"],
        "Normal Average":round(average_revenue,2),
        "Change Percent":round(-percentage_drop,2),
        "Status":"Low Revenue",
        "Suggested Action":"Revision sales and traffic"
    })
for _, row in high_refunds.iterrows():
    
    percentage_change =(
        (row["Refunds"]-average_refunds)/average_refunds
    ) *100 if average_refunds!=0 else 0
    reports.append({
        "Data":row["Data"],
        "Metric":"Refunds",
        "Actual Value":row["Refunds"],
        "Normal Average":round(average_refunds,2),
        "Change Percent": round(percentage_change,2),
        "Status":"High Refunds",
        "Suggested Action": "Review refund reasons"
    })  
report_df=pd.DataFrame(reports)
report_df.to_csv("anomaly_report.csv",index=False)
print("\nAnomaly report saved successfully!")
print("File:anomaly_report.csv")        
              
# visualize business metrics
import matplotlib.pyplot as plt
# sort data by date
df=df.sort_values("Date")
#create two charts    


# Identify ML anomalies
features = ["Revenue", "Orders", "Cost", "Refunds"]

ml_data = df[features].copy()

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["ML_Anomaly"] = model.fit_predict(ml_data)

df["ML_Anomaly"] = df["ML_Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# 2. Store ML anomaly rows
ml_anomalies = df[df["ML_Anomaly"] == "Anomaly"]

# 3. Create dashboard
# ---------- CREATIVE AI ANOMALY DASHBOARD ----------

import matplotlib.pyplot as plt
import pandas as pd

# Safety: prevent NameError if ML anomalies were not created
if "ml_anomalies" not in locals():
    ml_anomalies = df.iloc[0:0].copy()

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(
    "AI ANOMALY DETECTION | BUSINESS INTELLIGENCE",
    fontsize=18,
    fontweight="bold"
)

# KPI calculations
total_revenue = df["Revenue"].sum()
avg_revenue = df["Revenue"].mean()
total_refunds = df["Refunds"].sum()
anomaly_count = len(ml_anomalies)

# KPI cards across the top
fig.text(0.13, 0.91, f"Total Revenue\n{total_revenue:,.0f}",
         ha="center", fontsize=12, fontweight="bold")

fig.text(0.38, 0.91, f"Average Revenue\n{avg_revenue:,.0f}",
         ha="center", fontsize=12, fontweight="bold")

fig.text(0.63, 0.91, f"Total Refunds\n{total_refunds:,.0f}",
         ha="center", fontsize=12, fontweight="bold")

fig.text(0.87, 0.91, f"ML Anomalies\n{anomaly_count}",
         ha="center", fontsize=12, fontweight="bold")


# 1. REVENUE MONITORING
axes[0, 0].plot(
    df["Date"], df["Revenue"],
    marker="o", label="Daily Revenue"
)

axes[0, 0].axhline(
    average_revenue,
    linestyle="--",
    label="Average Revenue"
)

axes[0, 0].scatter(
    low_revenue["Date"],
    low_revenue["Revenue"],
    color="red", s=100,
    label="Low Revenue"
)

axes[0, 0].scatter(
    ml_anomalies["Date"],
    ml_anomalies["Revenue"],
    color="purple", marker="x", s=120,
    label="ML Anomaly"
)

axes[0, 0].set_title("Revenue Anomaly Detection")
axes[0, 0].set_ylabel("Revenue")
axes[0, 0].legend(fontsize=8)
axes[0, 0].grid(True, alpha=0.3)


# 2. REFUNDS MONITORING
axes[0, 1].plot(
    df["Date"], df["Refunds"],
    marker="o", label="Daily Refunds"
)

axes[0, 1].axhline(
    average_refunds,
    linestyle="--",
    label="Average Refunds"
)

axes[0, 1].scatter(
    high_refunds["Date"],
    high_refunds["Refunds"],
    color="red", s=100,
    label="High Refunds"
)

axes[0, 1].scatter(
    ml_anomalies["Date"],
    ml_anomalies["Refunds"],
    color="purple", marker="x", s=120,
    label="ML Anomaly"
)

axes[0, 1].set_title("Refund Anomaly Detection")
axes[0, 1].set_ylabel("Refunds")
axes[0, 1].legend(fontsize=8)
axes[0, 1].grid(True, alpha=0.3)


# 3. DAILY ORDERS
axes[1, 0].bar(
    df["Date"], df["Orders"],
    label="Daily Orders"
)

axes[1, 0].set_title("Order Performance")
axes[1, 0].set_ylabel("Orders")
axes[1, 0].legend(fontsize=8)
axes[1, 0].grid(True, axis="y", alpha=0.3)


# 4. DAILY COST
axes[1, 1].plot(
    df["Date"], df["Cost"],
    marker="o", label="Daily Cost"
)

axes[1, 1].set_title("Cost Monitoring")
axes[1, 1].set_ylabel("Cost")
axes[1, 1].legend(fontsize=8)
axes[1, 1].grid(True, alpha=0.3)


# Improve layout and save dashboard
for ax in axes.flat:
    ax.tick_params(axis="x", rotation=35)

fig.tight_layout(rect=[0, 0, 1, 0.86])

plt.savefig(
    "anomaly_dashboard.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()

print("Creative AI dashboard saved as anomaly_dashboard.png")
print(f"Total ML anomalies detected: {anomaly_count}")

# Prepare email alert messages

print("\nEMAIL ALERT SUMMARY")

if not low_revenue.empty or not high_refunds.empty:
    print("Anomalies detected!")
    print("Email alert is required.")
    
    if not low_revenue.empty:
        print("Alert:unusually lowrefunds detected.")
    if not high_refunds.empty:
        print("Alert:Unusually high refunds detected.")    
else:
    print("No anomalies detected.")
    print("Noemail alert required.")   
    
    



# Step 12 Machine Learning Anomaly Detection

features = ["Revenue", "Orders", "Cost", "Refunds"]

ml_data = df[features].copy()

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["ML_Anomaly"] = model.fit_predict(ml_data)

df["ML_Anomaly"] = df["ML_Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

print("\nMachine Learning Anomaly Results:")
print(df[["Date", "Revenue", "Orders", "Cost", "Refunds", "ML_Anomaly"]])

print("\nAnomalies detected:")
print(df[df["ML_Anomaly"] == "Anomaly"])

# Save Machine Learning Anomaly Report

ml_anomalies = df[df["ML_Anomaly"] == "Anomaly"]

ml_anomalies.to_csv("ml_anomaly_report.csv", index=False)

print("\nML Anomaly Report saved successfully!")
print("Total ML anomalies detected:", len(ml_anomalies))
print("Report file: ml_anomaly_report.csv")


# Step 13: Send anomaly details through Gmail

import smtplib
from email.message import EmailMessage


def send_anomaly_email():
    
    if low_revenue.empty and high_refunds.empty and (df["ML_Anomaly"] != "Anomaly").all():

        print("No anomalies detected. No email sent.")
        return

    msg = EmailMessage()
    msg["Subject"] = "AI Anomaly Agent - Anomaly Alert"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    
ml_anomalies = df[df["ML_Anomaly"] == "Anomaly"]

message = [
    "AI Anomaly Agent detected unusual business activity.\n",
    f"Total ML anomalies detected: {len(ml_anomalies)}\n",
    f"Total low revenue alerts: {len(low_revenue)}\n",
    f"Total high refund alerts: {len(high_refunds)}\n",
    "\nPlease review the following details.\n"
]


for _, row in low_revenue.iterrows():
        message.append(
            f"LOW REVENUE ALERT\n"
            f"Date: {row['Date']}\n"
            f"Revenue: {row['Revenue']}\n"
            f"Average Revenue: {average_revenue:.2f}\n"
            f"Suggested action: Review sales and traffic.\n"
        )

for _, row in high_refunds.iterrows():
        message.append(
            f"HIGH REFUNDS ALERT\n"
            f"Date: {row['Date']}\n"
            f"Refunds: {row['Refunds']}\n"
            f"Average Refunds: {average_refunds:.2f}\n"
            f"Suggested action: Review refund reasons.\n"
        )
        
        
for _, row in df[df["ML_Anomaly"] == "Anomaly"].iterrows():
        message.append(
            f"MACHINE LEARNING ANOMALY ALERT\n"
            f"Date: {row['Date']}\n"
            f"Revenue: {row['Revenue']}\n"
            f"Orders: {row['Orders']}\n"
            f"Cost: {row['Cost']}\n"
            f"Refunds: {row['Refunds']}\n"
            f"Suggested action: Investigate unusual business activity.\n"
        )

msg = EmailMessage()
msg["Subject"] = "AI Anomaly Agent - Anomaly Alert"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg.set_content("\n".join(message))

try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
            server.send_message(msg)

        print("Anomaly alert email sent successfully!")

except Exception as e:
        print("Email sending failed.")
        print("Error:", e)


send_anomaly_email()

    
    
                      