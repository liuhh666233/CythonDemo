import dis


def fn_expressive(upper=100000):
    total = 0
    for i in range(upper):
        total += i
    return total


def fn_terse(upper=100000):
    return sum(range(upper))


print("fn_expressive:")
dis.dis(fn_expressive)
print("*" * 50)
print("fn_terse:")
dis.dis(fn_terse)
