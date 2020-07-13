def searchforvowels():

    w = input('Yek kalame benevis: ')
    v = set('aeiou')
    found = v.intersection(set(w))
    for vowel in found:
        print(vowel)
    
print (searchforvowels())

    