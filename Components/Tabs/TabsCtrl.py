from Components.Base.BaseCtrl import *

class Tabs(Base):
    """
    необходимо дописать этот компонент
    внутри этого класса обрабатываюстя  вложенные фрагменты <cmpTabSheet />
    """
    def __init__(self, attrs):
        super().__init__(attrs)
        self.SetSysInfo = []
        self.CmpType = 'Tabs'
        self.tag = 'div'
        self.tagCls = "</div>"
        self.text = ""
        if "text" in attrs:
            self.text = attrs["text"]
            del attrs["text"]
        self.uniqid = self.genName()

        self.headHtml=[]
        self.bodyHtml = []
    def show(self):
        eventsStr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if k[:2] == "on")
        atr = "  ".join(f'{k}="{v}"' for k, v in self.attrs.items() if not k[:2] == "on")
        self.print(f"""
        <div class="tabs">
            <input id="tab1" type="radio" name="tabs" checked>
             <label for="tab1" title="Wordpress">Wordpress</label>
            <input id="tab2" type="radio" name="tabs">
             <label for="tab2" title="Windows">Windows</label>
            <input id="tab3" type="radio" name="tabs">
            <label for="tab3" title="HTML5">HTML5</label>
            <input id="tab4" type="radio" name="tabs">
            <label for="tab4" title="CSS3">CSS3</label>
            <section id="content-tab1">
                <p> WordPress — система управления содержимым сайта с открытым исходным кодом, распространяемая под GNU GPL. Написана на PHP, в качестве базы данных использует MySQL. </p>
                <p> Сфера применения — от блогов до достаточно сложных новостных ресурсов и интернет-магазинов. Встроенная система «тем» и «плагинов» вместе с удачной архитектурой позволяет конструировать практически любые проекты. WordPress выпущен под лицензией GPL версии 2. </p>
            </section>
            <section id="content-tab2">
                <p> Microsoft Windows (произносится [майкрософт ви́ндоус]) — семейство проприетарных операционных систем корпорации Microsoft, ориентированных на применение графического интерфейса при управлении. </p>
                <p> Изначально Windows была всего лишь графической надстройкой для MS-DOS. По состоянию на март 2013 года под управлением операционных систем семейства Windows по данным ресурса NetMarketShare (Net Applications) работает около 90 % персональных компьютеров[1]. Операционные системы Windows работают на платформах x86, x86-64, IA-64, ARM. </p>
            </section>
            <section id="content-tab3">
                <p> HTML5 (англ. HyperText Markup Language, version 5) — язык для структурирования и представления содержимого всемирной паутины. Это пятая версия HTML, последняя (четвёртая) версия которого была стандартизирована в 1997 году. По состоянию на октябрь 2013 года, HTML5 ещё находится в разработке, но, фактически, является рабочим стандартом (англ. HTML Living Standard). Цель разработки HTML5 — улучшение уровня поддержки мультимедиа-технологий, сохраняя при этом удобочитаемость кода для человека и простоту анализа для парсеров. </p>
                <p> Во всемирной паутине долгое время использовались стандарты HTML 4.01 и XHTML 1.1, и веб-страницы на практике оказывались свёрстаны с использованием смеси особенностей, представленных различными спецификациями, включая спецификации программных продуктов, например веб-браузеров, а также сложившихся общеупотребительных приёмов. HTML5 был создан, как единый язык разметки, который мог бы сочетать синтаксические нормы HTML и XHTML. Он расширяет, улучшает и рационализирует разметку документов, а также добавляет единое API для сложных веб-приложений. </p>
            </section>
            <section id="content-tab4">
                <p> Спецификация CSS3 — это неоспоримое будущее в области декоративного оформления веб-страниц, и ее разработка еще далека от завершения. Большинство модулей все еще продолжает совершенствоваться и модифицироваться, и ни один браузер не поддерживает все модули. Это означает, что CSS3 испытывает такие же сложности, как и HTML5. Веб-разработчикам нужно решать, какие возможности использовать, а какие игнорировать, а также каким образом заполнить зияющие пробелы в браузерной поддержке. </p>
                <p> CSS3 не является частью спецификации HTML5. Эти два стандарта были разработаны отдельно друг от друга, разными людьми, работающими в разное время в различных местах. Но даже организация W3C призывает веб-разработчиков использовать HTML5 и CSS3 вместе, как часть одной новой волны современного веб-дизайна. </p>
            </section>
""")

        # self.print(f"""<div  cmptype="{self.CmpType}" name="{self.name}" {atr}  {eventsStr}>\n{self.text}""")
        # Добавляется при инициализации  d3main.js d3theme.css
        #self.SetSysInfo.append("<scriptfile>Components/PageControl/js/PageControl.js</scriptfile>")
        #self.SetSysInfo.append("<cssfile>Components/PageControl/css/PageControl.css</cssfile>")

        # очистка содержимого блока
        for element in self.nodeXML.findall('*'):
            self.nodeXML.remove(element)
