from Components.Base.BaseCtrl import *

class ComboBox(Base):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'ComboBox'
        self.tag = 'table></div></div></div'
        self.style = getDomAttrRemove('style', None, self.attrs);
        # ============== INIT Html Class =========================
        self.classCSS = ['form-control ctrl_combobox editControl box-sizing-force']
        if 'class' not in self.attrs:
            self.classCSS = self.classCSS.extend([i for i in attrs['class'].split(" ")])
            del self.attrs['class']
        # ========================================================

        self.items_dataset = ""
        if 'dataset' in self.attrs:
            self.items_dataset = f""" items_dataset="{self.attrs["dataset"]}" """
            del self.attrs["dataset"]


        if "repeatername"  in self.attrs:
            self.items_repeatername = f' items_repeatername="{self.attrs["repeatername"]}" '
            del self.attrs["repeatername"]
        else:
            self.items_repeatername = f' items_repeatername="rep_{self.genName()}" '
        if not "id" in self.attrs:
            self.id = f"d3ctrl{self.genName()}"
        else:
            self.id = self.attrs["id"]
            del self.attrs["id"]

        if not "keyvalue" in self.attrs:
            self.keyvalue = ' keyvalue="" '
        else:
            self.keyvalue = f' keyvalue="{self.attrs["keyvalue"]}" '
            del self.attrs["keyvalue"]

        if not "onchange" in self.attrs:
            self.onchange = ''
        else:
            self.onchange = self.attrs["onchange"]
            del self.attrs["onchange"]

        if not "onclick" in self.attrs:
            self.onclick = ''
        else:
            self.onclick = self.attrs["onclick"]
            del self.attrs["onclick"]

        if not "onkeydown" in self.attrs:
            self.onkeydown = ''
        else:
            self.onkeydown = self.attrs["onkeydown"]
            del self.attrs["onkeydown"]

        if not "onkeyup" in self.attrs:
            self.onkeyup = ''
        else:
            self.onkeyup = self.attrs["onkeyup"]
            del self.attrs["onkeyup"]

        if not "onpostclone" in self.attrs:
            self.onpostclone = ''
        else:
            self.onpostclone = self.attrs["onpostclone"]
            del self.attrs["onpostclone"]
        if not "oncreate" in self.attrs:
            self.oncreate = ''
        else:
            self.oncreate = self.attrs["oncreate"]
            del self.attrs["oncreate"]
        if not "zindex" in self.attrs:
            self.zindex = f'style="display: none; min-width: 181px; width: 181px; left: 50px; top: 483px; height: 112px;"'
        else:
            self.zindex = f'style="z-index:{self.attrs["zindex"]}"'
            del self.attrs["zindex"]



    def show(self):
        if len(self.readonly)>0:
            self.readonly = ' readonly="readonly" '
        if len(self.placeholder)>0:
            self.placeholder = f' placeholder="{self.placeholder}" '
        if len(self.disabled)>0:
            self.disabled = ' disabled="true" '
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""
                      <div name="{self.name}" cmptype="{self.CmpType}" title="{self.title}" oncreate="{self.oncreate}" onpostclone="D3Api.ComboBoxCtrl.postClone(this);{self.onpostclone}" class="{' '.join(self.classCSS)}" {self.items_repeatername} dynitems="true" 
                       {self.items_dataset}  id="{self.id}"  {self.keyvalue} {self.style} {atr} >
                          <div class="cmbb-input">
                               <input cmpparse="{self.CmpType}" type="text"
                                 onchange="D3Api.stopEvent();{self.onchange}" 
                                 onclick="D3Api.ComboBoxCtrl.downClick(this);{self.onclick}"
                                 onkeydown="D3Api.ComboBoxCtrl.keyDownInput(this);{self.onkeydown}"
                                 onkeyup="D3Api.ComboBoxCtrl.keyUpInput(this);{self.onkeyup}" {self.disabled}/>
                         </div>
                       <div cmpparse="{self.CmpType}" class="cmbb-button" onclick="D3Api.ComboBoxCtrl.downClick(this);" title="Выбрать из списка">
                       </div><div cmptype="Base" name="ComboItemsList_{self.name}" id="d3ctrl{self.genName()}"><div cmptype="ComboBoxDL" cont="cmbbdroplist" class="cmbb-droplist" id="d3ctrl{self.genName()}" {self.zindex} >
                       <table>
""")


"""
<div name="IS_MAIN" cmptype="ComboBox" title="" oncreate="" onpostclone="D3Api.ComboBoxCtrl.postClone(this);"
     class="ctrl_combobox editControl box-sizing-force" style=";width: 100%;">
    <div class="cmbb-input"><input cmpparse="ComboBox" onchange="D3Api.stopEvent()" type="text"
                                   onclick="D3Api.ComboBoxCtrl.downClick(this);"
                                   onkeydown="D3Api.ComboBoxCtrl.keyDownInput(this);"
                                   onkeyup="D3Api.ComboBoxCtrl.keyUpInput(this);"/></div>
    <div cmpparse="ComboBox" class="cmbb-button" onclick="D3Api.ComboBoxCtrl.downClick(this);"
         title="Выбрать из списка"></div>
    <div cmptype="Base" name="ComboItemsList_IS_MAIN">
        <div cmptype="ComboBoxDL" cont="cmbbdroplist" class="cmbb-droplist">
            <table>

                <tr cmptype="ComboItem" name="cmp5f7d8713a7528" comboboxname="IS_MAIN">
                    <td>
                        <div class="item_block">
                            <span class="btnOC" comboboxname="IS_MAIN"></span>
                            <span cont="itemcaption"></span>
                        </div>

                    </td>
                </tr>


                <tr cmptype="ComboItem" name="cmp5f7d8713a79e4" comboboxname="IS_MAIN" value="1">
                    <td>
                        <div class="item_block">
                            <span class="btnOC" comboboxname="IS_MAIN"></span>
                            <span cont="itemcaption">Основное вещество</span>
                        </div>

                    </td>
                </tr>


                <tr cmptype="ComboItem" name="cmp5f7d8713a7e9f" comboboxname="IS_MAIN" value="0">
                    <td>
                        <div class="item_block">
                            <span class="btnOC" comboboxname="IS_MAIN"></span>
                            <span cont="itemcaption">Дополнительное вещество</span>
                        </div>

                    </td>
                </tr>

            </table>
        </div>
    </div>
</div>
    """
