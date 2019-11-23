#Cipher Problem


def cipher(k): #creates the cipher
    alpha_list=[] # Creates list for Alphabet
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        alpha_list.append(i)
        #print(alpha_list)

    key_list = []  # Creates a list for any potential key
    for l in k:
        key_list.append(l)
        #print(key_list)

    cipher= dict(zip(alpha_list,key_list))# creates a dictionary which translates alpha to key
    #print(cipher)
    return cipher

def encrypt(s,k):
    c=cipher(k)
    w=s.lower() #makes the entire string lower case

    input_w=[]#list of letters from input string
    for i in w:#adds letters to the list
        input_w.append(i)
        #print(input_w)

    output=[] #list of the output ciphered letters
    for i in input_w:
        output.append(c[i])


    final_encryption=''.join(output) #concatonates ciphered letters

    return final_encryption


def decrypt(s,k):
    c=cipher(k)
    inv_c = {a: b for b, a in c.items()} # inverses the dictionary made in the cipher(k) function
    #print(inv_c)
    d=s.lower()

    input_d=[]
    for i in d:
        input_d.append(i)
        #print(input_d)

    output_d=[]
    for i in input_d:
        output_d.append(inv_c[i])
        #print(output_d)

    final_decryption="".join(output_d)
    return  final_decryption


print("Clear message = attackxxatxxdawn")
ec = encrypt('attackxxatxxdawn', 'cotdiyuzbvgkmhjsxrpewanfql')
print("encrypted = ", ec)
dc = decrypt(ec, 'cotdiyuzbvgkmhjsxrpewanfql')
print("decrypted = ", dc)
