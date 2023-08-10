import numbers_round_solver
from itertools import combinations as combos

if __name__ == '__main__':
	allNumbers = (
		100, 75, 50, 25, # four 'large' numbers: multiples of 25
		10, 10, 9, 9, # two of each integer
		8, 8, 7, 7, # from 10 to 1
		6, 6, 5, 5, # called 'small' numbers
		4, 4, 3, 3,
		2, 2, 1, 1
	)

	noSolution = dict() # records no. of impossible games for every possible selection
	# there are 13243 unique selections
	# 899 possible target numbers (101-999) per selection
	# 13243 * 899 = 11905457 different games

	for selection in combos(allNumbers, 6): # passed to set because it was doubling up
		if selection in noSolution: # skip duplicates without storing full set
			print(f'skipping duplicate of {selection}') # testing
			continue

		print(selection)
		noSolution[selection] = 0 # records impossible games for each selection

		for goal in range(101, 1000):
			if not numbers_round_solver.solvable(selection, goal): # if selection can't reach goal
				noSolution[selection] += 1 # increments counter for selection
				print(f'{noSolution[selection]}: {goal}')

		print(f'Number of unsolvable targets: {noSolution[selection]}')
		print()

	print(f'Done!')