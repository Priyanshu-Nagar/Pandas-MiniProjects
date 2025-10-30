import pandas as pd


def performance_category(gred):
    if gred == "A":
        return "Excellent"
    elif gred == "B":
        return "Good"
    elif gred == "C":
        return "Average"
    else:
        return "Poor" 


data = {
    "name": ["Raj", "Simran", "Aman", "Neha", "Kiran", "Priya", "Ravi", "Tina"],
    "city": ["Delhi", "Mumbai", "Goa", "Delhi", "Goa", "Mumbai", "Delhi", "Goa"],
    "maths": [78, 85, 60, 90, 45, 88, 70, 55],
    "science": [82, 79, 65, 95, 50, 91, 68, 58],
    "english": [75, 88, 58, 80, 65, 85, 72, 60]
}

df = pd.DataFrame(data)

df["average"] = df[["maths", "science", "english"]].mean(axis=1)


df["Grade"] = df["average"].apply(lambda x: "A" if x >= 85 else ("B" if x >= 70 and x < 85 else ("C" if x >= 50 and x < 70 else "D")))

df["city"].replace({"Goa": "Panjim"}, inplace=True)

df["name"].replace({"Mr. ": "", "Ms. ": ""}, regex=True, inplace=True)

df["remarks"] = df["Grade"].apply(performance_category)
print(df)
