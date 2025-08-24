from flask import Flask, render_template, request, url_for
import requests
import matplotlib.pyplot as plt
import os
from datetime import date, timedelta
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

# ---------- Utilities ---------- #
def get_coordinates(city):
    """Get coordinates of a city using Open-Meteo geocoding (no key needed)"""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url).json()
    if response.get("results"):
        return (
            response["results"][0]["latitude"],
            response["results"][0]["longitude"],
            response["results"][0]["name"],
        )
    return None, None, None


def get_weather_data(lat, lon):
    """Fetch past week weather (temperature + rainfall)"""
    today = date.today()
    last_week = today - timedelta(days=7)

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={last_week}&end_date={today}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    )
    response = requests.get(url).json()

    if "daily" in response:
        daily = response["daily"]
        temps = []
        rainfall = []
        dates = daily["time"]

        for tmin, tmax, rain in zip(
            daily["temperature_2m_min"], daily["temperature_2m_max"], daily["precipitation_sum"]
        ):
            if tmin is not None and tmax is not None:
                temps.append((tmin + tmax) / 2)  # avg temp
            else:
                temps.append(None)
            rainfall.append(rain)

        return temps, rainfall, dates
    return [], [], []


def save_rainfall_chart(rainfall, dates, cname):
    clean_dates = []
    clean_rainfall = []
    for d, r in zip(dates, rainfall):
        if r is not None:
            clean_dates.append(d)
            clean_rainfall.append(r)

    plt.figure(figsize=(8, 4))
    plt.bar(clean_dates, clean_rainfall, color="skyblue", label="Rainfall")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.title(f"Rainfall Trend - {cname}")
    plt.xticks(rotation=45)
    plt.legend()

    filepath = os.path.join("static", "rainfall.png")
    plt.savefig(filepath)
    plt.close()
    return "rainfall.png"


def save_temperature_chart(temps, dates, cname):
    clean_dates = []
    clean_temps = []
    for d, t in zip(dates, temps):
        if t is not None:
            clean_dates.append(d)
            clean_temps.append(t)

    plt.figure(figsize=(8, 4))
    plt.plot(clean_dates, clean_temps, marker="o", color="tomato", label="Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend - {cname}")
    plt.xticks(rotation=45)
    plt.legend()

    filepath = os.path.join("static", "temperature.png")
    plt.savefig(filepath)
    plt.close()
    return "temperature.png"


def save_city_map(lat, lon, cname):
    """
    Create a temperature heatmap around the searched city.
    Uses OpenWeather API to sample nearby grid points.
    """
    API_KEY = "YOUR_OPENWEATHER_API_KEY"  # <-- put your key here

    m = folium.Map(location=[lat, lon], zoom_start=10)
    heat_data = []

    step = 0.05   # about ~5 km step
    grid_size = 3  # creates (2*grid_size+1)^2 points, here 7x7 = 49 calls

    for i in range(-grid_size, grid_size + 1):
        for j in range(-grid_size, grid_size + 1):
            lat_offset = lat + (i * step)
            lon_offset = lon + (j * step)

            url = (
                f"http://api.openweathermap.org/data/2.5/weather?"
                f"lat={lat_offset}&lon={lon_offset}&appid={API_KEY}&units=metric"
            )
            resp = requests.get(url).json()

            temp = resp.get("main", {}).get("temp")
            if temp is not None:
                heat_data.append([lat_offset, lon_offset, temp])

    if heat_data:
        HeatMap(heat_data, radius=25, blur=15, min_opacity=0.5).add_to(m)

    filepath = os.path.join("static", "city_map.html")
    m.save(filepath)
    return "city_map.html"


# ---------- Routes ---------- #
@app.route("/", methods=["GET", "POST"])
def index():
    temp_chart, rain_chart, city_map = None, None, None
    cname, error_msg = None, None

    if request.method == "POST":
        city = request.form["city"]
        lat, lon, cname = get_coordinates(city)

        if lat and lon:
            temps, rainfall, dates = get_weather_data(lat, lon)

            if temps and rainfall:
                temp_chart = save_temperature_chart(temps, dates, cname)
                rain_chart = save_rainfall_chart(rainfall, dates, cname)
                city_map = save_city_map(lat, lon, cname)
            else:
                error_msg = f"No climate data found for '{city}'."
        else:
            error_msg = f"Could not find coordinates for '{city}'. Try another city."

    return render_template(
        "index.html",
        cname=cname,
        temp_chart=temp_chart,
        rain_chart=rain_chart,
        city_map=city_map,
        error_msg=error_msg,
    )


if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)
