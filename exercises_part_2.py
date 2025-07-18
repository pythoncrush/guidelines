#New collection data type called set
#Sets are declared with {} or set() syntax
this_is_a_set = {'a','b','c','d','e','f','g',1,2,3,4}
single_digit_set = set([0,1,2,3,4,5,6,7,8,9,'a','b','c'])

#Remove duplicates with ease
list_with_duplicates = ['fish','heads','fish','heads','eat','them', 'up', 'yum']
no_more_duplicates = set(list_with_duplicates)
print(no_more_duplicates)
#{'eat', 'up', 'fish', 'them', 'heads', 'yum'}

#Coolest thing about sets is they allow set theory operations
#Removing Duplicates: Efficiently eliminate duplicate values from a collection.
#Membership Testing: Quickly check for the presence of an element.
#Mathematical Set Operations: Performing operations like union, intersection, and difference on data.

#union operation  | (combine elements from sets)
union_of_sets = this_is_a_set | single_digit_set

print(union_of_sets)
#{'b', 1, 2, 3, 4, 0, 'c', 'd', 5, 6, 7, 8, 9, 'a', 'g', 'e', 'f'}


#intersection operation &  (elements in both sets)
intersection_of_sets = this_is_a_set & single_digit_set
print(intersection_of_sets)
#{'b', 1, 2, 3, 4, 'c', 'a'}

#difference operation - (elements in the first set but not the second).
difference_of_sets = this_is_a_set - single_digit_set
print(difference_of_sets)
#{'e', 'f', 'g', 'd'}

#symmetric difference ^ (Also known as mututal exclusion) (elements in either set, but not both)
mutual_exclusion_of_sets = this_is_a_set ^ single_digit_set
print(mutual_exclusion_of_sets)
#{0, 5, 6, 7, 8, 9, 'd', 'e', 'f', 'g'}


#1
#Create data structures and logic below to give a final count like this
#Andre:
#word count total: <n>
#Big Boi:
#word count total: <n>

with open('southernplaya_lyrics.txt', 'r') as f:
    for line in f:
    	print(f"current line is {line}")

#2
#Extend solution to #1 by counting unique words
#For instance the word 'the' is used many time but it only counts as 1 in the unique words counter

#3
#Extend solution from previous to count the length of all words in lyrics and put them in counters
#words_under_4_characters    	
#words_above_4_characters
#words_above_35_characters