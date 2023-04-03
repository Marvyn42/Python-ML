def ft_filter(function_to_apply, iterable):
    try:
        for elem in iterable:
            if function_to_apply(elem):
                yield elem
    except Exception as err:
        print(f"{type(err).__name__}: {err}")
        return


x = [1, 2, 3, 4, 5]

print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))

print(ft_filter(function_to_apply=None, iterable=x))
print(list(ft_filter(function_to_apply=None, iterable=x)))
