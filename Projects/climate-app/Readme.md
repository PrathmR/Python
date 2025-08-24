Got it 👍
Here’s the **README.md** in plain text (single block):

---

# 🌦 Climate Analysis Dashboard

This project is a **Flask-based Climate Dashboard** that allows users to search for a city and visualize its **climate trends**. It uses free weather APIs to fetch historical data and generates:

* 📈 **Temperature Trend** (past week, with dates and days)
* 🌧 **Rainfall Trend** (past week)
* 🗺 **City Heatmap** (visualizing average temperature intensity across the searched city)

---

## 🚀 Project Flow

1. **User Input**

   * Enter a city name in the search bar.

2. **Data Collection**

   * The app fetches the city’s coordinates using the **Open-Meteo Geocoding API**.
   * Weather data (temperature & rainfall) for the past week is fetched from the **Open-Meteo Archive API**.

3. **Visualization**

   * **Matplotlib** is used to generate **Temperature** and **Rainfall** trend charts.
   * **Folium + HeatMap plugin** is used to generate an **interactive heatmap** for the searched city.

4. **Dashboard Display**

   * The dashboard shows:

     * Temperature graph 📈
     * Rainfall graph 🌧
     * Interactive temperature heatmap 🗺

---

## 🛠️ Tech Stack

* **Backend**: Python (Flask)
* **Frontend**: HTML (Jinja2 Templates), Bootstrap for layout
* **APIs**: Open-Meteo Geocoding + Archive
* **Visualization**: Matplotlib, Folium (Heatmap)

---

## 📂 Project Structure

```
project/
│── app.py  
            # Main Flask app
│── templates/
│    └── index.html     # Dashboard UI
│── static/
│    ├── temperature.png  # Generated temperature chart
│    ├── rainfall.png     # Generated rainfall chart
│    └── maps/
│         └── <city>_map.html  # Generated heatmap for searched city
│── README.md
```

---

## 🏃 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/PrathmR/Python.git
cd climate-dashboard
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in Browser

Visit:

```
http://127.0.0.1:5000/
```

---


