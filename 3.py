Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> w = 'yousef'
>>> v = ['a', 'e', 'i', 'o', 'u']
>>> found = []
>>> for letter in w:
	if letter in v:
		if letter not in found:
			found.append(letter)

			
>>> for vowel in found:
	print (vowel)

	
o
u
e
>>> 