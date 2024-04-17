def calculate_equation(equation):
    return eval(equation)


def add_function_info(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        params = ', '.join([str(arg) for arg in args] + [f"{key}={val}" for key, val in kwargs.items()])
        print(f"Function: {func_name}, Parameters: {params}, Result: {result}")
        return result

    return wrapper


@add_function_info
def calculate_equation(equation):
    return eval(equation)


equation = "2 + 3 * 5"
result = calculate_equation(equation)
print("Result:", result)
