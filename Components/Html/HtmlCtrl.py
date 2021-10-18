

class Html:
    def __init__(self, attrs):
        pass

    def show(self):
        eventsStr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f"{k}='{v}'" for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""<{self.tag}  {atr}  {eventsStr}>""")
