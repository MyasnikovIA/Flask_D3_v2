<div cmptype="Form" onshow="Form.onCreate();">
    <cmpScript>
        <![CDATA[
              Form.onCreate = function() {
                   this['_DOM_'].onresize = function() {
                        setTimeout(function () {
                            Form.SetContentMenu();
                        }, 500);
                   }
                   /*
                   D3Api.addEvent(this['_DOM_'], 'resize', function (_event) {
                        setTimeout(function () {
                            Form.SetContentMenu();
                        }, 500);
                        Form.bodyCoordinate = D3Api.getAbsoluteClientRect(document.body);
                    })
                    */
                   console.log(this['_DOM_'])
                   console.log(this)
                   Form.SetContentMenu();
              }

             Form.SetContentMenu = function () {
                var height = 60;
                var menuContext = getControl('menuContext');
                var otherButton = getControl('OtherButton');
                otherButton.style.disolay="none";
                var oldWidth = menuContext.offsetWidth;
                console.log("menuContext.offsetWidth",menuContext.offsetWidth );
                //console.log(menuContext);
                //console.log(menuContext.offsetHeight );
                var children = menuContext.childNodes;
                var summ = 0;
                for (var i = 0; i < children.length; ++i) {
                    if (typeof children[i]['getAttribute'] !=='function') continue;
                    rect = children[i].getBoundingClientRect()
                    summ+=rect.width ;
                    if ("OtherButton" !== children[i].getAttribute("name")) {
                        if (summ > (oldWidth-rect.width-rect.width)) {
                           otherButton.style.disolay="";
                           children[i].style.display="none"
                        }
                    }
                }

/*
<div class="item active" cmptype="PopupItem" name="3cf4083437d411ecb1e1001a7dda7108" title="" rootitem="true" caption="Отчет 1" id="d3ctrleec879b79a29553b89b2e5be3ed2745c">
        <table style="width:100%" cmpparse="PopupItem" cont="item" onclick=";D3Api.PopupItemCtrl.clickItem(this);" onmouseover=";D3Api.PopupItemCtrl.hoverItem(this);">
            <tbody>
            <tr>
                <td class="itemCaption">
                    <img src="/Components/PopupMenu/images/Icons/delete.png" cont="itemIcon" class="itemIcon"><span cont="itemCaption">Отчет 1</span>
                </td>
                <td class="caret"></td>
            </tr>
            </tbody>
        </table>
</div>
*/
                 /*
                 console.log("!menuContext.offsetWidth",menuContext.offsetWidth );
                console.log("!summ",summ);

                for (var i = 0; i < children.length; ++i) {
                    if (typeof children[i]['getAttribute'] !=='function') continue;
                    children[i].style.display=""
                    var newWidth =menuContext.offsetWidth;
                    console.log(newWidth,oldWidth, (oldWidth !== newWidth))


                    //if (oldWidth !== newWidth) {
                    //   oldWidth = newWidth;
                    //   children[i].style.display=""
                   // }
                }
*/

                /*
                setVisible('OtherMenu', false);
                var oldWidth = getControl('menuContext').offsetWidth;
                if (Form.StructMenu.length > 0) {
                    for (var i = 0; i < Form.StructMenu[0].childs.length; i++) {
                        var clone = getRepeater('rptName').addClone(Form.StructMenu[0].childs[i]);
                        var newWidth = getControl('menuContext').offsetWidth;
                        if (oldWidth !== newWidth) {
                            oldWidth = newWidth;
                        } else {
                            setVisible('OtherMenu', true);
                            getRepeater('rptName').removeClone(clone);
                            break;
                        }
                    }
                    for (; getControl('menuContext').offsetHeight >= height;) {
                        setVisible('OtherMenu', true);
                        var clones = getRepeater('rptName').clones();
                        if (clones.length > 0) {
                            getRepeater('rptName').removeClone(clones[clones.length - 1]);
                        }
                    }
                }
                // Form.isCreateMenu = false;
                // Form.rebuildMainMenu();
                */
        };
        ]]>
    </cmpScript>
     <div>
        <div style="display:inline-block; " cmptype="tmp" name="menuContext" title="dasdasdas" >
            <cmpButton name="reports_Ctrl1" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl2" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl3" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl4" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl5" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl6" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl7" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl8" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl9" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl10" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl11" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl12" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl13" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl14" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl15" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl16" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl17" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="reports_Ctrl18" popupmenu="p_reports_list_Ctrl" caption="Отчеты" width="50px" />
            <cmpButton name="OtherButton"    popupmenu="OtherMenu" caption="Еще..." width="50px"  />
            <cmpPopupMenu name="p_reports_list_Ctrl">
                 <cmpPopupItem caption="Отчет 1"    std_icon="delete"/>
                 <cmpPopupItem caption="Отчет 2"    std_icon="edit"/>
                 <cmpPopupItem caption="группа">
                 </cmpPopupItem>
            </cmpPopupMenu>
            <cmpPopupMenu name="OtherMenu">
           </cmpPopupMenu>
        </div>
    </div>
</div>
