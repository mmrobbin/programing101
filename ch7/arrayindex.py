def test_fnc(li):
    li[2] = 10


my_list = [51, 25, 35, 44]
print("before function call", my_list)
test_fnc(my_list)
print("after function call", my_list)