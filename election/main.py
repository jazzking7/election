# Author: Jasper Wang
# Date: 20 Sep 2021
# Goal: calculate minimum votes needed to win an election using 0-1 knapsack
from knapsack import *
def txtprocessor(filename):
    # Open the file
    file = open(filename,"r")
    number_of_state = int(file.readline())
    # Read data
    data = []
    for i in range(number_of_state):
        info = file.readline().split(" ")
        data.append(info)
    return data

def main():
    running = True
    while running:
        x = input("Enter the filename: ")
        result = getminvotes(txtprocessor(x))
        print(f'Min votes required to win the election: {result}' if result < sys.maxsize else\
                  "This election is impossible to win!")
        cont = input("Continue? y/n: ")
        running = True if cont.upper() == "Y" else False

if __name__ == "__main__":
    main()