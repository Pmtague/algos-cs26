#!/usr/bin/python

import argparse


def find_max_profit(prices):
	current_max = 0
	# Start with the first price and loop through
	for i in range(0, len(prices) - 2):

		# Compare with each of the following prices
		for k in range(i + 1, len(prices) - 1):
			diff = prices[k] - prices[i]

			# Allow for negative profit
			if diff < 0 and current_max == 0:
				current_max = diff

			# Replace with the max so far
			elif current_max < diff:
				current_max = diff
			k += 1
		i += 0
	max_profit = current_max
	return max_profit

if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(
		description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int,
						nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(
		profit=find_max_profit(args.integers), prices=args.integers))
