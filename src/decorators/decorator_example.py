def my_decorator(number):
    def actual_decorator(f):
        def wrapper(*args, **kargs):
            for i in range(number):
                print(f"Before function")
            f(*args, **kargs)
            for i in range(number):
                print("After function")

        return wrapper
    return actual_decorator


@my_decorator(4)
def execute_task(t):
    print("Executing task "+str(t))


execute_task(2)
