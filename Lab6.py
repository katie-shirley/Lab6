# This is for Lab 6 for COP3502C

def encode(password):
    password_str = str(password)
    encoded = ''
    for i in password_str:
        # temp = password_Str[i]
        encoded = int(password_st


# this is the beginning of Hannah Wait's code
def decode(password):
	# convert int password to str
	password = str(password)

	# initialize decoded password string
	decoded_password = ''

	# iterate through encoded password and decode
	for num in password:

		# convert back to int, subtract 3, and append to decoded_password as str
		num = int(num) - 3
		decoded_password += str(num)

	return decoded_password
# this is the end of Hannah Wait's code


if __name__ == '__main__':
    option = 0
    while option != 3:
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

