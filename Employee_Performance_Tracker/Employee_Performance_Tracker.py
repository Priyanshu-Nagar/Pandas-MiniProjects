import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
    "department": ["HR", "IT", "IT", "Sales", "HR", "Sales"],
    "experience_years": [3, 7, 2, 5, 10, 4],
    "monthly_sales": [5000, 7000, 3000, 9000, 12000, 6500],
    "customer_rating": [4.2, 4.5, 3.8, 4.7, 4.9, 4.1]
}
df = pd.DataFrame(data)

df["performance_score"] = (df["monthly_sales"]/1000) + (df["customer_rating"]*2) + (df["experience_years"] / 2)

df["grade"] = df["performance_score"].apply(lambda x: "A" if x >= 20 else ("B" if x >= 15 and x < 20 else ("C" if x >= 10 and x < 15 else "D")))

df["department"] = df["department"].replace({"IT": "Tech Department"})

# df["name"] = df["name"].replace({".*[A, a].*": "Anonymous"}, regex=True)
df["name"] = df["name"].replace({r"(?i).*a.*": "Anonymous"})

df["remark"] = df["grade"].apply(lambda x: "Excellent" if x == "A" else ("Good" if x == "B" else ("Average" if x == "C" else "Needs Improvement")))
print(df)
a_b = df[(df["grade"] == "A") | (df["grade"] == "B")]
print(a_b)
df.to_csv("employee_performance_report.csv", index=False)