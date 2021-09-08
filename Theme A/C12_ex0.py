li0 = [1, 20, 2.3, "pop"]
li1 = [1, 20, 2.3, "pop"]

def my_pop(li):
    if len(li) == 0:
        raise IndexError("pop from empty list")
    val_pop = li[-1]
    del li[-1]
    return val_pop

ret_native = li0.pop()
ret_custom = my_pop(li1)

print(ret_native)
print(ret_custom)
print(li0)
print(li1)

ret_native = li0.pop()
ret_custom = my_pop(li1)

print(ret_native)
print(ret_custom)
print(li0)
print(li1)

ret_native = li0.pop()
ret_custom = my_pop(li1)

print(ret_native)
print(ret_custom)
print(li0)
print(li1)

ret_native = li0.pop()
ret_custom = my_pop(li1)

print(ret_native)
print(ret_custom)
print(li0)
print(li1)

#ret_native = li0.pop()
ret_custom = my_pop(li1)

print(ret_native)
print(ret_custom)
print(li0)
print(li1)
