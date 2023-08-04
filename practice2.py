import random

#generating random float values
float_nums = random.uniform(1.0, 10.0)
print(float_nums)

#generating random float values between 0 and 1
float_nums = random.random()
print(float_nums)

#generating random integers in a specific range
float_nums = random.randint(1,10)
print(float_nums)


#select random values from a list 

list1 = [1,2,3,6,8,10,34,56,76,45]
float_nums = random.choice(list1)
print(float_nums)

