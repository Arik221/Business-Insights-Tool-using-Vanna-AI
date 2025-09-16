import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
from vanna.remote import VannaDefault

# -----------------------------
# Load Vanna API key
# -----------------------------
load_dotenv()
API_KEY = os.getenv("VANNA_API_KEY")
if not API_KEY:
    raise RuntimeError("VANNA_API_KEY not found in .env file")

# -----------------------------
# Initialize Vanna
# -----------------------------
vn = VannaDefault(model="chinook", api_key=API_KEY)

# -----------------------------
# Setup SQLite DB
# -----------------------------
DB_PATH = "business.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales;")
cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    amount FLOAT,
    date TEXT
);
""")
demo_data = [
    ("Laptop", 1200, "2024-01-10"),
    ("Phone", 800, "2024-01-12"),
    ("Tablet", 600, "2024-01-15"),
    ("Laptop", 1400, "2024-01-20"),
    ("Phone", 900, "2024-01-22"),
]
cursor.executemany("INSERT INTO sales (product, amount, date) VALUES (?, ?, ?);", demo_data)
conn.commit()

engine = create_engine(f"sqlite:///{DB_PATH}")

# -----------------------------
# Train Vanna (optional)
# -----------------------------
try:
    vn.train(ddl="CREATE TABLE sales (id INT, product TEXT, amount FLOAT, date DATE);")
    print("✅ Vanna trained on schema")
except Exception as e:
    print(f"⚠️ Schema training failed (still usable): {e}")

# -----------------------------
# Fallback queries
# -----------------------------
fallbacks = {
    "total sales by product": "SELECT product, SUM(amount) as total_sales FROM sales GROUP BY product;",
    "average laptop sales": "SELECT AVG(amount) as avg_sales FROM sales WHERE product='Laptop';",
    "sales by date": "SELECT date, SUM(amount) as total_sales FROM sales GROUP BY date;"
}

# -----------------------------
# Function to ask question and get results
# -----------------------------
def ask_and_run(question: str):
    try:
        sql = vn.generate_sql(question=question)
    except Exception as e:
        print(f"⚠️ Vanna SQL generation failed: {e}")
        sql = None

    if not sql:
        for key, query in fallbacks.items():
            if key in question.lower():
                sql = query
                print(f"✅ Using fallback SQL: {sql}")
                break

    if not sql:
        print("⚠️ No SQL generated. Skipping.")
        return

    try:
        df = pd.read_sql_query(sql, engine)
        print(f"\n📌 Question: {question}")
        print(f"📝 SQL: {sql}")
        print("📊 Results:")
        print(df)

        # plot numeric column if available
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        if numeric_cols:
            y_col = numeric_cols[0]
            x_candidates = [c for c in df.columns if c != y_col]
            x_col = x_candidates[0] if x_candidates else None
            if x_col:
                df.plot(kind="bar", x=x_col, y=y_col)
            else:
                df[y_col].plot(kind="bar")
            plt.title(question)
            plt.tight_layout()
            plt.show()

    except Exception as e:
        print(f"⚠️ Error executing SQL: {e}")

# -----------------------------
# Interactive loop
# -----------------------------
print("\n💡 Vanna AI Business Insights Generator")
print("Type your question and press Enter. Type 'exit' to quit.")

while True:
    q = input("\n❓ Enter question: ").strip()
    if q.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break
    if q:
        ask_and_run(q)
