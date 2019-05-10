
def add_number(num1, num2):
    try:
        return num1 + num2
    except:
        return 'Invalid input'
# print(add_number(1,'KV'))


def args_example(*num):
    print(num)
    return sum(num)
# print(args_example(1,3,4 ))

def kw_args_example(**arg):
    print(arg)

(kw_args_example(name = 'kv', age = '6 days', address = 'KV bhavan'))
