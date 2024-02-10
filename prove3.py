Domain1 = {2,4,6,8,16}
Set1 = {1/n for n in Domain1} # Add Set Comprehension Code Here
Domain2 = {-2,-1,0,1,2}
Set2 = {n**2 for n in Domain2} # Add Set Comprehension Code Here
Set3 = {n for n in range(1,100) if 24 % n == 0} # Add Set Comprehension Code Here
Set4 = {n for n in range(-100,100) if n >= -10 and n <= 10} # Add Set Comprehension Code Here



# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)