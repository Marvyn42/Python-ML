def ft_map(function_to_apply, iterable):
    try:
        for elem in iterable:
            yield function_to_apply(elem)
    except Exception as err:
        print(f"{type(err).__name__}: {err}")
        return None


x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))

print(ft_map(function_to_apply=None, iterable=x))
list(ft_map(function_to_apply=None, iterable=x))
