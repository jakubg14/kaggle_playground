import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def remove_unnamed_columns(data_frame):
	for column in data_frame.columns:
		if 'Unnamed' in column:
			del data_frame[column]

data = pd.read_csv('data.csv', encoding='utf-8')

remove_unnamed_columns(data)

data['radius_mean'].plot()

plt.show()
