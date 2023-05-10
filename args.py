def fullname(firstname, lastname, middlename):
    print(f"{firstname} {middlename} {lastname}")

def div(**kwargs):
    print(kwargs)
    return kwargs['dividend']/kwargs['divisor'] * kwargs['multiplier']

#fullname("Smith", lastname="Doe", firstname="John")

print(div(dividend=10, divisor=2, multiplier = 3))

# first positional args
# then keyword args

def is_valid_age(age,max_age=100):
    if age > max_age:
        return False
    else:
        return True
    
print(is_valid_age(101))