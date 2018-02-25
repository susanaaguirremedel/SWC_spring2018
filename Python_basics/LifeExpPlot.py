#This is LifeExPlot.py

# Importing packages
import pandas as pd
import matplotlib.pyplot as plt

#Reading file
my_file = pd.read_table("gapminder.txt")

Canada = my_file.loc[my_file['country']=="Canada", :]

#This is LifeExPlot.pyprint(Canada)

Canada.plot.line(x="year",y="lifeExp", label="Life Expectancy", figsize=(8,6))
plt.suptitle("Life Expectancy in Canada over the years", fontsize=20)
plt.xlabel("Year",fontsize=16)
plt.savefig("PlotlifeExp.png")

