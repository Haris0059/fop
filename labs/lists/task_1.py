# Write a function to return the list of elements squared.

def square_list(list):
    return [i ** 2 for i in list]

lista = [1,2,3,4,5]
print(square_list(lista))