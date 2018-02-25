#!/bin/bash
#this script records a country with highest life expectancy in 2002 among countries in gapminder.txt
#usage: script.sh
#usage: ./MyFirstScript.sh
input=Data/gapminder.txt
cut -f1,3,4 Data/gapminder.txt | grep 2002 | sort -n -k3 | tail -n 1 > CountryHighestLifeExp.txt