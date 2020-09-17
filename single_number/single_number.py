'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    count = [0 for _ in range(len(arr))]

    unique = None

    for i in arr:
        count[i] += 1

    for i in range(len(count)):
        if count[i] == 1:
            unique = i

    return unique


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
