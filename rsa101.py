import rsa_algorithm as do
import assets



if __name__ == '__main__':
    print banner
    loop = True
    while loop:
    	print menu1
    	choice = input("Enter your choice [0-4]: ")
	    
	    if choice==0:     
	        loop = False
	    
	    # Generate new key pair
	    elif choice==1:
	    	p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
	    	q = int(raw_input("Enter another prime number (Not one you entered above): "))
	    	print "Generating your public/private keypairs now . . ."
	    	public, private = do.keypair(p, q)
	    	print "Your public key is ", public ," and your private key is ", private
	    
	    # Encrypt text from input		    
	    elif choice==2:
	    	if p,q in locals():
	    		message = raw_input("Enter a message to encrypt with your public key: ")
	    		cipher = do.encrypt_txt(private, message)
	    		print "Your encrypted message is: "
	    		print ''.join(map(lambda x: str(x), cipher))
	    	else:
	    		p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
	    		q = int(raw_input("Enter another prime number (Not one you entered above): "))
	    		print "Generating your public/private keypairs now . . ."
	    		public, private = do.keypair(p, q)
	    		print "Your public key is ", public ," and your private key is ", private
	    		message = raw_input("Enter a message to encrypt with your public key: ")
	    		cipher = do.encrypt_txt(private, message)
	    		print "Your encrypted message is: "
	    		print ''.join(map(lambda x: str(x), cipher))
	    	
	    # Decrypt text from input
	    elif choice==3:
	    	if p,q in locals():
	    		message = raw_input("Enter a cipher to decrypt with your private key: ")
	    		print "Decrypting message with private key ", private ," . . ."
	    		print "Your message is:"
	    		print do.decrypt_txt(private, cipher)
	    	else:
	    		p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
	    		q = int(raw_input("Enter another prime number (Not one you entered above): "))
	    		print "Generating your public/private keypairs now . . ."
	    		public, private = do.keypair(p, q)
	    		print "Your public key is ", public ," and your private key is ", private
	    		message = raw_input("Enter a cipher to decrypt with your private key: ")
	    		print "Decrypting message with private key ", private ," . . ."
	    		print "Your message is:"
	    		print do.decrypt_txt(private, cipher)
	    
	    # Encrypt/decrypt text from file
		elif choice==4:
	        ## You can add your code or functions here
	    elif choice==5:
	        ## You can add your code or functions here
	    else:
	        raw_input("Wrong option selection. Enter any key to try again.")




    p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
    q = int(raw_input("Enter another prime number (Not one you entered above): "))
    print "Generating your public/private keypairs now . . ."
    public, private = generate_keypair(p, q)
    print "Your public key is ", public ," and your private key is ", private
    message = raw_input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print "Your encrypted message is: "
    print ''.join(map(lambda x: str(x), encrypted_msg))
    print "Decrypting message with public key ", public ," . . ."
    print "Your message is:"
print decrypt(public, encrypted_msg)