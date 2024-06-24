#File: ex3.1_solution.py

def check_divisibility(n1, n2, reverse = False):

    """A function that calculates whether the entered numbers n1 is divisible by n2. ( reverse = True : n1 divisible by n2 ) 

    Parameters
    ----------
    n1 : int 
         dividend ( divisor when reverse = True)
    n2 : int
         divisor ( dividend when reverse = True)
    
    Returns
    -------
    : Boolean
        True  - dividend divisible by divisor 
        False - divident not divisible by divisor

    """
    if reverse == False : 
      if n1 % n2 == 0:
        return True
      else:
        return False

    if reverse == True : 
      if n2 % n1 == 0:
        return True
      else:
        return False
        

def case_1():
    """
    function to check if the enetered integer is divisible by either [2,3,5,7]
    (uses the check divisibility fucntion defined above)
    """
    divisors = [2, 3, 5, 7]

    try:
      num = int(input("Enter an integer for which the divisiblity check needs to be performed: "))
      for divisor in divisors:
        if num % divisor == 0:
            print(f"{num} is divisible by {divisor}")
        else:
            print(f"{num} is not divisible by {divisor}")

    except ValueError:
      print("Enter a valid integer")


def case_2():
    """
    function to check if two integers entered are divisible by each other
    (uses the check_divisibility() with reverse = True and reverse = False )
    """
    try:
      num1, num2 = map(int, input("Enter two integers: " ).split())
        
      if check_divisibility(num1 , num2):
        print(f"{num1} is divisible by {num2}")
      else:
        print(f"{num1} is not divisible by {num2}")

      if check_divisibility(num1 , num2, reverse = True):
        print(f"{num2} is divisible by {num1}")
      else:
        print(f"{num2} is not divisible by {num1}")

    except ValueError:
      print("Enter 2 valid integers")
        
    except ZeroDivisionError:
      print("Enter non zero intergers to prevent division by zero")

if __name__ == '__main__' :
   case_1()
   print("\n")
   case_2()

