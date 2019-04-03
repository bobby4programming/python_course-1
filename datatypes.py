#Write a programme to multiply all the items in a list.

items = [1,3,4,5,6]
for item in items:
    item * 2


#Using "while" loop write a programme that loops from 1 - 100. 
#It should print "fizz" if the number is divisible by 3, and print "buzz" if the number is divisible by 5. 
#If the number is divisible by 3 and 5 if should print "fizzbuzz".

num = 1
while num <= 100:
    if num % 15 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)
    num += 1  
 
# Write a programme that performs unit conversion from grammes to kilogrammes. e.g If giving an argument of 5000g, it should return 5kg as output.

def convert_gram_to_kilogram(unit):
    return str(unit / 1000)+'g'

#Write a programme to find the Max of list numbers.

def find_max_num(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
            continue
    return max_num