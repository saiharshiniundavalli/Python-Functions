def fun4():
    def fun5():
        print("Hello")
    return fun5

fun = fun4() # fun = fun5
fun()

# def fun6():
#     def inner(name):
#         print(f"Hello {name}")
#     return inner
#
# l = fun6()
# l("Prabhas")


# def dec(x):
#     def inner(y):
#         print(x+y)
#         return y
#     return inner
#
# k = dec(50)
# print(k(30))
# print(k.__closure__)
# print(k.__closure__[0].cell_contents)
# k.__closure__[0].cell_contents = 100
# print(k.__closure__[0].cell_contents)
# print(k(30))

