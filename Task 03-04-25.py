'''
1.write a program that finds the smallest prime digit (2, 3, 5, or 7) in a given number?

ANS:-

'''
def find_smallest_prime_digit(num):
  prime_digits = [2, 3, 5, 7]
  smallest_found = None
  for digit in str(num):
    digit_int = int(digit)
    if digit_int in prime_digits:
      if smallest_found is None or digit_int < smallest_found:
        smallest_found = digit_int
  return smallest_found
numbers = [123456789, 987654321, 1024, 500, 1111, 75321, 6480]
for num in numbers:
  smallest_prime_digit = find_smallest_prime_digit(num)
  if smallest_prime_digit:
    print(f"Smallest prime digit in {num}: {smallest_prime_digit}")
  else:
    print(f"No prime digit found in {num}")