# import time

# def main():
#     for i in range(60, -1, -1):
#         print(i)
#         time.sleep(1)
# main()
    # A program to average a set of numbers
#    Illustrates interactive loop with two accumulators

def main():
    sum = 0.0
    count = 0
    moredata = "yes"

    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ").lower()
    print("\nThe average of the numbers is", sum / count)

main()