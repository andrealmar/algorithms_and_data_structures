"""
PROBLEM:

Write a function called censor that takes two strings, 
text and word, as input. It should return the text with the word you 
chose replaced with asterisks

For example: censor("this hack is wack hack", "hack")
Should return: "this **** is wack ****"

1. Assume your input strings won't contain punctuation or upper case letters.
2. The number of asterisks you put should correspond to the number of letters in the censored word.
"""

"""
HIGH LEVEL ANSWER:

After splitting the string with string.split(), 
you can loop through the indices in the list and replace 
the words you are looking for with their asterisk equivalent. 
Join the list at the end to get your sentence!
"""

def censor(text, word):
    return text.replace(word, "*" * len(word))

print(censor("isso aqui esta uma merda", "merda"))