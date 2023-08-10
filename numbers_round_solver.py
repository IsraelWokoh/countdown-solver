from itertools import combinations as combos
from operator import add, sub, mul, truediv
def replaceOperands(newList, toRemove, toAdd) -> list:  # Removes operands, replaces with result
	for elem in toRemove:
		newList.remove(elem) # Remove operands
	newList.append(toAdd) # Append resulting element
	return newList

def solvable(ourNumbers: tuple, ourGoal: int) -> bool:
	# "empty" definitions above are for unsolvables.py to provide arguments

	'''
	>>> solvable((100, 9, 5, 10, 2, 4), 114) # Trivial solvable case
	True

	>>> solvable((1, 1, 2, 2, 3, 3), 999) # Trivial unsolvable case
	False

	>>> solvable((100, 2, 75, 5, 50, 8), 894) # Non-trivial unsolvable case 1
	False

	>>> solvable((75, 2, 50, 6, 2, 100), 257) # Non-trivial unsolvable case 2
	False

	>>> solvable((100, 75, 1, 25, 1, 50), 596) # Non-trivial solvable case 1
	True

	>>> solvable((100, 9, 5, 10, 2, 4), 566) # Non-trivial solvable case 2
	True
	'''

	solutionFound = False
	operators = {'+':add,
	             '-':sub,
	             '*':mul,
	             '/':truediv}

	# Nested function definition obviates the need for globals - non-locals instead
	def findSolution(currentNumbers: tuple or list,  # Starting 6 numbers - one less elem per recursion
	                 target: int) -> None: # Number to reach

		# Reverse makes sub/div simpler; tuple iterates more quickly than list
		currentNumbers = tuple(sorted(currentNumbers, reverse=True))

		nonlocal solutionFound
		for operands in combos(currentNumbers, 2):  # then iterate over operand pairs
			if solutionFound:
				break # break out of outer iteration

			for operator in operators.keys(): # Iterate over operators
				if solutionFound:
					break # break out of inner iteration

				operationResult = operators[operator](*operands) # does calculation with chosen pair and operator
				if operationResult == target: # if target reached
					solutionFound = True

				else: # target not reached
					if operationResult > 0 and not operationResult % 1: # if result is positive and integral
						newNumbers = replaceOperands(
									    list(currentNumbers), # using .append() function
							            operands,
							            int(operationResult) # Specified INT because div returns float
									 )

						findSolution(newNumbers, target) # Recurse



	findSolution(ourNumbers, ourGoal)
	return solutionFound

def getNumbers(): # Input numbers and target

	# Starting numbers
	ourNumbers = tuple(map(int, input('Enter number selection \
as integers separated by single spaces\n\
(e.g. "100  9  5  10  2  4") → ').split()))
	ourGoal = int(input('\nEnter integral value for target\n\
(e.g. "566") → '))
	# ourNumbers = (100, 9, 5, 10, 2, 4)
	# ourGoal = 566

	'''
	Possible solution:
	5*10
	50-9
	100+41
	141*4
	564+2
	'''

	return ourNumbers, ourGoal

if __name__ == '__main__':
	# find test cases under solvable()
	# un-comment the two lines below and run via cmd line to run tests
	# import doctest
	# doctest.testmod()

	if solvable(*getNumbers()):
		print(f'\nSolution found!')
	else:
		print('\nNo solutions found.')