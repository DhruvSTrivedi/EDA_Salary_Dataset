import pandas as pd

# Load the dataset
file_path = "Salary Dataset.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info(), df.head()

import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import numpy as np

# Set plot style
plt.style.use("fivethirtyeight")

# Define figure size
figsize = (10, 6)

# 1️⃣ Salary Distribution – Histogram & KDE plot
plt.figure(figsize=figsize)
sns.histplot(df["Salary"], kde=True, bins=30, color="blue", edgecolor="black", alpha=0.7)
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.grid(True)
plt.show()

# 2️⃣ Box Plot of Salary vs. Employment Status
plt.figure(figsize=figsize)
sns.boxplot(x="Employment Status", y="Salary", data=df, palette="coolwarm")
plt.xlabel("Employment Status")
plt.ylabel("Salary")
plt.title("Salary Distribution by Employment Status")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3️⃣ Top Companies Paying the Highest Salaries (Bar Chart)
top_companies = df.groupby("Company Name")["Salary"].mean().nlargest(10).sort_values()
plt.figure(figsize=figsize)
top_companies.plot(kind="barh", color="darkred", edgecolor="black", alpha=0.8)
plt.xlabel("Average Salary")
plt.ylabel("Company Name")
plt.title("Top Companies Paying the Highest Salaries")
plt.grid(True)
plt.show()

# Top Job Roles & Their Salaries (Horizontal Bar Chart)
top_roles = df.groupby("Job Roles")["Salary"].mean().nlargest(10).sort_values()
plt.figure(figsize=figsize)
top_roles.plot(kind="barh", color="purple", edgecolor="black", alpha=0.8)
plt.xlabel("Average Salary")
plt.ylabel("Job Role")
plt.title("Top Job Roles & Their Salaries")
plt.grid(True)
plt.show()

# 6️⃣ Salary Trends per Job Role & Employment Type (Multi-line Plot)
plt.figure(figsize=(12, 6))
sns.lineplot(x="Job Roles", y="Salary", hue="Employment Status", data=df, marker="o")
plt.xlabel("Job Role")
plt.ylabel("Salary")
plt.title("Salary Trends per Job Role & Employment Type")
plt.xticks(rotation=90)
plt.legend(title="Employment Status")
plt.grid(True)
plt.show()

# 7️⃣ Salary vs. Company Rating (Scatter with Regression Line)
plt.figure(figsize=figsize)
sns.regplot(x="Rating", y="Salary", data=df, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.xlabel("Company Rating")
plt.ylabel("Salary")
plt.title("Salary vs. Company Rating")
plt.grid(True)
plt.show()

# 8️⃣ Salary vs. Job Roles (Violin Plot)
plt.figure(figsize=(12, 6))
sns.violinplot(x="Job Roles", y="Salary", data=df, palette="coolwarm", inner="quartile")
plt.xlabel("Job Role")
plt.ylabel("Salary")
plt.title("Salary Distribution by Job Role")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# 9️⃣ Salary Variance by Job Roles & Employment Status (Heatmap)
pivot_table = df.pivot_table(index="Job Roles", columns="Employment Status", values="Salary", aggfunc="mean")
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)
plt.xlabel("Employment Status")
plt.ylabel("Job Role")
plt.title("Salary Variance by Job Roles & Employment Status")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()

# 🔟 Top 10 Locations with Highest Salaries (Bar Chart)
top_locations = df.groupby("Location")["Salary"].mean().nlargest(10).sort_values()
plt.figure(figsize=figsize)
top_locations.plot(kind="barh", color="darkblue", edgecolor="black", alpha=0.8)
plt.xlabel("Average Salary")
plt.ylabel("Location")
plt.title("Top 10 Locations with Highest Salaries")
plt.grid(True)
plt.show()

# 1️⃣2️⃣ Correlation Heatmap (Understanding relationships)
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Salary Dataset")
plt.show()

# 1️⃣3️⃣ Salary Outliers Analysis (Box Plot with IQR)
plt.figure(figsize=figsize)
sns.boxplot(y=df["Salary"], color="blue")
plt.title("Salary Outliers Analysis")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# 1️⃣4️⃣ Salary Trends per Industry (Grouped Bar Chart) - Adjusted
plt.figure(figsize=(12, 6))
industry_salary = df.groupby("Job Roles")["Salary"].mean().nlargest(10).sort_values()
industry_salary.plot(kind="bar", color="darkgreen", edgecolor="black", alpha=0.8)
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.title("Salary Trends per Industry (Using Job Roles)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 1️⃣5️⃣ Word Cloud of Most Popular Job Titles
from wordcloud import WordCloud

wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="coolwarm").generate(" ".join(df["Job Title"]))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Popular Job Titles")
plt.show()

