import numpy as np 
import pandas as pd
import matplotlib

data = pd.read_csv('tips.csv')

name = data['Payer Name']

print(name)
print(type(name))

also_data = np.genfromtxt('tips.csv', delimiter=',', skip_header=1, dtype='str')

print(also_data)


# https://pandas.pydata.org/docs/user_guide/10min.html