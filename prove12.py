from math import factorial

def P(n, r):
    return factorial(n) // factorial(n - r)

def C(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Total number of fruits available
total_fruits = 9

# Number of fruits to choose for the fruit salad
fruits_for_salad = 5

# Calculate the number of different combinations for the fruit salad
combinations = C(total_fruits, fruits_for_salad)

# Scenario 1: Form a committee of 5 from 8 people
committee_5_from_8 = C(8, 5)

# Scenario 2: Select 8 people from 26 for a project
select_8_from_26 = C(26, 8)

# Scenario 3: Select 15 winners from 100 contestants
select_15_from_100 = C(100, 15)

print("How many ways can we form a committee of 5 people from a group of 8 people?", committee_5_from_8)
print("How many ways can we select 8 people from a group of 26 people to work on a single project, assuming all people are equally qualified?", select_8_from_26)
print("How many ways can we select 15 winners for a vacation drawing from a group of 100 contestants assuming each prize is the same?", select_15_from_100)
