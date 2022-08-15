"""
BEFORE WE BEGIN LOOKING AT THE FUNCTIONS:
-> what is time complexity
-> what is space complexity

ANSWER - How the execution time or additional memory changes in relation to the input
size changing
"""


def removeDuplicates(input):
    inputSet = set()
    for i in input:
        inputSet.add(i)
    print(inputSet)

# TIME - O(N) | SPACE - O(N)


removeDuplicates([1, 5, 5, 3, 2, 1])


def sumOfAllValues(input):
    for i in input:
        for j in input:
            print(i + j)

# TIME - O(N^2) | SPACE - O(1)

sumOfAllValues([1, 5, 5, 3, 2, 1])



def findSumRemoveDuplicatesThenPrintsAllThenFirstTen(input):
    inputSet = set()

    for i in input:
        for j in input:
            inputSet.add(i+j)
    for i in input:
        print(i)
    for i in range(10):
        print(inputSet[i])

# TIME - O(N^2) | SPACE - O(N)


"""
TIME/SPACE COMPLEXITY GENERAL RULES
1. Always think about the worst case scenario
2. See if new memory is created and what the size of that would be relative to the input (space complexity)
3. How is the time impacted if the input size increases (recursive calls, loops etc.)
4. Add complexities if they're separate logic
5. Multiply complexities if they're indented logic
6. Discard constants and insignifant values 2N -> N, N/2 -> N, N+ 10 -> N (always focus on the biggest effect)
"""

