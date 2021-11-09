from Components.Base.BaseCtrl import *


class Tree(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Toolbar'
        self.tag = 'div'
        self.tagCls="</div></div>"
        self.styleArr = []
        if 'style' in self.attrs:
            self.styleArr.extend([i for i in attrs['style'].split(";")])
            del self.attrs['style']
        self.classCSS = []
        if 'class' in self.attrs:
            self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']
        self.caption = ""
        if 'caption' in self.attrs:
            self.caption = self.attrs['caption']
            del self.attrs['caption']
        if 'text' in self.attrs:
            del self.attrs['text']



    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        stleTxt=""
        if len(self.styleArr)>0:
            stleTxt = f""" style="{';'.join(self.styleArr)}" """
        classStr = ""
        if len(self.classCSS)>0:
            classStr = f' class="{" ".join(self.classCSS)}" '

        self.print(f"""
<div class="content">
            <div class="search">
                <input type="search" required="" placeholder="Search components" spellcheck="false">
                <i class="material-icons search-icon">search</i>
            </div>
            <p class="nothing-found message" style="display: none;">No components were found</p>
            <p class="sign-in message"></p>
            <p class="cant-reach-servers message">Could not reach server. Please check your internet connection.</p>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="list"><span class="item-folder smart-editable">
                <i class=""></i><b class="name" title="Text" onclick="onclickItemsTree(this);">Text</b><input>
            </span>
            <div class="subtree" style="display: none;">
                <span class="item"><u><span></span></u>
                    <b>Heading</b>
                </span>
                <span class="item">
                    <u><span></span></u>
                    <b>Paragraph</b>
                </span>
            </div>
            <span class="item-folder smart-editable">

                <i class="down"></i><b class="name" title="Image"  onclick="onclickItemsTree(this);" >Image</b><input></span>
                <div class="subtree" style="display: block;"><span
                        class="item"><u><span></span></u><b>Image</b></span><span class="item"><u><span></span></u><b>Picture</b></span><span
                        class="item"><u><span></span></u><b>Icon</b></span><span class="item"><u><span></span></u><b>Carousel</b></span><span
                        class="item"><u><span></span></u><b>Figure</b></span><span class="item"><u><span></span></u><b>Figcaption</b></span>
                </div>
            </div>
            <div class="suggested" style="display: none;">
                <hr>
                <div class="name"><span>Suggested</span> <span class="collapse"></span></div>
                <div class="suggested-list"></div>
            </div>
        </div>
""")

        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Tree/js/Tree.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Tree/css/Tree.css</cssfile>")
