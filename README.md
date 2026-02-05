# 🌤️ Weather Platform

A modern, Django-based weather dashboard that delivers real-time weather updates and 5-day forecasts. Manage your favorite cities with a personalized, responsive interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🚀 Features

- **User Authentication**: Secure signup and login system to protect user data.
- **Live Weather Data**: Real-time temperature, humidity, wind speed, and conditions via OpenWeatherMap API.
- **5-Day Forecast**: Plan ahead with detailed predictive weather data.
- **Smart Dashboard**:
  - Search and view weather for any global city.
  - **Favorites Manager**: Pin cities to your dashboard.
  - **Quick Access**: Click any favorite city to instantly load its latest weather report.
- **Responsive UI**: A polished, mobile-ready interface built with modern CSS and glassmorphism effects.

## 🛠️ Technology Stack

- **Backend**: Python, Django Framework
- **Database**: SQLite (Development), utilizing Redis for caching (optional support included)
- **Frontend**: HTML5, CSS3, JavaScript
- **API Integration**: OpenWeatherMap

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.8 or higher installed
- `pip` package manager

### 1. Clone the Repository

```bash
git clone https://github.com/Start-sys-hub/Weather-app.git
cd weather_platform
```

*(Note: Replace the URL with your actual repository URL if different)*

### 2. Set Up Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Application Configuration

Create a `.env` file in the root directory (`/weather_platform/.env`) to store your secrets.

```env
# Django Settings
DEBUG=True
SECRET_KEY=your_secure_django_secret_key

# External APIs
WEATHER_API_KEY=your_openweathermap_api_key
```

### 5. Database Setup

Apply the migrations to set up your database schema.

```bash
python manage.py migrate
```

### 6. Run the Server

Start the local development server.

```bash
python manage.py runserver
```

Open your browser and navigate to: [http://127.0.0.1:8000/]

## 📖 Usage Guide

1. **Sign Up**: Register a new account to access the dashboard.
2. **Search**: Use the main search bar to look up a city (e.g., "Paris").
3. **Pin Favorites**: When viewing a city's weather, click **"Save to Favorites"**.
4. **Quick Navigation**: Your favorite cities appear as pills on the dashboard. Click them to view their current weather instantly.



