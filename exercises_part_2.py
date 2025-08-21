import re
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
bb_dict = {}
ad_dict = {}
ch_dict = {}
current_artist = None

with open("southernplaya_lyrics.txt", "r") as f:
    for line in f:
        if regex_match := re.search(r".*:\s(.*)\]$", line):
            current_artist = regex_match.group(4)
            continue
        
        for word in line.split():
            no_punct_word = re.sub(r"[^a-zA-Z0-9\s]", "", word)
            
            if "Big Boi" in current_artist:
                if no_punct_word in bb_dict:
                    bb_dict[no_punct_word] = bb_dict[no_punct_word] + 1
                else:
                    bb_dict[no_punct_word] = 1

            if "3000" in current_artist:
                if no_punct_word in ad_dict:
                    ad_dict[no_punct_word] = ad_dict[no_punct_word] + 1
                else:
                    ad_dict[no_punct_word] = 1

            if "Choir" in current_artist:
                if no_punct_word in ch_dict:
                    ch_dict[no_punct_word] = ch_dict[no_punct_word] + 1
                else:
                    ch_dict[no_punct_word] = 1

    # Total Big Boi
    print(f"Whole dictionary for Big Boi word counts {bb_dict.items()}")
    print(f"Unique words Big Boi {len(bb_dict.keys())}")
    print(f"Total words overall Big Boi including duplicates {sum(bb_dict.values())}")
    print(f"Words over 4 characters for Big Boi")


    # # Total Andre
    print(f"Unique words Andre {len(ad_dict.keys())}")
    print(f"Total words overall Andre including duplicates {sum(ad_dict.values())}")

    # # Total Chorus
    print(f"Unique words Chorus {len(ch_dict.keys())}")
    print(f"Total words overall Chorus including duplicates {sum(ch_dict.values())}")

#2
#Extend solution to #1 by counting unique words
#For instance the word 'the' is used many time but it only counts as 1 in the unique words counter

#3
#Extend solution from previous to count the length of all words in lyrics and put them in counters
#words_under_4_characters    	
#words_above_4_characters
#words_above_35_characters
