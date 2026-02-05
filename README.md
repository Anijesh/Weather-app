# Weather Platform 🌤️

A robust Django-based weather application that provides real-time weather updates, 5-day forecasts, and a personalized dashboard for managing favorite cities.

## Features ✨

- **User Authentication**: Secure registration and login system.
- **Real-time Weather**: Get up-to-date weather conditions for any city using the OpenWeatherMap API.
- **5-Day Forecast**: View detailed forecast data including temperature and weather conditions.
- **Favorites Dashboard**: Save your favorite cities for quick access. Click on any favorite city to view its current weather.
- **Responsive Design**: Beautiful, mobile-friendly interface with modern styling.

## Tech Stack 🛠️

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3 (Custom styling), JavaScript
- **Database**: SQLite (Default), Redis (Support enabled)
- **API**: OpenWeatherMap

## Installation & Setup 🚀

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd weather_platform
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   WEATHER_API_KEY=your_openweathermap_api_key
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage 📖

1. **Register/Login**: Create an account to access the dashboard.
2. **Search Weather**: Enter a city name in the search bar to see current weather and forecast.
3. **Save Favorites**: Click "Save to Favorites" to pin a city to your dashboard.
4. **View Favorites**: Click on any pinned city in the dashboard to instantly refresh its weather data.

## License 📄

This project is open-source and available under the [MIT License](LICENSE).
