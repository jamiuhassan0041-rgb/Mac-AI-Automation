import sys
import pandas as pd
import ollama

path = sys.argv[1]
df = pd.read_csv(path)

issues = []

dupes = int(df.duplicated().sum())
issues.append("Duplicate rows: " + str(dupes))

missing = df.isna().sum()
for col, count in missing.items():
    if count > 0:
        issues.append("Missing values in " + col + ": " + str(int(count)))

for col in df.select_dtypes("number").columns:
    negatives = int((df[col] < 0).sum())
    if negatives > 0:
        issues.append("Negative values in " + col + ": " + str(negatives))

report = "\n".join(issues)
print("FOUND BY PANDAS:")
print(report)
print()

prompt = (
    "You are a data analyst. These data quality issues were found in a CSV file:\n"
    + report
    + "\n\nExplain in plain English why each matters and how to fix it. Be brief."
)

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
)

print("AI EXPLANATION:")
print(response["message"]["content"])