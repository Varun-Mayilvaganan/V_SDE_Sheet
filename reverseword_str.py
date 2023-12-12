def reverseWords(s):
    words = s.split()
    print(words)
    reversed_words=[]
    for word in words:
        reversed_word=word[::-1]
        reversed_words.append(reversed_word)
        print(reversed_words)
    print( ' '.join(reversed_words))
reverseWords("iam batman")