import os, sys
sys.path.insert(0, './modules')
import assets
import rsa_algorithm as calc


if __name__ == '__main__':
    print assets.banner
    loop = True
    while loop:
        print assets.menu
        choice = input("Enter your choice [1-5]: ")
#=============================================================================== 
        if choice == 1:
            p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
            q = int(raw_input("Enter another prime number (Not one you entered above): "))
            print "Generating your public/private keypairs now . . ."
            pub, priv = calc.keypair(61,53)
            print "Your public key is: ", pub, " and your private key is: ", priv
            raw_input("Press enter to continue to main menu.")          
#===============================================================================   
        elif choice == 2:
            try:
                pub
            
            except NameError:
                p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
                q = int(raw_input("Enter another prime number (Not one you entered above): "))
                print "Generating your public/private keypairs now . . ."
                pub, priv = calc.keypair(61,53)
                print "Your public key is: ", pub, " and your private key is: ", priv

                message = raw_input("Enter a msg to encrypt with your pub key: ")
                to_encrypt = [ord(char) for char in message]
                print "The ascii representation of your message is:", to_encrypt
                
                cipher =[]
                for i in range(len(to_encrypt)):
                    cipher.append(calc.encrypt(priv, to_encrypt[i]))
                print "Your encrypted cipher is:", cipher
                raw_input("Press enter to continue to main menu.")  
            
            else:
                message = raw_input("Enter a msg to encrypt with your pub key: ")
                to_encrypt = [ord(char) for char in message]
                print "The ascii representation of your message is:", to_encrypt
                
                cipher =[]
                for i in range(len(to_encrypt)):
                    cipher.append(calc.encrypt(priv, to_encrypt[i]))
                print "Your encrypted cipher is:", cipher
                raw_input("Press enter to continue to main menu.")  
#===============================================================================
        elif choice == 3:
            try:
                pub
            
            except NameError:
                p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
                q = int(raw_input("Enter another prime number (Not one you entered above): "))
                print "Generating your public/private keypairs now . . ."
                pub, priv = calc.keypair(61,53)
                print "Your public key is: ", pub, " and your private key is: ", priv
                
                cipher = raw_input("Enter a cipher to decrypt with your private key: ")
                cipher = cipher.split(", ")
                cipher = [s.strip('[') for s in cipher]
                cipher = [s.strip(']') for s in cipher]
                cipher = map(int,cipher)
                
                to_decrypt = []
                for i in range(len(cipher)):
                    to_decrypt.append(calc.decrypt(pub, cipher[i]))
                print "The ascii representation of your decrypted cipher is:", to_decrypt
                print "Your decrypted cipher is:", ''.join(map(chr,map(int, to_decrypt)))
                raw_input("Press enter to continue to main menu.")  

            else:
                cipher = raw_input("Enter a cipher to decrypt with your private key: ")
                cipher = cipher.split(", ")
                cipher = [s.strip('[') for s in cipher]
                cipher = [s.strip(']') for s in cipher]
                cipher = map(int,cipher)
                
                to_decrypt = []
                for i in range(len(cipher)):
                    to_decrypt.append(calc.decrypt(pub, cipher[i]))
                print "The ascii representation of your decrypted cipher is:", to_decrypt
                print "Your decrypted cipher is:", ''.join(map(chr,map(int, to_decrypt)))
                raw_input("Press enter to continue to main menu.")  
#===============================================================================
        elif choice == 4:
            try:
                pub
            
            except NameError:
                p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
                q = int(raw_input("Enter another prime number (Not one you entered above): "))
                print "Generating your public/private keypairs now . . ."
                pub, priv = calc.keypair(61,53)
                print "Your public key is: ", pub, " and your private key is: ", priv
                
                message = open("input.txt", "r").read()
                print "Your file's message to encrypt is: \n", message
                to_encrypt = [ord(char) for char in message]
                print "The ascii representation of your message is:", to_encrypt
                
                cipher =[]
                for i in range(len(to_encrypt)):
                    cipher.append(calc.encrypt(priv, to_encrypt[i]))
                open("output.txt", "w+").write(str(cipher))
                print "Your encrypted cipher is: \n", cipher, "\nAnd it's been saved to output.txt"
                raw_input("Press enter to continue to main menu.")
                  
            else:
                message = open("input.txt", "r").read()
                print "Your file's message to encrypt is: \n", message
                to_encrypt = [ord(char) for char in message]
                print "The ascii representation of your message is:", to_encrypt
                
                cipher =[]
                for i in range(len(to_encrypt)):
                    cipher.append(calc.encrypt(priv, to_encrypt[i]))
                open("output.txt", "w+").write(str(cipher))
                print "Your encrypted cipher is: \n", cipher, "\n And it's been saved to output.txt"
                raw_input("Press enter to continue to main menu.")  
#===============================================================================
        elif choice == 5:
            try:
                pub
            
            except NameError:
                p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
                q = int(raw_input("Enter another prime number (Not one you entered above): "))
                print "Generating your public/private keypairs now . . ."
                pub, priv = calc.keypair(61,53)
                print "Your public key is: ", pub, " and your private key is: ", priv
                
                cipher = open("output.txt", "r").read()
                print "Your file's cipher to decrypt is: \n", cipher
                cipher = cipher.split(", ")
                cipher = [s.strip('[') for s in cipher]
                cipher = [s.strip(']') for s in cipher]
                cipher = map(int,cipher)
                
                to_decrypt = []
                for i in range(len(cipher)):
                    to_decrypt.append(calc.decrypt(pub, cipher[i]))
                print "The ascii representation of your decrypted cipher is:", to_decrypt
                print "Your decrypted cipher is:", ''.join(map(chr,map(int, to_decrypt)))
                raw_input("Press enter to continue to main menu.")
                
            else:
                cipher = open("output.txt", "r").read()
                print "Your file's cipher to decrypt is: \n", cipher
                cipher = cipher.split(", ")
                cipher = [s.strip('[') for s in cipher]
                cipher = [s.strip(']') for s in cipher]
                cipher = map(int,cipher)
                
                to_decrypt = []
                for i in range(len(cipher)):
                    to_decrypt.append(calc.decrypt(pub, cipher[i]))
                print "The ascii representation of your decrypted cipher is:", to_decrypt
                print "Your decrypted cipher is:", ''.join(map(chr,map(int, to_decrypt)))
                raw_input("Press enter to continue to main menu.")  
#===============================================================================
        elif choice == 0:
            loop = False
        else:
            raw_input("Wrong option selection. Enter any key to try again.")