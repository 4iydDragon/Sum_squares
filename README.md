# Problem:
  # Write a program that inputs numbers
  # Calculate the square of the number in numbers
  # Calculate the sum of the squares of the numbers
  # the sum of the squares
  
# Define the {sum_square} class with the numbers{numb} as the input
def sum_square():
  # Request user to input a list of numbers
  numbs = input("Enter a list of numbers separated by space: ")
  # Set number in numbers as an integer and split the numbers with a space
  numbs = [int(n) for n in numbs.split(" ")]
  # set the {sum} variable to 0
  sums = 0
  # for the number{n} in the numbers{numb}:
  for n in numbs:
    # set square as equal to the square of the number{n * n}
    square = n ** 2
    # set the sum as equal to the {square} + previous {sum}
    sums = square + sums
  # return the value of the sum
  return sums

# print the class
print(sum_square())
