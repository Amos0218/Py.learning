def to_title_case(sentence):
    needlowers = {'a','an','the','and','but','or','for','nor','so','on','at','to','by','in','up','of'}
    words = sentence.split()
    title_cased_words = []
    for i,word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in needlowers:
            title_cased_words.append(word.capitalize())
        else:
            title_cased_words.append(word.lower())

    return ' '.join(title_cased_words)            

sentence = input()
result = to_title_case(sentence)
print(result)
