class Foo(object):
    a = 123

    @staticmethod
    def bar(x):
        print(x)


print(Foo.bar(2))
