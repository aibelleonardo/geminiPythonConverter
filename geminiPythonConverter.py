def binary_to_decimal(binary_string):
  """
  Converts a binary string to its decimal equivalent.

  Args:
      binary_string: The binary string to convert.

  Returns:
      The decimal equivalent of the binary string.

  Raises:
      ValueError: If the input string contains invalid characters (not 0 or 1).
  """
  decimal = 0
  base = 1

  # Iterate through the binary string in reverse order
  for digit in binary_string[::-1]:
    # Check for invalid digits (not 0 or 1)
    if digit not in ('0', '1'):
      raise ValueError("Invalid binary string. Please enter only 0s and 1s.")

    # Convert digit to integer and add its value with base position
    decimal += int(digit) * base

    # Update base for the next digit
    base *= 2

  return decimal

def main():
  """
  Prompts user for input and performs binary to decimal conversion.
  """
  while True:
    try:
      binary_string = input("Enter a binary number: ")
      decimal = binary_to_decimal(binary_string)
      print("Decimal equivalent:", decimal)

      # Ask if user wants to continue
      choice = input("Do you want to perform another conversion? (y/n): ")
      if choice.lower() != 'y':
        break

    except ValueError as e:
      print(e)

if __name__ == "__main__":
  main()
