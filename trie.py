
class Trie(object):

	_end = '_end_'

	max = 10

	def __init__(self,words, canonical):
		
		def make_trie(words, canonical):
			root = dict()
			for (word,replacement) in zip(words,canonical):
				current_dict = root
				for letter in word:
					current_dict = current_dict.setdefault(letter, {})
				current_dict = current_dict.setdefault(Trie._end, replacement)
			return root

		self.trie = make_trie(words, canonical)


	def search(self, word):
	    current_dict = self.trie
	    for letter in word:
	        if letter in current_dict:
	            current_dict = current_dict[letter]
	        else:
	            return False
	    else:
	        if Trie._end in current_dict:
	            return current_dict[Trie._end]
	        else:
	            return False

