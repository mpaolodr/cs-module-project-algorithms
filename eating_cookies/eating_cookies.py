'''
Input: an integer
Returns: an integer
'''
cookie_cache = {}


def eating_cookies(n, cache=None):
    # Your code here

    if cache or not cache:
        cache = cookie_cache

    if n in cache:
        return cache[n]

    if n == 0:
        return 1

    if n <= 2:
        return n

    else:

        value = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

        cache[n] = value

        return value


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
