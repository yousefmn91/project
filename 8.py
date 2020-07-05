w = input( 'yek kalame benevis: ')
v = ['a', 'i', 'o', 'u', 'e']

found = {}

found ['a'] = 0
found ['o'] = 0
found ['u'] = 0
found ['i'] = 0
found ['e'] = 0

for letter in w:
    if letter in v:
        found[letter] += 1
        
for k, v in sorted (found.items()):
    print (k, 'was found', v, 'times(s)')
    
    