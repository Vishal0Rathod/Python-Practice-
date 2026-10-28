
# def my_func_Decor(func):
#     def wrapper(x, y):
#         if x < y:
#             return func(x, y)
#         return func(y, x)
#     return wrapper


# @my_func_Decor
# def OrignslFunc(x, y):
#     print(x / y)


# OrignslFunc(5, 10)


# def my_Func_Decor(func):
#     def wrapper(x, y):
#         if x > y:
#             return func(x, y)
#         x, y = y, x
#         return func(x, y)
#     return wrapper


# @my_Func_Decor
# def OriginalFun(x, y):
#     print(x / y)


# OriginalFun(5, 10)

# Create Decorator
def check_datatype(func):
    def wrapper(x, y):
        if isinstance(x, str):
            x = float(x) if "." in x else int(x)

        if isinstance(y, str):
            y = float(y) if "." in y else int(y)

        return func(x, y)

    return wrapper


@check_datatype
def devision(x, y):
    print(x / y)


devision("10", "2")
devision("10.5", "2")


def cheak_datatype(func):
    def wrapper(x,y):
        if isinstance(x, str):
         x = float(x) if "." in x else int(x)

        if isinstance(y, str):
            y = float(y) if "." in y else int(y)
            
        return func(x,y)

    return wrapper

@cheak_datatype 
def division (x,y):
    print(x/y)

    
division("10", "2")
division("10.5", "2")