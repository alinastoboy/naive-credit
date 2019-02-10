def is_creditable(age, salary):
    """


    >>> is_creditable(20, 40_000)
    False


    """
    min_age = 21
    max_age = 60
    min_salary = 30_000
    if age < min_age:
        return False

    if age > max_age:
        return False

    if salary < min_salary:
        return False

    return True

