import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset_km_miles.csv')
plt.scatter(data['km'], data['miles'])
plt.xlabel('Kilometers')
plt.ylabel('Miles')
plt.title('Kilometers vs Miles')
plt.grid(True)
plt.show()

