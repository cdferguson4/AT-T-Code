import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt


#open the car file
df = pd.read_csv('Car_Detail.csv')
df2 = pd.read_csv('Median_Household_Incomes.csv')
f = open('Car_Detail.csv')
csv_file = csv.reader(f)
#print(df)
header_row = next(csv_file)
'''
#1
#print(df.isnull().sum())



#2 Find median MSRP
med = []
#Iterate and append to a list
for row in csv_file:
    if row[7] == "AUTOMATIC":
        med.append(int(row[16]))

#print(med)
#Print Answer
answer = statistics.median(med)

print(answer)

#3 Engine cylinder of least amount
print(df['Popularity'].min())

#4
print(df['Year'].min() - df['Year'].max()) 

df2 = pd.read_csv('Median_Household_Incomes.csv')
#5
print(df2['Median_CO'].min())

#least = df2['Median_CO' == 52560]
#print(least)

#6
#wheels = df['Driven_Wheels'].value_counts()
#print(wheels)
#print(df['Make'].unique())
print(df.groupby(['Make']),df['Driven_Wheels'].value_counts())
#7
#print(df['MSRP'].max())
#year = df[df['MSRP'].max()]
#print(year)

#8
print(df['Year'].value_counts())
total = df[df["Year"]== 2015, df['Number.of.Doors'] == 2 ,df['Vehicle.Size'] == 'Compact' , df['Vehicle.Style'] == 'Convertable']
print(total)
#9

'''
#Starting over.

#describe datafram
#print(df)
#1 How many columns have NA valuse less than 3742?
#print(df.isnull().sum())

#2 What is the median MSRP of all automatic cars
#print(df.groupby(['Transmission.Type'], as_index= False).median())

#3 What is the engine cylinder of the least most popular car
#print(df.groupby(['Engine.Cylinders'],as_index = False)['Popularity'].min())

#4 How many individual years does the cars data cover
#unique = len(pd.unique(df['Year']))

#print(unique)

#5 What was the year with the lowest median income for Colorado

#print(df2[df2.Median_CO.min() == df2.Median_CO])

#6 Calculate the total number of cars with 
# rear-wheel drive by who makes it. Who is the 5th Largest producer of cars with rear-wheel drive?
'''
print(df.groupby(['Driven_Wheels' == 'rear wheel drive','Make'],as_index = False).count())

new = df.groupby(['Make'])['Driven_Wheels'].agg('count').reset_index()
print(new)
'''

#print(df.groupby(['Make'])['Driven_Wheels'].value_counts(ascending=False).head())

'''rear = df[df['Driven_Wheels'] == 'rear wheel drive']['Make'].count()

print(df.groupby(['Make']))

rear = df.groupby(['Driven_Wheels'])
rear2 = rear.get_group('rear wheel drive')

print(df.groupby(['Make']))
'''
###########################################################
'''list6 = []
for row in csv_file:
    if row[8] == 'rear wheel drive':
        list6.append(row)

fd = pd.DataFrame(list6, columns=['',"Make","Model","Year","Engine.Fuel.Type","Engine.HP","Engine.Cylinders","Transmission.Type","Driven_Wheels","Number.of.Doors","Market.Category","Vehicle.Size","Vehicle.Style","highway.MPG","city.mpg","Popularity","MSRP"])
print(fd)

print(fd.groupby(['Make'])['Driven_Wheels'].value_counts(ascending=True)) 

'''
#########################Mercedes######################################

#7 What year has the highest average MSRP
#print(df.groupby(['Year'])['MSRP'].max())

#8 How many manual, compact , 2-door , convertables were made in 2015
'''print((header_row))
list8 = []
for row in csv_file:
    if row[7] == 'MANUAL':
        if row[11] == 'Compact':
            if row[12] == 'Convertible':
                if row[9] == 2:
                    list8.append[row]
### This answer is 0
print(len(list8))
'''
#9 Largest Decrease of income in 1 year
'''diffCO = df2['Median_CO'].diff().min()
dffNY = df2['Median_NY'].diff().min()
dffCA = df2['Median_CA'].diff().min()
dffTX = df2['Median_TX'].diff().min()
dffIN = df2['Median_IN'].diff().min()

print('Colorado:', diffCO)
print('New York',dffNY)
print('California',dffCA)
print('Texas',dffTX)
print('Indiana',dffIN)

#print(df2.groupby(['DATE'])['Median_CO'].min())
'''

#10 For the state of Texas,
# What is the correlation between the median income by year, and the median car MSRP by year for the years found in both datasets

#correlation = df['MSRP'].corr(df2['Median_TX'])

#print(correlation)

############

dodge = []

for row in csv_file:
    
        if row[1] == "Dodge":
            if row[8] == "rear wheel drive":
                dodge.append(row)

print(len(dodge))


#### Visualize the average MSRP by year

avg  = df.groupby(['Year'],as_index= False)['MSRP'].mean()

avg.plot(x='Year', y='MSRP', legend = False)

plt.show()


## table 1 table 2, id

