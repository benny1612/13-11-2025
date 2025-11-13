def caesar_cipher(word,number):
    list1=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y" ,"Z"]

    list2=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y" ,"Z"]
    new_word=""
    word=word.upper()
    word=word.replace(" ","")
    for i in word:
        if i in list1:
            i=list1.index(i)
            i=((i+number) % 26)
   
            new_word+=list2[i]
    return new_word       






def faence(word):

    new_word1=[]
    new_word2=[]
    new_word3=""

    word=word.replace(" ","")
    word=list(word)
    print (word)
    for i in range (len(word)):
        if i % 2==0:
            new_word1.append(word[i])
        else:
            new_word2.append(word[i])
 
    new_word1.append(new_word2)
    new_word1=str(new_word1)
    for t in new_word1:
        if t == " ":
            new_word1=new_word1.replace(" ","")
    for j in new_word1:
        if j.isalpha():
            new_word3 += j
    return new_word3


