TODO: Reflect on what you learned this week and what is still unclear.
when appending certain strings into slots that are respective to the multiples of specified values, use the equation "i % [int] == 0"

e.g. To print the word "Fizz" for every multiple of three within a list from 1 to 100:

fizz_list = []
for i in range(1, 101):
if i % 3 == 0:
fizz_list.append("Fizz")
else:
fizz_list.append(i)
return fizz_list
