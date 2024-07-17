numerical_emojis = [
    '0️⃣',  # U+0030 U+FE0F U+20E3
    '1️⃣',  # U+0031 U+FE0F U+20E3
    '2️⃣',  # U+0032 U+FE0F U+20E3
    '3️⃣',  # U+0033 U+FE0F U+20E3
    '4️⃣',  # U+0034 U+FE0F U+20E3
    '5️⃣',  # U+0035 U+FE0F U+20E3
    '6️⃣',  # U+0036 U+FE0F U+20E3
    '7️⃣',  # U+0037 U+FE0F U+20E3
    '8️⃣',  # U+0038 U+FE0F U+20E3
    '9️⃣'   # U+0039 U+FE0F U+20E3
]

nums = ['1','2','3','4','5','6','7','8','9','0']



def to_emojicode(emojis):
    decimales = [ord(char) for char in emojis]
    lst_p = ""
    for i, decimal in enumerate(decimales):
        lst = ""
        for digit in str(decimal):
            lst += numerical_emojis[int(digit)]
        if i == len(decimales) - 1 or len(decimales) == 1:
            lst_p += lst
        else:
            lst_p += lst + " "
    return lst_p

def to_emojis(emojicode):
    emojis = ""
    for code in emojicode.split(' '):
        decimal = ""
        for emoji in code:
            numers = ""
            for u in emoji:
                if u in nums:
                    numers += u
            decimal += numers
        
        emojis += chr(int(decimal))
        
            
    
                    
    return emojis
        
            
            

# Ejemplo de uso:
emojicode = '1️⃣2️⃣8️⃣5️⃣8️⃣4️⃣ 1️⃣2️⃣8️⃣5️⃣8️⃣5️⃣ 1️⃣2️⃣8️⃣5️⃣8️⃣6️⃣'  # Ejemplo de emojis numéricos
emojis = to_emojis(emojicode)
print(emojis)  # Esto imprimirá una cadena con los emojis correspondientes en caracteres Unicode


