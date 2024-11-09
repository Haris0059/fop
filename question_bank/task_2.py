# Write a Python program to construct the following pattern, using a nested for loop.
#   *
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *
# 	* * * *
# 	* * *
# 	* *
# 	*

for i in range(1,6):
    print(" *" * i)
    if i == 5:
        for j in range(1,5):
            print(" *" * (i-j) )
