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