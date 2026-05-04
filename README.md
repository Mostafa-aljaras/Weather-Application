# Weather Application (Python & PyQt5) 🌦️

## 1. Introduction
[cite_start]This project is a Python-based **Weather Application** built using the **PyQt5** graphical user interface (GUI) library[cite: 3]. [cite_start]The system allows users to enter any city name and receive real-time weather information such as temperature, weather description, and an emoji representing current conditions[cite: 4]. [cite_start]The goal is to provide an easy-to-use interface to check weather data interactively[cite: 5].

## 2. Problem Statement
[cite_start]Many people need quick access to accurate weather information for daily planning[cite: 7]. [cite_start]Manual searches or reading raw JSON data from APIs can be time-consuming and difficult for regular users[cite: 8]. [cite_start]This project solves the problem by providing a clean desktop GUI that retrieves and displays real-time weather conditions instantly using the **OpenWeatherMap API**[cite: 9, 10].

## 3. System Functionality
* [cite_start]**User Input Handling**: Allows users to enter a city name through a text box using `QLineEdit` and `QLabel`[cite: 12, 13, 14].
* [cite_start]**Fetch Weather Data**: Connects to OpenWeatherMap API using the `requests` library to receive JSON responses[cite: 15, 16, 17].
* [cite_start]**Data Processing**: Extracts temperature, descriptions, and condition codes[cite: 18].
* [cite_start]**Temperature Conversion**: Converts Kelvin (API default) to Celsius[cite: 19, 20].
* [cite_start]**Weather Emoji System**: Uses conditional logic (`if/elif`) to match weather codes with descriptive emojis[cite: 24, 25, 26].
* [cite_start]**Error Handling**: Manages HTTP errors like 404 (City not found), 401 (Invalid API Key), and internet connection issues[cite: 27, 28, 29, 32].
* [cite_start]**Professional GUI**: Built with `QVBoxLayout` and styled with custom **CSS** inside `setStyleSheet()`[cite: 34, 35, 37].

## 4. System Flowchart
The following diagram illustrates the application logic:

```text
User Input (City Name) 
       │
       ▼
[Send API Request] ───► OpenWeatherMap Server
       │                        │
       ▼                        ▼
[Receive JSON Data] ◄─── [Weather Data]
       │
       ▼
[Process Data: Convert, Extract, Match Emoji]
       │
       ▼
[Update GUI: Display Temp + Desc + Emoji]