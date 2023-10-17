"""In this project I am going to analyze the overall world happipness
I am going to see if there are trends, what are the most important factors to happiness and 
Is happiness increassing or decreasing over time. I am going to use 
Tablaue to graph those trends and python to analyze the data"""

import numpy as np
import pandas as pd
import datetime
table_1=pd.read_csv('C:\myPythonProjects\world happiness\\2015.csv')
table_2=pd.read_csv('C:\myPythonProjects\world happiness\\2016.csv')
table_3=pd.read_csv('C:\myPythonProjects\world happiness\\2017.csv')
table_4=pd.read_csv('C:\myPythonProjects\world happiness\\2018.csv')
table_5=pd.read_csv('C:\myPythonProjects\world happiness\\2019.csv')

"""We have all of the tables but they are not orginized. 
Lets clean the data and merge all of the tables"""
print(table_1.shape,table_2.shape,table_3.shape,table_4.shape,table_5.shape)

#add the year of each table
table_1['Year']=2015
table_2['Year']=2016
table_3['Year']=2017
table_4['Year']=2018
table_5['Year']=2019

#they are not the same shape, lets merge on the country name but first lets change to column name of 2017 2018 and 2019

table_3=table_3.rename(columns={
"Happiness.Rank":'Happiness Rank'
,"Happiness.Score":'Happiness Score',
'Economy..GDP.per.Capita.':"Economy (GDP per Capita)",
'Health..Life.Expectancy.':'Health (Life Expectancy)',
"Trust..Government.Corruption.":'Trust (Government Corruption)'})

table_4=table_4.rename(columns={
'Country or region':'Country',
 'Overall rank':'Happiness Rank',
 'Score':'Happiness Score',
 'GDP per capita':"Economy (GDP per Capita)",
 "Healthy life expectancy":'Health (Life Expectancy)',
 'Freedom to make life choices':'Freedom',
 'Perceptions of corruption':'Trust (Government Corruption)'})

table_5=table_5.rename(columns={
    'Country or region':'Country',
    'Overall rank':'Happiness Rank',
    'Score':'Happiness Score',
    'GDP per capita':"Economy (GDP per Capita)",
    "Healthy life expectancy":'Health (Life Expectancy)',
    'Freedom to make life choices':'Freedom',
    'Perceptions of corruption':'Trust (Government Corruption)'})

merged=pd.concat([table_1,table_2,table_3,table_4,table_5],join='inner',axis=0)
#lets sort the table to make it more readable

merged=merged.sort_values(['Country','Year'])
print(merged)


#now we have the complete Data frame with all data from 2015-2019

#first lets see what are the greatest contributers to happiness
print(merged.columns)
only_numeric=merged[['Happiness Rank', 'Happiness Score','Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Freedom','Trust (Government Corruption)', 'Generosity']]

print(only_numeric.corr()['Happiness Score'])

"""of course Happiness Rank has the biggest correlation but it does'nt really count
becuase those are intertwined
the next biggest correlations is Economy, Health, Freedom Trust of the govenment and Generosity
generosity has a low correlation so we'll ignore it for now 
Lets look at them side by side in tableau
We'll plot it in Tableau
The Tableau file is also icluded with the code""" 

merged.to_csv('combined.csv')#we export the file so we can use it in Tableau

"""we have the actual correlation plot so we can better visualize the trends of correlation
It is a much better representation than the python Series
we can really look at the data points to understand the data
We can see that Economy has the highert correlation to happiness score
That meakes sense becuse that means countries with higher GDP per capita 
Have less citizens below the poverty line
Thus making their lives more happy"""

"""Now lets look at happiness over the years-
do countries become more or less happy, are there countries that deviate from that standdart?"""

"""I created a dashboard in Tableau. It can be seen clearly
that the overall average per year of happiness score does'nt change much
and that trend is true for most countries
However there are countries that don't follow this trend
those countries are colored and added to the dashboard
Another intersting fact is that on Average 2017 was the least happy year and 2019 was the happiest on average
I also included a map of the countries and the strength of the color tells us how happy it is on average"""

#now lets check weather the top countries kept their spot or not

"""Thats amazing! the top 10 countries stayed the same over those 5 year span
meaning that those countries kept up their lifestyle and kept caring for their citiziens 
We can also see that the top 10 countries tend to be reacher per Capita
Which goes hand and hand with our correlation table
"""


"""Now that we know That Happiness score if most affected by GDP per Capita
Each country should think about it and maybe try to better it's economy
Countries that """

print(merged[merged['Country'].isin(['China','Russia','Afghanistan','Philippines'])])





