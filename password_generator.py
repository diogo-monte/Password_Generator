import random
all = ['q','w','e','r','t','y','u','i','o','p','[','{','}',']','|','a','s','d',
       'f','g','h','j','k','l',';','z','x','c','v','b','n','m',' ','/',
       '0','1','2','3','4','5','6','7','8','9','*','+','-','~','!','@','#','$',
       '$','%','^','&','(',')','=']
while True:
       try:
              password_len = int(input("How many digits for the password? "))
              password = ''
              for x in range(0, password_len):
                     digit = all[random.randint(0, len(all)-1)]
                     if x % 2 == 0:
                            password += digit
                     else:
                            password += digit.upper()
              print(password)
       except ValueError:
              print('Only integer numbers, please')