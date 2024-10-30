# We want to make a row of bricks that is an inch long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Write a function to return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small_bricks, big_bricks, row):
    calc_big_bricks = big_bricks * 5
    result = small_bricks + calc_big_bricks
    if result == row:
        return True
    else:
        return False

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))