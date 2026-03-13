import pandas as pd
import os
file_name = 'pandas\\example.csv'

df = pd.read_csv(f'{file_name}')

names = df['name']                         
names_and_salaries = df[['name', 'salary']]              
living_nyc = df.loc[df['city'] == 'New York', ['name', 'department']]  
high_earner = df.loc[df['salary'] > 80000, ['name', 'salary']]  

#print(df.head())    
print(high_earner)