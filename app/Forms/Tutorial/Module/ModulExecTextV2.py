"""
Пример реализации класса для вызова его из  тэга cmpModule
"""
class ExecModuleEny:
    def __init__(self):
        print("init")
        pass

    def test(self, attrs):
        print(attrs)
        attrs["sdfsdfsd"] = 1111
        return attrs
