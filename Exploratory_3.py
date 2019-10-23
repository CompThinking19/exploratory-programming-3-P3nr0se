#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import re
def magnifying_glass(book):
    if type(book) != str:
        raise TypeError("Not a string!")
    result = re.findall('[a-zA-Z]*at\\b', book)
    atwords = []
    for word in result:
        if len(word) > 3:
            atwords.append(word)
    return atwords

source = open('A_Modest_Proposal.txt')
proposal = source.read()

print magnifying_glass(proposal)
