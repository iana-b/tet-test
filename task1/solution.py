def strict(func):

    def wrapper(*args):
        annotations = func.__annotations__
        expected_types = [annotations[name] for name in annotations if name != 'return']
        if len(args) != len(expected_types):
            raise TypeError("Incorrect number of arguments")
        for arg, expected in zip(args, expected_types):
            if not isinstance(arg, expected):
                raise TypeError(f"Expected {expected.__name__}, got {type(arg).__name__}")
        return func(*args)

    return wrapper
