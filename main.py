# def BracketCombinations(n: int) -> list[str]:
#     """
#     Generate all combinations of balanced parentheses for n pairs.
    
#     :param n: Number of pairs of parentheses
#     :return: List of valid combinations
#     """
#     def backtrack(s='', left=0, right=0):
#         if len(s) == 2 * n:
#             combinations.append(s)
#             return
#         if left < n:
#             backtrack(s + '(', left + 1, right)
#         if right < left:
#             backtrack(s + ')', left, right + 1)

#     combinations = []
#     backtrack()
#     return combinations

# print(BracketCombinations(3))  # Example usage

# def BracketCombinations2(n: int) -> int:
#     """
#     Read n(input number) which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses,
#     where n is the number for finding valid combination.    
#     """
#     def count_combinations(left, right):
#         if left == 0 and right == 0:
#             return 1
#         if left > right:
#             return 0
#         total = 0
#         if left > 0:
#             total += count_combinations(left - 1, right)
#         if right > 0:
#             total += count_combinations(left, right - 1)
#         return total

#     return count_combinations(n, n)
# print(BracketCombinations2(3))  # Example usage


# def factorial(n: int) -> int:
#     """
#     Calulate the factorial of a number n.
#     :param n: The number to calculate the factorial of
#     :return: The factorial of n
#     """
#     if(n < 0):
#         raise ValueError("Factorial is not defined for negative numbers")
#     if(n == 0 or n == 1):
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# print('Factorial')  
# print(factorial(3)) # Example usage

# def factorialWithoutAnyLoop(n: int) -> int:
#     """
#     Calculate the factorial of a number n without using any loops.
#     :param n: The number to calculate the factorial of
#     :return: The factorial of n
#     """
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     if n == 0 or n == 1:
#         return 1
#     # Recursive call to calculate factorial
#     number2 = factorialWithoutAnyLoop(n - 1)
#     return n * number2

# print('Factorial without any loop')
# print(factorialWithoutAnyLoop(3))  # Example usage

# def factorialCustom(n: int) -> int:
#     """
#     Calculate the factorial of a number n using a custom recursive approach.
#     :param n: The number to calculate the factorial of
#     :return: The factorial of n
#     """
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     if n == 0 or n == 1:
#         return 1
#     nextNumber = factorialCustom(n - 1)
#     return n * nextNumber

# print('Factorial Custom')
# print(factorialCustom(2))  # Example usage


# def checkPrimeNumberWithoutLoop(n: int) -> bool:
#     """
#     Check if a number n is prime without using any loops.
#     :param n: The number to check
#     :return: True if n is prime, False otherwise
#     """
#     if n % 2 == 0:
#         return False
#     return True
    
    
# print('Check Prime Number Without Loop')
# print(checkPrimeNumberWithoutLoop(17))  # Example usage

def checkPrimeNumberWithoutModulus(n: int) -> bool:
    """
    Check if a number n is prime without using the modulus operator.
    :param n: The number to check
    :return: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    def is_prime(num, divisor):
        baseCondition1 = divisor * divisor > num
        baseCondition2 = num // divisor * divisor == num
        if baseCondition1:
            return True
        if baseCondition2:
            return False
        return is_prime(num, divisor + 1)
    return is_prime(n, 2)
    
print('Check Prime Number Without Modulus')
print(checkPrimeNumberWithoutModulus(11))  # Example usage