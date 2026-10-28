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