import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def remove_unnamed_columns(data_frame):
	for column in data_frame.columns:
		if 'Unnamed' in column:
			del data_frame[column]

def check_missing_vals(column):
	missing_entries = []
	for counter, val in enumerate(column):
		if val is None or val == '' or val == '-':
			missing_entries.append(counter)
	return missing_entries

def find_poor_observation(dataframe):
	errors = []
	for column in list(dataframe):
		errors = errors + check_missing_vals(column)
		if len(errors) > 0:
			print(str(column) + ' has missing value')
	print(str(len(errors)) + ' poor observations were found.')
	return set(errors)
		
data = pd.read_csv('data.csv', encoding='utf-8')

remove_unnamed_columns(data)

errors = find_poor_observation(data)


data['radius_mean'].plot()

plt.show()


