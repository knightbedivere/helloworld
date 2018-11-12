# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

def fnl(l):
    l=l+[4
    

#Question 1
word='aeiou'
new_word=word.replace('a','i')
print(new_word)

#Question 2
def fn2(n):
   for m in range(1,n+1):
       for k in range(1,n+1):
           print(m,"*",k,'=',m*k,sep='')

#Question 3
sentence='this is a long sentenc'
words=sentence.split(' ')

length=[]
for each_item in words:
    length.append(len(each_item))

new_list=list(zip(length,words))
result=sorted(new_list)
print(result)

#Question 4
my_file=open('C:/Users/Katherine/Documents/Computing/question4.txt').read().replace('\n',' ')
my_file_low=my_file.lower()
words=my_file_low.split()
counts=dict()
for each_word in words:
  counts[each_word]=counts.get(each_word,0)+1 
sorted_count=sorted([(number,each_word) for each_word, number in counts.items()],reverse=True)
result=sorted_count[0:5]
print(result)

#Question 5
#a
^\d{4}[-/]\d{2}[-/]\d{2}$
#b
^\d{5}(?:[-]\d{4})?$
#c
^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

#Question 6
import numpy as np
a=np.array([1,2,3,2])
b=np.array([2,2,2,2])
c=a-b
d=np.where(c==0)
print(d)
