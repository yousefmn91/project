class Zaman:
    """
        Namayeshe zaman rooz.
        
        attributes: saat, daghighe, sanie
        
    """
zaman = Zaman()
zaman.saat = 8
zaman.daghighe = 45
zaman.sanie = 12 

def print_zaman(t):
    """ namayeshe string az zaman
    
        t: Zaman obj
        
    """    
    print('%.2d:%.2d:%.2d' % (t.saat, t.daghighe, t.sanie))
    
    
def afzoodane_zaman(t1, t2):
#    if not zaman_sahih(t1) or not zaman_sahih(t2):
#        raise ValueError('obj Zaman sahih nist.')
    assert zaman_sahih(t1) and zaman_sahih(t2)
    sanieha = zaman_be_int(t1) + zaman_be_int(t2)
    return int_be_zaman(sanieha)    


def afzayesh(zaman, sanieha):
    zaman.sanie += sanieha
    
    if zaman.sanie >= 60:
        zaman.sanie -= 60
        zaman.daghighe += 1
        
    if zaman.daghighe >= 60:
        zaman.daghighe -= 60
        zaman.saat += 1    
        
def zaman_be_int(zaman):
    daghigheha = zaman.saat * 60 + zaman.daghighe   
    sanieha = daghigheha * 60 + zaman.sanie    
    return sanieha

def int_be_zaman(sanieha):
    zaman = Zaman()
    daghigheha, zaman.sanie = divmod(sanieha, 60)
    zaman.saat, zaman.daghighe = divmod(daghigheha, 60)
    return zaman

def zaman_sahih(zaman):
    if zaman.saat < 0 or zaman.daghighe < 0 or zaman.sanie < 0:
        return False
    if zaman.daghighe >= 60 or zaman.sanie >= 60:
        return False
    return True
    





