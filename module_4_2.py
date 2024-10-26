def test_function(x):
    a = x ** 2
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()
    return a

print(test_function(8))
inner_function()