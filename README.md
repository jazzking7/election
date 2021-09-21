# election
A program to simulate an election

Input => a text file in the following format:
1. The first line is an integer indicating the number of states/territories/provinces
2. Each line consists of 4 integer numbers: a b c d, where
   a = weight of the territory
   b = number of people who decided to vote for you
   c = number of people who decided to vote for your opposition
   d = number of people who are undecisive

Output => the minimum amount of votes you need to receive in order to win the election
