
routs= {}


def rout(path):
    print(path)
    def wrapper(f):
        print(f)
        routs[path] = f
        
        
    return wrapper


@rout('/')
def foo1():
    print(1)

@rout('/cat')
def foo2():
    print(2)

adr = '/cat'
routs[adr]()

