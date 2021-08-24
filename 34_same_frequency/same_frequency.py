def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    same_frequency = True
    my_num1 = str(num1)
    my_num2 = str(num2)
    for digits1 in my_num1:
        for digits2 in my_num2:
            if my_num2.count(digits1) != my_num2.count(digits2):
                same_frequency = False
    return same_frequency
