"""
PROBLEM: 

Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.
For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

HIGH LEVEL ANSWER: 

You can set a found variable inside count. 
You can then loop over your sequence and increment found 
every time you find an element in the sequence that matches item
"""

def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
        	found += 1
    return found

print(count([1,2,1,1,1,4,4,4,5,6], 4))
