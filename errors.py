try:
    print(div(1, 0))
except Exception as e:
    print('Define Function before calling it')
print('Program continues')

def div(a, b):
    try:
        a = [1, 2, 3]
        print('adas')
        print(25+56)
        if b==0:
            raise Exception('Division by zero, you idiot')
        return a[2]/0
    except ZeroDivisionError:
        print('oops, division by zero')
    except TypeError:
        print('oops, Invalid Type')
        return 0
    except Exception as e:
        print(e)
        return 0
    

print(div(1, 0))

