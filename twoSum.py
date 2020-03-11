# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:08:24 2020

@author: Blessing
"""

def twoNumberSum(array, targetSum):
    # O(n) time | O(n) space
	num_to_index = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in num_to_index:
			return [potentialMatch, num]
		else:
			num_to_index[num] = True
	return []