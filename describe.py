import sys
import pandas as pd
import ollama

path = sys.argv[1]
df = pd.read_csv(path)

profile = (
    "Rows: " + str(len(df)) + "\n"
    "Columns: " + ", ".join(df.columns) + "\n"
    "Missing values per column:\n" + df.isna().sum().to_string() + "\n"
    "Summary stats:\n" + df.describe().to_string() + "\n"
    "First rows:\n" + df.head().to_string()
)

prompt = (
    "You are a data analyst. Based on this profile of a CSV file, "
    "describe what the data seems to be about, point out data quality "
    "issues, and suggest three questions worth exploring.\n\n" + profile
)

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
)

print(response["message"]["content"])