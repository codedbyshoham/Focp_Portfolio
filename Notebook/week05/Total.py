import sys

count = len(sys.argv)

total = 0.0

index = count - 1
while index > 0:
    total += float(sys.argv[index])
    index -= 1

num_values = count - 1

if num_values > 0:
    average = total / num_values
    print("Total is", total)
    print("Average is", average)
else:
    print("no arguments were provided")
