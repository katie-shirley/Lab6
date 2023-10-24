#This is for Lab 6 for COP3502C

def encode (password):
	password_str = str(password)
	encoded = ''
	for i in password_str:
		#temp = password_Str[i]
		encoded = int(password_st

def decode (password)
	password_str =str(password)
	decoded = ''
	for i in password_str:
		decoded = int(password_str[i]-3)
	return decoded

if __name__ == '__main__':
   option = 0
   while option !=3:
	password = ''
	print()
	print('Menu\n-------------\n')
	print('1. Encode')
	print('2. Decode')
	print('3. Quit')
	pinrt()
	option = int(input("Please enter an option: "))

	if option == 1:
		password = input("Please enter your password to encode: ")
		encoded_pw = encode(password)
		print("Your password has been encoded and stored!")
	if option == 2:
		print("The encoded password is " + encoded_pw + " and the original password is " + decode(encoded_pw))
	if option == 3:
		break

	

