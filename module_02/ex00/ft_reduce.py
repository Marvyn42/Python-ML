from functools import reduce


def ft_reduce(function_to_apply, iterable):
    try:
        if iterable is None:
            return
        lst = iterable[0]
        for elem in iterable[1:]:
            lst = function_to_apply(lst, elem)
        return lst
    except Exception as err:
        print(f"{type(err).__name__}: {err}")


lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print(ft_reduce(lambda u, v: u + v, None))
print(ft_reduce(lambda u, v: u + v, 5))
print(ft_reduce(lambda u, v: u + v, [1, 2, 3, 4]))
print(ft_reduce(lambda u, v: u + v, [1, 2, '3', 4]))
