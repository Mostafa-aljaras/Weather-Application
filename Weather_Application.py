import sys
import requests
import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

load_dotenv()

class Weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.citylabel = QLabel("Enter City Name:", self)
        self.cityinput = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.tempraturelabel = QLabel(self)
        self.emojilabel = QLabel(self)
        self.descriptionlabel = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(600, 200, 700, 700)

        vbox = QVBoxLayout()
        vbox.addWidget(self.citylabel)
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.tempraturelabel)
        vbox.addWidget(self.emojilabel)
        vbox.addWidget(self.descriptionlabel)

        self.setLayout(vbox)

        self.citylabel.setAlignment(Qt.AlignCenter)
        self.cityinput.setAlignment(Qt.AlignCenter)
        self.tempraturelabel.setAlignment(Qt.AlignCenter)
        self.emojilabel.setAlignment(Qt.AlignCenter)
        self.descriptionlabel.setAlignment(Qt.AlignCenter)

        self.citylabel.setObjectName("citylabel")
        self.cityinput.setObjectName("cityinput")
        self.get_weather_button.setObjectName("get_weather_button")
        self.tempraturelabel.setObjectName("tempraturelabel")
        self.emojilabel.setObjectName("emojilabel")
        self.descriptionlabel.setObjectName("descriptionlabel")

        self.setStyleSheet("QLabel, QPushButton{font-family: calibri;}"
                           "QLabel#citylabel{font-size: 50px; font-style: italic; color: white;}"
                           "QLineEdit#cityinput{font-size: 30px; background-color: white;}"
                           "QPushButton#get_weather_button{font-size: 30px; font-weight: bold; color: white; background-color: #1e3c72;}"
                           "QLabel#tempraturelabel{font-size: 70px; color: white;}"
                           "QLabel#emojilabel{font-size: 90px; font-family: Segoe UI Emoji; color: white;}"
                           "QLabel#descriptionlabel{font-size: 50px; color: white;}"
                           "QWidget{background-color: #1a2a6c;}")

        self.get_weather_button.clicked.connect(self.get_weather) 
     
        
    def get_weather(self):
        api_key = os.getenv("WEATHER_API_KEY")
        city = self.cityinput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
              

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nplease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error:\nplease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\n Server is down")
                case 504:
                    self.display_error("Gateway Timeout:\nno response from the server")    
                case _:
                    self.display_error("HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("No internet connection available.")
        except requests.exceptions.Timeout:
            self.display_error("The request timed out.") 
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects.")           
        except requests.exceptions.RequestException as req_error:
            self.display_error("Request Error:\n{req_error}")                                                                                                                          


    def display_error(self, message):
        self.tempraturelabel.setStyleSheet("font-size: 50px;")
        self.tempraturelabel.setText(message)
        self.emojilabel.clear()
        self.descriptionlabel.clear()


    def display_weather(self, data):
        tempreature_k = data["main"]["temp"]
        tempreature_c = tempreature_k - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]
        
        self.tempraturelabel.setText(f"{tempreature_c:.0f}°C")
        self.descriptionlabel.setText(weather_description)
        self.emojilabel.setText(self.weather_emoji(weather_id))


    @staticmethod
    def weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 761:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "🌈"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather = Weatherapp()
    weather.show()
    sys.exit(app.exec_())