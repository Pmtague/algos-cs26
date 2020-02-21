#!/usr/bin/python

import math
# Check for the recipe item in the ingredients list
# If the item is not there, return 0
# If the item is there, divide the item value in ingredients by the item value in recipe
# Store the value in a list
# Return the smallest value in the new list


def recipe_batches(recipe, ingredients):
	batches = []
	for key in recipe:
		if not key in ingredients:
			return 0
		else:
			batches.append(ingredients[key] // recipe[key])
	return min(batches)
		


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
