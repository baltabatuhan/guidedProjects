def divides_self(n):
    digits = list(str(n))

    for d in digits:
        if (d == "0") or (n % int(d) != 0):

            return False

    # if we get ti this line.the number is good:
    return True


print(divides_self(999))
