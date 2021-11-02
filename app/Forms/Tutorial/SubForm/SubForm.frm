<div cmptype="Form" caption="" width="60%" height="60%">
    <cmpScript name="main_script">
        <![CDATA[
            Form.onCreate = function() {  }

            Form.onPopupPayments = function(coords, show) {
              console.log(coords, show);

            }
        ]]>
    </cmpScript>
    <cmpCheckBox name="myChek" caption="pMENU"/>
    <cmpSubForm path="Tutorial/SubForm/SubFormExtend"/>
</div>
