natural-sort
============

Natural Sort is defined as sorting that is intuitive for users. FileNameComparator1.py contains the compare function which takes two strings s1 and s2, and returns 1 if s1 is greater than s2, 0 if equal and -1 otherwise. Here is an non exhaustive list of things it does at the moment.


* Orders by whole numbers, so "File2" would appear before "File10" (except when there are dates)
* Files with the same prefix come together, so ["player","player2","player2Algo","playerAlgo"]
would be sorted to ["player","playerAlgo","player2","player2Algo"]
* Recognizes dates and sorts according to them. So "DSC_09-23-1994.jpg" comes before "DSC_01-01-2010.jpg"
* Padded zeroes dont count. So "File0001" would come before "File2".
* Common abbreviations are automatically canonicalized. So, "logov1" comes before "logoversion2" comes before "logov3".


ReplacementTrie in FileNameComparator1.py takes two lists as input for the Trie constructor. The ith element of list2 is the string that the ith element of list1 should be replaced by in s1 and s2.
