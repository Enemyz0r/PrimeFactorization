def prime(n):
    """ Verify if number is prime and display its prime factors

    Args: n - Number given to check.
    """

    if (n % 2 == 0):
        while(n > 1):
            n = int(n/2)
            print(n)
    else:
        print("Number is not prime!")


def main():
    prime(n)

if __name__ == '__main__':
    main()
