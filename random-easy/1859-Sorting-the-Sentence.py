def sortSentence(s):
    words = s.split()
    tmp = {}
    sentense = ""
    for i in words:
        tmp[i[-1]] = i[:-1]
    for j in sorted(tmp):
        sentense += tmp[j] +  ' '

    return sentense[0:-1]
        
print(sortSentence("is2 sentence4 This1 a3")) # This is a sentence
print(sortSentence("Myself2 Me1 I4 and3")) # Me Myself and I
