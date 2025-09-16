import sqlite3

# Create and connect to SQLite DB
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

# Create sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    amount FLOAT,
    date TEXT
);
""")

# Insert sample rows
cursor.executemany("""
INSERT INTO sales (product, amount, date)
VALUES (?, ?, ?)
""", [
    ("Laptop", 1200.50, "2023-01-01"),
    ("Phone", 800.00, "2023-01-05"),
    ("Tablet", 450.75, "2023-01-10"),
    ("Laptop", 1350.00, "2023-01-15"),
    ("Phone", 900.25, "2023-02-01")
])

conn.commit()
conn.close()
print("✅ business.db created with sample sales data!")
