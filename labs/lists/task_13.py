# Write a function that for a given list of strings,
# returns a list where each string has all its ”x” removed.
# noX([”ax”, ”bb”, ”cx”]) -> [”a”, ”bb”, ”c”]
# noX([”xxax”, ”xbxbx”, ”xxcx”]) ->  [”a”, ”bb”, ”c”]
# noX([”x”]) ->  [””]

def no_x(lista):
    for i in lista:
        print(i)

print(no_x(["ax", "bb", "cx"]))
# print(no_x(["xxax", "xbxbx", "xxcx"]))
# print(no_x(["x"]))