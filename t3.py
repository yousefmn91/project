def bin(x):
    z=''
    d=0
    k=0
    while x!=0:
        r=x%2
        x=x//2
        z=z+str(r)
    z=z+'0'
    print(z[::-1])

    for x in z:
        if x=='0':
            k=k+1
        else:
            d=d+1
    print('sefr = ',k)
    print('yek = ',d)
x=int(input('yek adad vared konid: '))
bin(x)
