def search_for_vowels (word:str) -> set:
    """ Har harfe seda dare peyda hode dakhele word
    ra bargardan"""
    v = set ('aeiou')
    return v.intersection (set(word))
print (search_for_vowels('teacher'))
