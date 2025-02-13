def success_test():
    assert 1 == True


def unsuccessful_test():
    assert 1 == False


success_test()
try:
    unsuccessful_test()
except AssertionError as e:
    print(f"Test failed successfully ", e)
