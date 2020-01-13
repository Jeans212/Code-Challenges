'''
     **** Strong Password ****
     Check the challenge at http://hr.gs/551sq

'''


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = '0123456789'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = "!@#$%^&*()-+"
    hasNumber = False
    hasLower = False
    hasUpper = False
    hasSpecial = False

    if n == 0:
        num = 6
    else:
        res = 0
        for i in range(n):
            if (password[i] in numbers):
                hasNumber = True
            if password[i] in lower_case:
                hasLower = True
            if password[i] in upper_case:
                hasUpper = True
            if password[i] in special_characters:
                hasSpecial = True
        if hasNumber == True:
            res += 1
        if hasLower == True:
            res += 1
        if hasUpper == True:
            res += 1
        if hasSpecial == True:
            res += 1

        if n > 0 and n < 6:
            num = max(6-n, 4-res)

        elif n >= 6:        
            num = 4 - res        
    return num

if __name__ == '__main__':
    n = int(input('Enter n: '))
    password = input('Enter password: ')
    answer = minimumNumber(n, password)
    print(answer)
