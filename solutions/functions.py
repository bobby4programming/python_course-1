# QUESTION 1
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
# sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def generate_fib_numbers():
        fib_nums = [1,1]
        fib_prev = fib_curr = 1 
        itr = 2
        while True:
                user_input = int(input('give me a number that is greater than 0 ? '))
                if isinstance(user_input, int) and user_input > 0:
                        break
        if user_input == 1:
                return [1]
        if user_input == 2:
                return fib_nums
        while itr < user_input:
                fib = fib_prev + fib_curr
                fib_prev = fib_curr
                fib_curr = fib
                fib_nums.append(fib)
                itr += 1
        return fib_nums


# QUESTION 2
# Write a function that returns student information if given a “student id” and a list of students as a parameter. 
# The student data should come from a list of students containing at least five students. 
# E.g. { “id” : 1, “name” : ”James Wale”, “age” : 23, “sex” : ”male”, “height” : “167 cm” }

def get_student_info(student_id, students):
        if isinstance(student_id, int) and isinstance(students, list):
                if student_id < 1 or len(students) == 0:
                        return {}
                for student in students:
                        if student['id'] == student_id:
                                return student
                return {}
        else:
                return f'Invalid input for student {student_id} of student list'


# QUESTION 3
# Write a function to count the number of strings where the string length is 2 or more and the first and 
# last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result = 2

def get_finite_automata_count(list_of_strings):
        count = 0
        if isinstance(list_of_strings, list):
                if not list_of_strings:
                        return count
                for item in list_of_strings:
                        if len(item) > 2 and item[0] == item[-1]:
                                count += 1
        else: 
                'input should be a list of strings'
        return count


# QUESTION 4
# Write a getPrimes function that takes an integer value n as argument and generates prime numbers from 0 to n with asymptotic analysis. 
# The generated prime numbers should be in an array. Your logic should be as efficient as possible (with minimal iterations).

# get_primes help function to check is number is a prime number
def is_prime(n):
        for d in range(2, n):
                if n % d == 0:
                        return False
        return True

def get_primes(n):
        primes = []
        if isinstance(n, int) == False:
                return 'Input should be an integer'
        if n == 1:
                return []
        for i in range(2, n+1):
                if is_prime(i):
                        primes.append(i)
                
        return primes
