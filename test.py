import pandas as pd

# Lee el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Muestra las primeras filas
print(car_data.head())
