<div cmptype="Form"  caption="" width="60%" height="60%"  >
    <!--
        openD3Form('Tutorial/Dependences/Dependences')
        D3Api.showForm('Tutorial/Dependences/Dependences', $(".D3MainContainer").get(0), {history: false});


    <br  /><div  name="RANGE_BEGIN" mask_template="9999999999" mask_original="0000000000" emptymask="true" cmptype="Edit" title=""  class="ctrl_edit editControl box-sizing-force"  style=";width: 100%;"><input cmpparse="Edit" type="text" value="" onchange="D3Api.stopEvent();"/></div>
    <br  /><div  name="RANGE_END" mask_template="9999999999" mask_original="0000000000" emptymask="true" cmptype="Edit" title=""  class="ctrl_edit editControl box-sizing-force"  style=";width: 100%;"><input cmpparse="Edit" type="text" value="" onchange="D3Api.stopEvent();"/></div>
    <br  /><div  onclick="Form.MySendPHP();"           name="ButtonOk" cmptype="Button" title=""  tabindex="0" class="ctrl_button box-sizing-force" style="">

                        <div class="btn_caption btn_center minwidth" >Запуск</div>

                    </div>

    <div  cmptype="Mask"   name="cmp617433889cde4"   controls="RANGE_BEGIN;RANGE_END"  style="display:none"></div>
	<div  cmptype="Dependences"   name="cmp61743388a03db"   required="RANGE_BEGIN;RANGE_END"   depend="ButtonOk"    style="display:none"></div>


    -->
<!--
    <br  /><div  name="RANGE_BEGIN" mask_template="9999999999" mask_original="0000000000" emptymask="true" cmptype="Edit" title=""  class="ctrl_edit editControl box-sizing-force"  style=";width: 100%;"><input cmpparse="Edit" type="text" value="" onchange="D3Api.stopEvent();"/></div>
    <br  /><div  name="RANGE_END" mask_template="9999999999" mask_original="0000000000" emptymask="true" cmptype="Edit" title=""  class="ctrl_edit editControl box-sizing-force"  style=";width: 100%;"><input cmpparse="Edit" type="text" value="" onchange="D3Api.stopEvent();"/></div>
    <br  /><div  onclick="Form.MySendPHP();"           name="ButtonOk" cmptype="Button" title=""  tabindex="0" class="ctrl_button box-sizing-force" style="">

                        <div class="btn_caption btn_center minwidth" >Запуск</div>

                    </div>
-->


    <cmpScript name="main_script">
        <![CDATA[
            Form.onCreate = function() {
            }
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
        ]]>
    </cmpScript>
    <br/><cmpEdit name="RANGE_BEGIN" mask_template="9999999999" mask_original="0000000000" emptyMask="true" width="100%"/>
    <br/><cmpEdit name="RANGE_END" mask_template="9999999999" mask_original="0000000000" emptyMask="true" width="100%"/>
    <br/><cmpButton name="ButtonOk" onclick="Form.MySendPHP();" caption="Запуск"/>

    <cmpMask controls="RANGE_BEGIN;RANGE_END"/>
    <cmpDependences required="RANGE_BEGIN;RANGE_END" depend="ButtonOk"/>
    <!-- ctrl_disable -->



</div>
