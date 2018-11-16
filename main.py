import os, sys
sys.path.insert(0, './modules')
import assets


if __name__ == '__main__':
    print assets.banner
    #print assets.binary_exponentiation(123, 1001, 101)
    loop = True
    while loop:
        print assets.menu1
        choice = input("Enter your choice [1-5]: ")
        if choice == 1:
            pub, priv = assets.keypair(61,53)
            print pub, priv
#===============================================================================            
            message = raw_input("Enter a msg to encrypt with your pub key: ")
            #to_encrypt = [str(ord(char)).zfill(3) for char in message]
            to_encrypt = [ord(char) for char in message]
            #to_encrypt = map(int, to_encrypt)
            print to_encrypt
            
            cipher =[]
            for i in range(len(to_encrypt)):
                cipher.append(assets.encrypt(priv, to_encrypt[i]))
            print cipher
            
            print map(int, cipher)
            #print ''.join(map(lambda x: str(x), cipher))
            #print to_encrypt
#===============================================================================   
            cipher = raw_input("Enter a cipher to decrypt with your private key: ")
            cipher = cipher.split(", ")
            cipher = [s.strip('[') for s in cipher]
            cipher = [s.strip(']') for s in cipher]
            cipher = map(int,cipher)
            print cipher
            print type(cipher)
            
            to_decrypt = []
            for i in range(len(cipher)):
                to_decrypt.append(assets.decrypt(pub, cipher[i]))
            print to_decrypt
            
            print ''.join(map(chr,map(int, to_decrypt)))
        
        elif choice == 2:
            loop = False
            
#===============================================================================
# xx=[str(ord(char)).zfill(3) for char in "a&%"]
# print ''.join(map(lambda x: str(x), xx))
# [cipher[i:i+3] for i in range(0, len(cipher), 3)]
# listanum = map(int, listacipher)
# ''.join(map(chr,listanum))
#===============================================================================