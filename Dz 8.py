def robust_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    return wrapper

@robust_calculator
def calculate(expression):
    return eval(expression)
if __name__ == "__main__":
    expression1 = "2 + 2"
    expression2 = "10 / 0"
    expression3 = "10 ** 3"
    result1 = calculate(expression1)
    result2 = calculate(expression2)
    result3 = calculate(expression3)

    print(f"Результат 1: {result1}")
    print(f"Результат 2: {result2}")
    print(f"Результат 3: {result3}")