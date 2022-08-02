from ctypes.wintypes import WORD


def the_same(word):
    
    check=''

    for i in reversed(word):
        check+=i
       
    if check==word:
        return print("Wyraz jest Palindromem")
    
    elif check != word:   
        
        return print("Wyraz nie jest Palindromem")
      

the_same('potop')