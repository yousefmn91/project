def search_for_letters (phrase:str , letters:str) -> set:
    """ Majmoueye (set) horoofe peyda shode (letters) dar
    phrase ra bargardan"""
    return set (letters).intersection (set (phrase))

print (search_for_letters ('yousef','usdtyfi'))