<div cmptype="Form"  caption="" width="60%" height="60%"  >
    <cmpScript name="main_script">
        <![CDATA[
            Form.onCreate = function() {
               // Добавить фильтр и маску в коде
               // callControlMethod('Depend', 'removeRequiredControl', 'INC_VAL', true);
               // callControlMethod('Depend', 'removeRequiredControl', 'START_VAL', true);
               // D3Api.MaskCtrl.setParam(getControl('MAX_VAL'), 'mask_type', 'number');
               // D3Api.MaskCtrl.setParam(getControl('MAX_VAL'), 'mask_template_regular', new RegExp(/^\d+$/));
            }
            Form.MySendPHP = function() {
                openD3Form('main',true)
            }
        ]]>
    </cmpScript>
    <br/>Ввести число <cmpEdit name="RANGE_BEGIN" mask_template="9999999999" mask_original="0000000000" emptyMask="true" width="100%"/>
    <br/>Ввести время<cmpEdit name="ACCEPT_TIME" mask_template="99:99" value="" width="20%" />
    <br/>Ввести дату и время DD:HH:MI:SS<cmpEdit name="L_COSTS" placeholder="DD:HH:MI:SS" width="20%"
                            mask_template="99:99:99:99" mask_original="00:00:00:00"
                            mask_check_regular="^([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])$"
                            mask_template_regular="^([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])\:([0-9][0-9])$"/>


    <br/>Ввести телефон<cmpEdit name="PHONE" data="value:CREATE_EMP_PHONE;" placeholder="+7(NNN)NNN-NN-NN" mask_original="+7(000)0000000" mask_template="+7(999)9999999" emptyMask="false"/>
    <br/>Ввести СНИЛС<cmpEdit name="CC_SNILS" width="100px"
                               mask_template_regular="^[0-9]{3}-[0-9]{3}-[0-9]{3}\s{1}[0-9]{2}$"
                               mask_check_regular="^[0-9]{3}-[0-9]{3}-[0-9]{3}\s{1}[0-9]{2}$"
                               mask_empty="true"
                               mask_original="000-000-000 00"
                               mask_template="999-999-999 99"/>
    <br/>Ввести TOKEN <cmpEdit name="ctrlTOKEN" width="50%" placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                         mask_template_regular="^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"
                         mask_check_regular="^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"/>

    <br/><cmpButton name="ButtonOk" onclick="Form.MySendPHP();" caption="Запуск"/>

    <cmpMask controls="RANGE_BEGIN;RANGE_END;ACCEPT_TIME;CC_SNILS;L_COSTS;ctrlTOKEN;PHONE"/>
    <cmpDependences required="RANGE_BEGIN;RANGE_END" depend="ButtonOk"/>
</div>
