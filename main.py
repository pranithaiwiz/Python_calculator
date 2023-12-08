def primeNumber_checker():
       num = int(input("Enter the number to chec wether it is prime or not : "))
       is_prime = True
       for i in range(2,num):
         if num%i == 0:
           is_prime = False 
       if is_prime:
         print("It is a prime number")
       else: 
         print("It is a non prime number")

primeNumber_checker()