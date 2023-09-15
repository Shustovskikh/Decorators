import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(f"{datetime.datetime.now()} - вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}, возвращаемое значение: {result}\n")
            return result
        return new_function
    return __logger