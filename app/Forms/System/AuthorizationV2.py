class ExecModuleEny:
    def __init__(self):
        pass

    def test(self, attrs):
        print(attrs)
        attrs["sdfsdfsd"] = 1111
        return attrs
