from divide_and_conquer import *
from chip_and_be_conquered import *

# Chip and Be Conquered tests

test1 = chipAndBeConquered(56, 19, Rational(2, 1), Rational(9, 7), 'Test 1')
test2 = chipAndBeConquered(27, 11, Rational(31, 10), Rational(12, 7), 'Test 2')

# Divide and Conquer tests

test3 = divideAndConquer(56, Rational(80, 7), Rational(2, 1), Rational(9, 7), 'Test 3')
test4 = divideAndConquer(27, Rational(11, 6), Rational(31, 10), Rational(12, 7), 'Test 4')

print(f"Test 1: {test1}, Test 2: {test2}, Test 3: {test3}, Test 4: {test4}")