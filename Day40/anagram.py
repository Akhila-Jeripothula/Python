# Two strings are anagrams if they contain the same characters with same frequency.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  

#output:
#True