# 1️⃣6️⃣ Sunburst Chart Alternative – Grouped Bar Chart for Job Roles & Locations
plt.figure(figsize=(12, 6))
role_location_salary = df.groupby(["Job Roles", "Location"])["Salary"].mean().unstack().fillna(0)
role_location_salary.nlargest(10, role_location_salary.columns[0]).plot(kind="bar", stacked=True, figsize=(12, 6))
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.title("Average Salary by Job Roles & Locations")
plt.legend(title="Locations", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 1️⃣7️⃣ Interactive Bubble Chart Alternative – Scatter Plot of Salary vs. Company Rating
plt.figure(figsize=figsize)
sns.scatterplot(x="Rating", y="Salary", size="Salaries Reported", hue="Job Roles", data=df, alpha=0.6, palette="coolwarm", edgecolor="black")
plt.xlabel("Company Rating")
plt.ylabel("Salary")
plt.title("Salary vs. Company Rating")
plt.legend(title="Job Roles", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.show()

# 1️⃣8️⃣ Treemap Alternative – Grouped Bar Chart for Salary Distribution by Job Roles & Companies
plt.figure(figsize=(12, 6))
job_company_salary = df.groupby(["Job Roles", "Company Name"])["Salary"].mean().unstack().fillna(0)
job_company_salary.nlargest(10, job_company_salary.columns[0]).plot(kind="bar", stacked=True, figsize=(12, 6))
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.title("Salary Distribution by Job Role & Company")
plt.legend(title="Companies", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 1️⃣9️⃣ Salary Distribution Histogram by Job Roles
plt.figure(figsize=figsize)
sns.histplot(data=df, x="Salary", hue="Job Roles", bins=30, kde=True, palette="coolwarm", alpha=0.7)
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution Across Job Roles")
plt.grid(True)
plt.show()

# 2️⃣0️⃣ Network Graph Alternative – Bar Chart for Most Common Job Roles
plt.figure(figsize=figsize)
df["Job Roles"].value_counts().nlargest(10).plot(kind="bar", color="purple", edgecolor="black", alpha=0.8)
plt.xlabel("Job Roles")
plt.ylabel("Count")
plt.title("Most Common Job Roles")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
plt.style.use("fivethirtyeight")
figsize = (10, 6)

# 2️⃣1️⃣ Salary Distribution Across Job Roles (Box Plot)
plt.figure(figsize=figsize)
sns.boxplot(x="Job Roles", y="Salary", data=df, palette="coolwarm")
plt.xlabel("Job Roles")
plt.ylabel("Salary")
plt.title("Salary Distribution Across Job Roles")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# 2️⃣2️⃣ Salary Variance by Employment Type (Violin Plot)
plt.figure(figsize=figsize)
sns.violinplot(x="Employment Status", y="Salary", data=df, palette="magma")
plt.xlabel("Employment Status")
plt.ylabel("Salary")
plt.title("Salary Variance by Employment Type")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 2️⃣3️⃣ Salary Trends Over Job Roles (Line Chart)
plt.figure(figsize=figsize)
sns.lineplot(x="Job Roles", y="Salary", data=df, marker="o", color="blue")
plt.xlabel("Job Roles")
plt.ylabel("Salary")
plt.title("Salary Trends Over Job Roles")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# 2️⃣4️⃣ Salary Density Plot
plt.figure(figsize=figsize)
sns.kdeplot(df["Salary"], shade=True, color="red")
plt.xlabel("Salary")
plt.ylabel("Density")
plt.title("Salary Density Plot")
plt.grid(True)
plt.show()

# 2️⃣5️⃣ Salary Breakdown by Job Roles (Stacked Bar Chart)
plt.figure(figsize=(12, 6))
job_role_salary = df.groupby(["Job Roles", "Employment Status"])["Salary"].mean().unstack().fillna(0)
job_role_salary.nlargest(10, job_role_salary.columns[0]).plot(kind="bar", stacked=True, figsize=(12, 6))
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.title("Salary Breakdown by Job Roles & Employment Status")
plt.legend(title="Employment Type", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
