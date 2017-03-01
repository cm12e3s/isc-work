#exercise 1
def double_it(number):
    return 2 * number

print double_it(2)
print double_it("Hello")

#exercise 2
def calc_hypo(a, b):
    hypo = ((a**2) + (b**2))**0.5
    return hypo
print calc_hypo(3, 4)

#exercise 3
def calc_hypo(a, b):
    if type(a) not in (float, int) and type(b) not in (float, int):
        return False
        print "Bad Argument"
    else:
        hypo = ((a**2) + (b**2))**0.5
        return hypo
print calc_hypo(3, 4)
calc_hypo("hello", "hello")
