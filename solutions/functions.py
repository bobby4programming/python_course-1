# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
# sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def generate_fib_numbers(user_input):
        fib_nums = [1,1]
        fib_prev = fib_curr = 1 
        itr = 2

        while itr < user_input:
                fib = fib_prev + fib_curr
                fib_prev = fib_curr
                fib_curr = fib
                fib_nums.append(fib)
                itr += 1
        return fib_nums

#user_input = int(input('give me a number that is at least greater than 1 ? '))

#print(generate_fib_numbers(user_input))
        