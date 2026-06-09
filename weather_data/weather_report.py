import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculating dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Formating dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Getting Dhaka weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=23.81&longitude=90.41&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

# Extracting the daily data
daily_data = data['daily']

# Creating a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})
avrg_temp= df['min_temp'].mean()
print(f'Average temperature is {avrg_temp}')

# Converting date strings to datetime
df['date'] = pd.to_datetime(df['date'])

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Dhaka Weather - Past 7 Days')
plt.legend()

# Rotating x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Saveing the plot
plt.savefig('weather_chart.png')
plt.show()


# Creating data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Saveing to CSV
df.to_csv('data/Dhaka.csv', index=False)
print("Data saved to data/Dhaka.csv")