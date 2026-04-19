# 🚀 Data Engineering ETL Pipeline (Python)

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python.

The pipeline processes raw sales data, performs data cleaning and transformation, stores the data in a database, and generates business insights.

---

## ⚙️ Pipeline Workflow

### 🔹 Extract

* Reads raw CSV data using Pandas

### 🔹 Transform

* Removes duplicate records
* Handles missing values
* Converts date formats
* Generates aggregated insights (Sales by Category)

### 🔹 Load

* Loads processed data into SQLite database

---

## 📂 Project Structure

```text
data-engineering-etl-pipeline/
├── data/
├── scripts/
├── database/
├── output/
├── main.py
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📊 Output

* Database file → `sales.db`
* Summary file → `sales_summary.csv`
* Log file → `pipeline.log`

---

## 🛠️ Technologies Used

* Python
* Pandas
* SQLite
* Logging

---

## 💡 Key Features

* Modular ETL pipeline design
* Data cleaning and preprocessing
* Logging for monitoring pipeline execution
* Automated data processing workflow

---

## 📈 Future Enhancements

* API-based data extraction
* Scheduling with Airflow
* Cloud deployment (AWS/Azure)

---

## 👨‍💻 Author

Durga Rakesh Sunkara

---
