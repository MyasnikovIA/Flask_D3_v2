<div cmptype="Form"  name="MAINFORM" caption="" width="60%" height="60%" >

     <cmpScript name="MyScript">
        <![CDATA[
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
        ]]>
    </cmpScript>

     <cmpButton  caption="Tutorial" name="Button1"   onclick="openD3Form('Tutorial/main',true);" />
</div>
