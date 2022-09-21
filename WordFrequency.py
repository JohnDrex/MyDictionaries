# Write a program that reads the contents of a text file 
# (you can use this file - sometext.txt 
# The program should create a dictionary in which the keys are the individual
#  words found in the file and the values are the number of times each word appears. For example, 
# if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 
# 128 as the value. The program should display the frequency of each word.

txtfile = open('sometext.txt', 'r')

txt = txtfile.read()
txt = txt.rstrip('\n' + ','+'.')
list = (txt.split(' '))

dict = {}
print(list)
for record in list:
    if record in list and record not in dict:
        a = list.count(record)
        dict[record]={'count': a}
print(dict)