
# **Automated Business Insights Generator using Vanna AI**

## **Overview**

The **Automated Business Insights Generator** is an AI-powered tool that translates natural language questions into SQL queries using **Vanna AI**, executes them against a database, and provides business-ready insights with visualizations. It allows non-technical stakeholders to easily query and analyze data without writing SQL.

This project demonstrates the integration of **LLMs for SQL generation**, automated data handling, and real-time interactive visualization.

---

## **Features**

* Converts **natural language questions** into SQL queries using **Vanna AI**.
* Automatically generates **tables and visualizations** from the query results.
* Includes **fallback queries** for reliability if the AI fails to generate SQL.
* Interactive **command-line interface (CLI)** for live querying.
* Fully self-contained with **demo SQLite database** (no CSV required).

---

## **Demo Questions**

* `Show total sales by product`
* `Average laptop sales`
* `Sales by date`
* `Which product has the highest sales?`

---

## **Technologies Used**

* **Python 3.9+** – Main programming language
* **Vanna AI** – Natural language to SQL conversion using LLM
* **SQLite** – Local demo database
* **SQLAlchemy** – Database engine connection
* **Pandas** – Data manipulation and analysis
* **Matplotlib** – Visualization
* **python-dotenv** – Securely load API keys

---

## **Installation & Setup**

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd AutomatedBusinessInsights
```

2. **Create a virtual environment**

```bash
python -m venv venv
# Activate venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

*(or manually install: vanna, python-dotenv, pandas, matplotlib, sqlalchemy)*

4. **Add your Vanna API key** in a `.env` file in the root folder:

```
VANNA_API_KEY=your_actual_vanna_api_key_here
```

5. **Run the project**

```bash
python app.py
```

---

## **Usage**

1. After running `app.py`, type a natural language question and press Enter.

2. The system will:

   * Generate SQL using **Vanna AI**
   * Execute the SQL on the local SQLite database
   * Display a **table of results**
   * Generate a **bar chart** if numeric data is present

3. Type `exit` or `quit` to close the program.

---

## **Project Structure**

```
AutomatedBusinessInsights/
│
├── app.py           # Main application file
├── .env             # Vanna API key
├── business.db      # SQLite database (auto-created)
├── venv/            # Python virtual environment
└── README.md        # This file
```

---

## **How It Works**

1. **Vanna AI Initialization** – Connects to Vanna cloud using your API key.
2. **Schema Training** – Vanna is trained with the SQLite database schema for accurate SQL generation.
3. **Interactive Querying** – Users type questions; Vanna generates SQL.
4. **SQL Execution** – Queries run on local SQLite database.
5. **Results Visualization** – Tables are printed and numeric columns plotted as bar charts.
6. **Fallback Queries** – Predefined SQL used if Vanna cannot generate a query.

---

## **Future Improvements**

* Add support for **multiple tables and joins**.
* Connect to **real business datasets** instead of demo data.
* Improve **visualizations** with interactive dashboards.
* Allow **dynamic CSV uploads** for live queries.

---

## **License**

MIT License – Free to use for personal and educational purposes.

