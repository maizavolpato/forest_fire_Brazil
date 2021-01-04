#first let's import all necessery libraries for this analysis
import pandas as pd
import numpy as np

#using pandas library and 'read_csv' function to read amazon.csv file
df = pd.read_csv('amazon.csv')

#the columm month is in Portuguese, it's better for a project change to English
#First creat a dictonary with the translate
month_map = {'Janeiro': 'January', 'Fevereiro': 'February', 'Março': 'March', 'Abril': 'April', 'Maio': 'May',
          'Junho': 'June', 'Julho': 'July', 'Agosto': 'August', 'Setembro': 'September', 'Outubro': 'October',
          'Novembro': 'November', 'Dezembro': 'December'}

#use funcion map() to maping our translate months
df['month'] = df['month'].map(month_map)
df.rename(columns = {'year':'Year', 'state': 'State', 'number': 'Number_fire', 'month': 'Month'}, inplace = True)

print("Hello! Let's explore about Brazil's wildfire in the last 20 years.\nFrom 1998 to 2017.".title())


#chekcing how many fires were reported in 20 years
total_fire_year = df.groupby(by = 'Year')['Number_fire'].sum().reset_index()
print("\n Below we have the total wildfire per year:\n")
print(total_fire_year)
total_fire = df['Number_fire'].sum()
print('\nThe total wildfire in Brazil in the last 20 years were {}.'.format(total_fire))
    
#the total number of wildfire per state in 20 years
total_fire_state = df.groupby(by = ['State'])['Number_fire'].sum().sort_values(ascending = False).reset_index()
print("\n Below we have the total wildfire per State in the last 20 years, in descending order:\n")
print(total_fire_state)

#usimg the function descrive to undertand about the wildfire's numbers in 20 years
statistics = df['number'].describe().reset_index().round(3)
print("\nComputing a summary of statistics about the wildfires in Brazil in the last 20 years:")
print(statistics)

#the average of wildfire per state in 20 years
#create two new list one is for state's name and another for fire's numbers
states = list(df.State.unique())

fires_per_state = []
for i in states:
    y = df.loc[df['State']==i].Number_fire.sum().round(3)
    fires_per_state.append(y)

#after using for loop to calculate the mean per state in 20 years
mean_fires_state = []
for n in fires_per_state:
    n /= 20
    mean_fires_state.append(n.round(2))
   

mean_fires_state_dic = dict(zip(states, mean_fires_state))
print("\n The average per state in 20 years are:\n") 

#create a data frame with the dictionary of avarege fires and state
dfmean = pd.DataFrame.from_dict(mean_fires_state_dic, orient='index', columns = ['AVG'])
print(dfmean)


