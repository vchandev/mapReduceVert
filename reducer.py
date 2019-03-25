#!/usr/bin/env python
import sys
 
# Create a dictionary to map words to counts
wordcount = {}
 
# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()
 
    # parse the input from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count
 
# Write the tuples to stdout
# Currently tuples are unsorted

# Top 5 word count descending
print("Top 5 Word Frequencies")
for key, value in sorted(wordcount.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:5]:
        print "%s\t%s" % (value, key)

print("\n")

# Sort word count by highest frequency
print("All Word Frequencies")
for key, value in sorted(wordcount.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print "%s\t%s" % (value, key)

# Sort word count by keys alphabetically
# keylist = wordcount.keys()
# keylist.sort()
# for key in keylist:
#     print "%s\t%s" % (wordcount[key], key)

# Print unsorted word count
# for word in wordcount.keys():
#     print '%s\t%s'% ( word, wordcount[word] )