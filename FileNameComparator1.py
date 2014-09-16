import re
from trie import Trie

ReplacementTrie = Trie(["version","location"],["v","loc"])	# Trie containing common abbreviations and their replacements


''' 

This functions compares two filenames and enforces a "natural" ordering to them, such that it is intuitive to end users.
Here is an non exhaustive list of things it can do.

*	Orders by whole numbers, so "File2" would appear before "File10" (except when there are dates)
*	Files with the same prefix come together, so ["player","player2","player2Algo","playerAlgo"] 
	would be sorted to ["player","playerAlgo","player2","player2Algo"]
*	Recognizes dates and sorts according to them. So "DSC_09-23-1994.jpg" comes before "DSC_01-01-2010.jpg"
*	Padded zeroes dont count. So "File0001" would come before "File2".
*	Common abbreviations are automatically canonicalized. So, "logov1" comes before "logoversion2" comes before "logov3".

'''

def compare(s1, s2):
	

	''' 
	This function does a linear pass over the two strings and canonicalizes common abbreviations. Like version for version etc
	This is order len(s1) as the elements in the Trie are constant, and so is the Max length of abbreviations.
	'''
	def canonicalizePass(s1):
		for i in xrange(len(s1)):
			for j in xrange(i,max(Trie.max,len(s1))):
				rep = ReplacementTrie.search(s1[i:j]) 
				if rep != False:
					s1 = s1[:i] + rep + s1[j:]
					return s1
		return s1


	''' 
	This function compares two characters and returns 1 if c1 is greater than c2, -1 if c1 is lesser than c2, and 0 if equal.
	There is a slight change in order when compared to ASCII values. Numbers are assigned the highest priority. This ensures that
	all filenames with same prefixes are clubbed together in the sorted list. 
	'''

	def comparechar(c1, c2):
		if c1.isdigit() and not c2.isdigit():
			return 1
		if not c1.isdigit() and c2.isdigit():
			return -1

		if c1 < c2:
			return -1
		elif c1 > c2:
			return 1
		return 0

	s1 = re.sub("(\d\d)([\/\-\.\:])(\d\d)([\/\-\.\:])(\d\d\d\d)", "\\5\\4\\1\\2\\3", s1)    # Normalizing dates so that the function can sort them properly
	s2 = re.sub("(\d\d)([\/\-\.\:])(\d\d)([\/\-\.\:])(\d\d\d\d)", "\\5\\4\\1\\2\\3", s2)

	s1 = canonicalizePass(s1)
	s2 = canonicalizePass(s2)

	i = 0	# Index of first string
	j = 0	# Index of first string
	state = 0 # 1 if previous characters of both strings are different numbers else 0 
	ret = 0		# The value that we will eventually return
	while i < len(s1) and j < len(s2):
		# To remove padded 0s from the s1
		if s1[i] == '0' and state == 0:
			i += 1
			continue
		# To remove padded 0s from the s2
		if s2[j] == '0' and state == 0:
			j += 1
			continue
		if s1[i] == s2[j]:
			if s1[i].isdigit():
				state = 1										# If we see a digit, we set state = 1
			i += 1
			j += 1
		else:
			# If we have seen a bigger number in one string, we return the ret when we see a character
			# We cant do it before seeing all the digits of the two numbers
			if ret != 0 and not s1[i].isdigit() and not s2[j].isdigit():
				return ret
			elif not s1[i].isdigit() and not s2[j].isdigit():
				return comparechar(s1[i],s2[j])
			# If a number is longer than another, the string containing it should be the greater string
			elif not s1[i].isdigit() and s2[j].isdigit() and state == 1:
				return -1
			elif s1[i].isdigit() and not s2[j].isdigit() and state == 1:
				return 1
			# We set ret and whenever we see different digits at the same index in the two strings
			elif state == 0 and s1[i].isdigit() and s2[j].isdigit():
				state = 1
				ret = comparechar(s1[i], s2[j])
				i += 1
				j += 1
			elif state == 0 and (not s1[i].isdigit() or not s2[j].isdigit()):
				return comparechar(s1[i],s2[j])
			elif state == 1 and s1[i].isdigit() and s2[j].isdigit():
				if ret == 0:
					ret = comparechar(s1[i], s2[j])
				i += 1
				j += 1
	# If one of the strings is exhausted
	if i == len(s1) and j!= len(s2):
		if state == 0 or s2[j].isdigit():
			return -1
		if not s2[j].isdigit():
			if ret == 0:
				return -1
			return ret
	if i != len(s1) and j== len(s2):
		if state == 0 or s1[i].isdigit():
			return 1
		if not s1[i].isdigit():
			if ret == 0:
				return 1
			return ret
	return ret
				
