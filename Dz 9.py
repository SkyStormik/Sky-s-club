import requests
import sqlite3
from datetime import datetime
def get_temperature():
    city = 'Ternopil'
    url = f'https://weather.com/weather/today/l/{city}'
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    except Exception as e:
        print(f"Помилка при отриманні погоди: {e}")
        return None
def save_to_database(date_time, temperature):
    connection = sqlite3.connect('weather_database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY AUTOINCREMENT, date_time TEXT, temperature REAL)''')
    cursor.execute('INSERT INTO weather (date_time, temperature) VALUES (?, ?)', (date_time, temperature) )
    connection.commit()
    connection.close()
current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
temperature = get_temperature()
if temperature is not None:
    save_to_database(current_date_time, temperature)
    print(f"Дані успішно збережено: {current_date_time}, Температура: {temperature}°C")
else:
    print("Не вдалося отримати дані про погоду.")
