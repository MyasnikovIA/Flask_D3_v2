from Components.Base.BaseCtrl import *

class Label(Base):

    def __init__(self, attrs):
        super().__init__(attrs)
        self.CmpType = 'Label';
        self.tag = 'span';
        self.classCSS = []
        self.style = getDomAttrRemove('style', None, self.attrs);
        # ============== INIT Html Class =========================
        if 'class' not in self.attrs:
            self.classCSS = ['label', ]
        else:
            self.classCSS = [i for i in attrs['class'].split(" ")]
            del self.attrs['class']
        if ('label' not in self.classCSS):
            self.classCSS.append('label')
        # ========================================================

        self.format = RemoveArrKeyRtrn(self.attrs, 'format')
        self.caption = RemoveArrKeyRtrn(self.attrs, 'caption')
        self.before_caption = ArrKeyRtrn(self.attrs, 'before_caption');
        self.after_caption = ArrKeyRtrn(self.attrs, 'after_caption');
        if (self.caption == '_'):
            self.caption = '';
        self.note = ""
        note = RemoveArrKeyRtrn(self.attrs, 'note')
        if len(note) > 0:
            note_style = []
            note_offset = RemoveArrKeyRtrn(self.attrs, 'note_offset')
            if len(note_offset) > 0:
                note_style.append(f'bottom:{note_offset};')
            note_size = RemoveArrKeyRtrn(self.attrs, 'note_size')
            if len(note_size) > 0:
                note_style.append(f'font-size:{note_size};')
            note_width = RemoveArrKeyRtrn(self.attrs, 'note_width')
            if len(note_width) > 0:
                note_style.append(f'min-width:{note_width};')
            self.note = f'<span class="labelNote" style="{note_style}">{note}</span>';
        if ('format' in self.attrs) and ('onformat' not in self.attrs):
            self.attrs['onformat'] = f'D3Api.LabelCtrl.format(this, {self.attrs["format"]}, arguments[0]);'
        self.data = getDomAttrRemove('data', None, self.attrs);



    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        if len(self.classCSS) > 0:
            classCSSStr = f""" class='{' '.join(self.classCSS)}'"""
        else:
            classCSSStr = ""
        self.print(f"""
                <span  cmptype="{self.CmpType}" name="{self.name}" {classCSSStr}  {self.style} {eventsStr} {self.data}> {self.before_caption}{self.caption}{self.after_caption}{self.note} {atr}""")

        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/Label/js/Label.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/Label/css/Label.css</cssfile>")

