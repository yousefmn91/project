phrase = 'Parcham balast! '

ph_list = list(phrase)

for i in range (2):
    ph_list.pop()
    
ph_list.pop (0)
ph_list.remove ('s')
ph_list.remove (' ')

ph_list.insert (0, ph_list.pop(-5))
ph_list.insert (2, ph_list.pop(4))

ph_list.remove ('c')


new_ph = ''.join (ph_list)

for i in range (4):
    ph_list.pop()

        


print (ph_list)
print (new_ph)
