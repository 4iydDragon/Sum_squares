def sum_square():
    numbs = input("Enter a list of numbers separated by commas: ")
    numbs = [int(n) for n in numbs.split(" ")]
    sums = 0
    for n in numbs:
        square = n ** 2
        sums = square + sums
    return sums

print(sum_square())