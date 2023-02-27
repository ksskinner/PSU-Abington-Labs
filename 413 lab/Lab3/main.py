
input1 = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"
pattern1 = "CMPSC"
pattern2 = "course"
input2 = "AABAACAADAABAABAABBBBBAAABDCBA"
pattern3 = "BBBBBA"

def naivesearch(string1,string2):
    indexes = [] # list of matched indexes

    for x in range(len(string1)-len(string2)): #for each item in length of string - lenght of pattern
        if string1[x] == string2[0]: #if first character matches
            matched = True #set variable to true
            for y in range(len(string2)): #checks each item
                if string1[x+y] != string2[y]: #if string not matched
                    matched = False #set false and break out
                    break
            if matched:
                indexes.append(x) #else add the starting index to lsit
    if len(indexes) == 0: #if no matches found, return 0
        return -1
    else: #else return the indexes
        return indexes


def getLPS(pat):
    lps = [0] * len(pat) #set the LPS to all 0s
    pref = 0
    for i in range(1,len(pat)): #for each item after first

        while pref >0 and pat[i] != pat[pref]: #if the item doens't match the existing prefix
            pref = lps[pref - 1]

        if pat[i] == pat[pref]: #if the ltter matches the existing prefix
            pref += 1 #increase the prefix by 1
            lps[i] = pref

    return lps #return LPS

def KMPSearch(string1,pattern): #takes a string and a pattern
    indexes = [] #list of matched index
    lps = getLPS(pattern) #creates the LPS from pattern 1
    patindex = 0 #pattern index 1
    for i in range(len(string1)): # for each item in string
        while patindex>0 and pattern[patindex] != string1[i]: #if no match is found
            patindex = lps[patindex - 1]

        if pattern[patindex] == string1[i]: #if match is foundjoip
            if patindex == len(pattern) - 1: #if the full match is found
                indexes.append(i - patindex) #add the index to the list
            else:
                patindex += 1 #otherwise incement pointer and keep checking

    if len(indexes) == 0: # if matches were not found, return -1
        return -1
    else: # else return matches
        return indexes

naive1 = naivesearch(input1, pattern1)
naive2 = naivesearch(input1, pattern2)
naive3 = naivesearch(input2, pattern3)
kmp1 = KMPSearch(input1,pattern1)
kmp2 = naivesearch(input1, pattern2)
kmp3 = naivesearch(input2, pattern3)
print("Naive Search")
print("Pattern found at indexes " + str(naive1[0]) + " and " + str(naive1[1]))
print("Pattern found at indexes " + str(naive2[0]) + " and " + str(naive2[1]))
print("Pattern found at indexes " + str(naive3[0]))
print("---------")
print("KMP Search")
print("Pattern found at indexes " + str(kmp1[0]) + " and " + str(kmp1[1]))
print("Pattern found at indexes " + str(kmp2[0]) + " and " + str(kmp2[1]))
print("Pattern found at indexes " + str(kmp3[0]))

