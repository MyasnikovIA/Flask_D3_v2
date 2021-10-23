from Components.Base.BaseCtrl import *


class Expander(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Expander';
        self.tag = 'div><div  style="cursor:s-resize;height:5px;"  onmousedown="D3Api.ExpanderCtrl.moveSplit(event,\'top\')" ></div';
        self.backgroundPosition = "background-position:  4px -7px;"

        self.showClass = ""
        self.heightSrc = "20"
        if 'height' in self.attrs:
            self.heightSrc = self.attrs['height']
            self.height = f''' height="{self.attrs['height']}" '''
            del self.attrs['height']
        else:
            self.height = ''' height="" '''

        if len(re.sub("[0-9]", "", self.heightSrc)) == 0:
            self.heightSrc = f"{self.heightSrc}px"

        if 'show' in self.attrs:
            self.stylePar = f''' show="{self.attrs['show']}" '''
            if (self.attrs['show'] != 'true'):
                self.heightSrc = "20px"
                self.showClass = ""
            else:
                self.showClass = "show"
                self.backgroundPosition = "background-position:  4px 10px;"
            del self.attrs['show']
        else:
            self.stylePar = f''' show="true" '''
            self.showClass = "show"
            self.backgroundPosition = "background-position:  4px 10px;"
        if "caption" in attrs:
            self.caption = attrs["caption"]
            del attrs["caption"]
        else:
            self.caption = ""
        if "img" in attrs:
            self.img = f"""background: url('/{attrs["img"]}') no-repeat;"""
            del attrs["img"]
        else:
            self.img = ""

        self.onclick = ""
        if 'onclick' in self.attrs:
            self.onclick = self.attrs['onclick']
            del self.attrs['onclick']
        self.style = ""
        if 'style' in self.attrs:
            self.style = self.attrs['style']
            del self.attrs['style']

        self.classTxt = ""
        if 'class' in self.attrs:
            self.classTxt = self.attrs['class']
            del self.attrs['class']

    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(
            f""" <div  cmptype="{self.CmpType}" class="ctrl_expandable_vertical_dir {self.showClass}{self.classTxt}" style="height:{self.heightSrc};{self.style};" {self.height} {atr} {eventsStr} {self.stylePar}> <div class="expander_zone_click" style="{self.backgroundPosition}{self.img}" onclick="D3Api.ExpanderCtrl.toggleHeight(this,500);{self.onclick};return false">{self.caption}</div><br/> {self.text} """)
