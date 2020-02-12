def decorator(func):
    def wrapper(*args,**kwargs):
        func()
        print('ok, decorating...{0}'.format(func.__name__))
        print('making skin and lips beautiful now')
        func.skin='tan'
        func.lips = 'smooth'
        print('you are now beautiful and you should be called beautiful')
        func.__name__='beautiful'
        return func
    return wrapper

@decorator
def ugly():
    print('I need to be beautiful, please!')

if __name__=='__main__':
    u=ugly()
    print('you have been made... {0}'.format(u.__name__))
    print('your skin is {0} and your lips are {1}'.format(u.skin,u.lips))


    
