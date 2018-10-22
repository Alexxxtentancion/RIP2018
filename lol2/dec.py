def print_result(foo):
    def decorated(*args,**kwargs):
        print(foo.__name__)
        res = foo(*args)
        if isinstance(res, list):
            print('\n'.join(list(map(str, res))))
        elif isinstance(res, dict):
            print('\n'.join(["{} = {}".format(key, value) for key, value in res.items()]))
        else:
            print(res)
        return res

    return decorated


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


test_1()
test_2()
test_3()
test_4()
