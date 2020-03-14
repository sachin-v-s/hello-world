# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:54:16 2020

@author: Sachin
"""

#program with  for sum of odd numbers in a range
print('program to find sum of even numbers between two numbers')
print('Enter First number')
first=int(input())#assign input value to variable first
print('enter last number')
last=int(input())#assign last number to variable last
if first%2!=0:
    first=first+1#adding a number in case entered term is odd
sum=0
for i in range(first,last+1,2):#setting a common difference of 2 since 2+ any odd number gives next odd number
    sum=sum+i                  #last+1 is used because range function doesnt take last number 
print(sum)    
