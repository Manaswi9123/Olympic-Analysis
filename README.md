# Olympic-Analysis
# 🏅 120 Years of Olympic History: Interactive Analysis Dashboard

This repository features a comprehensive **Exploratory Data Analysis (EDA)** of the modern Olympic Games, from Athens 1896 to Rio 2016. The project consists of a deep-dive research notebook and a multi-page **Streamlit** web application for real-time data exploration.

---

## 🛠️ The Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Plotly (Interactive), Matplotlib, Seaborn
* **Environment:** PyCharm / Jupyter Notebook

---

## 🧠 Dashboard Modules & Features

### 1. Medal Tally
* Filterable by **Year** and **Country**.
* Provides a consolidated view of Gold, Silver, and Bronze counts across the history of the games.

### 2. Overall Analysis
* **High-level Statistics:** Total editions, host cities, sports, events, athletes, and participating nations.
* **Growth Visualization:** Interactive charts showing the increase in participating nations and events over the decades.
* **Sport-wise Heatmaps:** Visualize the number of events in every sport for every Olympic edition.

### 3. Country-wise Analysis
* **Performance Timeline:** Line charts showing a specific country's medal haul over the years.
* **Sport Excellence:** Heatmaps identifying which sports a specific country excels in.
* **Top Athletes:** A listing of the most successful athletes from a chosen nation.

### 4. Athlete-wise Analysis
* **Age Distribution:** Probability density plots (Distplots) showing the age of medalists across different sports.
* **Height vs. Weight:** Scatter plots showing the physical attributes of athletes, filterable by sport and medal type.
* **Gender Participation:** Visualizing the ratio of male to female athletes over time.

---

## 📂 Project Structure
* `App.py`: The main dashboard script handling the Streamlit UI and navigation.
* `preprocessor.py`: Cleans the raw data (filtering Summer Olympics, handling duplicates, and One-Hot Encoding medals).
* `helper.py`: Contains the complex data manipulation logic for medal tallies, heatmaps, and stats.
* `olympicAnalysis.ipynb`: The primary research notebook used for initial data exploration and algorithm testing.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git](https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git)
