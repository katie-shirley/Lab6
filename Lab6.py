#This is for Lab 6 for COP3502C

def encode (password):
	password_str = str(password)
	encoded = ''
	for i in password_str:
		#temp = password_Str[i]
		encoded[i] = int(password_str[i])+3
	return encoded

def decode (password)
	password_str =str(password)
	decoded = ''
	for i in password_str:
		decoded[i] = int(password_str[i]-3)
	return decoded


