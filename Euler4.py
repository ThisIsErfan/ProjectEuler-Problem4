#Project Euler(projecteuler.net)
#Largest palindrome product (Problem 4)
#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(number):
    number = str(number)
    reverse_of_number = number[::-1]
    return int(reverse_of_number)

palindromic_numbers = list()
for num1 in range(999,99,-1):
    for num2 in range(999,99,-1):
        mu = num1*num2
        if mu == reverse(mu):
            palindromic_numbers.append(mu)
            break
        
palindromic_numbers.sort()
print(palindromic_numbers.pop())