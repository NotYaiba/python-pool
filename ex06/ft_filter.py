def ft_filter(function, iterable):
    """
    ft_filter(function, iterable)

    Return a list of items from iterable for which function(item) is truthy.
    Unlike built-in filter, this returns a list.
"""
    return [x for x in iterable if function(x)]
