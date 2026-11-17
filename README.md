# Mac AI Automation

Beginner-friendly automation projects built on a MacBook, using Shortcuts, Python, and a free local AI model (Ollama with llama3.2). No API key or paid account needed.

## What's inside

- **describe.py**: Reads a CSV file, builds a profile of the data (rows, columns, missing values, summary stats), and asks a local AI model to describe what the data is about and suggest questions to explore.
- **check.py**: Uses pandas to find data quality issues (duplicate rows, missing values, negative numbers), then asks the AI to explain why each matters and how to fix it.
- **sales.csv**: A small sample dataset with deliberate problems, for testing.

## How to run

1. Install Ollama from ollama.com and run `ollama pull llama3.2`
2. Create a virtual environment: `python3 -m venv myenv`
3. Activate it: `source myenv/bin/activate`
4. Install libraries: `pip install pandas ollama`
5. Run a script: `python3 check.py sales.csv`

## Key idea

Let code do the checking, and let the AI do the explaining. Pandas finds the issues reliably, and the AI turns them into plain English.

## Author

Jamiu Hassan
