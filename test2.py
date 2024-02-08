
def mergeStrings(one,two):

    targetString=""
    str_one_len = len(one)
    str_two_len = len(two)
    print(str_two_len)

    if (str_one_len > str_two_len):
        for i in range(str_two_len):
            targetString = targetString + one[i]
            targetString+=two[i]
        
        targetString+= one[str_two_len:str_one_len]  
    else:
        for i in range(str_one_len):
            targetString = targetString + one[i]
            targetString+=two[i]
        
        targetString+= one[str_two_len:str_one_len]  

    print(targetString)
one="abcdefghijklmnopqrstuvwxyzbfjwefbwhbijsijdhajhkwjhdoskdfjowkdhokfowdojsofhkefjhkfjhsk"

two="zyomjikljfisfjhisjfhinihirjwhfidujhfijhdjsjabcdefghijklmnopqrstuvwxyzbfjwefbwhbijsijdhajhkwjhdoskdfjowkdhokfowdojsofhkefjhkfjhsk"
mergeStrings(one,two)