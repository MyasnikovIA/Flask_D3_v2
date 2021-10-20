/**
 *
 * @component
 */
D3Api.CheckBoxCtrl = new function CheckBoxCtrl()
{
    /**
     *
     * @param _dom
     */
    this.init = function(_dom)
    {
        var inp = D3Api.CheckBoxCtrl.getInput(_dom);
        D3Api.addEvent(inp, 'change', function(event){
            D3Api.setControlPropertyByDom(_dom,'value',D3Api.CheckBoxCtrl.getValue(_dom),undefined,true);
            D3Api.stopEvent(event);
        }, true);
        this.init_focus(inp);
        D3Api.BaseCtrl.initEvent(_dom,'onchange','value');
        _dom.D3Base.addEvent('onchange_property',function(property,value){
           if(property == 'value')
               _dom.D3Base.callEvent('onchange',value);
               //D3Api.execDomEvent(_dom,'onchange');
        });
    }

    /**
     *
     * @param _dom
     * @returns {*}
     */
    this.getInput = function CheckBox_getInput(_dom)
    {
        return D3Api.getChildTag(_dom,'input',0);
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setEnabled = function CheckBox_setEnabled(_dom, _value)
    {
        var input = D3Api.CheckBoxCtrl.getInput(_dom);
        //делаем активным
        if (D3Api.getBoolean(_value))
        {
            input.removeAttribute('disabled');
        }//делаем неактивным
        else
        {
            input.setAttribute('disabled','disabled');
        }
        D3Api.BaseCtrl.setEnabled(_dom, _value);
    }

    /**
     *
     * @param _dom
     * @param _value
     * @returns {*}
     */
    this.getValue = function CheckBox_getValue(_dom, _value)
    {
        var input = D3Api.CheckBoxCtrl.getInput(_dom);

        var val = (input.checked)?D3Api.getProperty(_dom,'valuechecked',true):D3Api.getProperty(_dom,'valueunchecked',false);
        //Такая строка при проверке всегда дает true
        if(val === '0')
            val = 0;
        else if(val === 'false')
            val = false;
        
        return val;
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setValue = function CheckBox_setValue(_dom, _value)
    {
        var input = D3Api.CheckBoxCtrl.getInput(_dom);

        if (_value == D3Api.getProperty(_dom,'valuechecked',true))
        {
                input.checked = true;
        }
        if (_value == D3Api.getProperty(_dom,'valueunchecked',false))
        {
                input.checked = false;
        }
    }

    /**
     *
     * @param _dom
     * @returns {*}
     */
    this.getValueChecked = function CheckBox_getValueChecked(_dom)
    {
        return D3Api.getProperty(_dom,'valuechecked',true);
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setValueChecked = function CheckBox_setValueChecked(_dom,_value)
    {
        D3Api.setProperty(_dom,'valuechecked',_value);
    }

    /**
     *
     * @param _dom
     * @returns {*}
     */
    this.getValueUnChecked = function CheckBox_getValueUnChecked(_dom)
    {
        return D3Api.getProperty(_dom,'valueunchecked',true);
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setValueUnChecked = function CheckBox_setValueUnChecked(_dom,_value)
    {
        D3Api.setProperty(_dom,'valueunchecked',_value);
    }

    /**
     *
     * @param _dom
     * @returns {*}
     */
    this.getCaption = function CheckBox_getCaption(_dom)
    {
        var cc = D3Api.getChildTag(_dom,'span',0);
        return cc.innerHTML;
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setCaption = function CheckBox_setCaption(_dom, _value)
    {
        var cc = D3Api.getChildTag(_dom,'span',0);
        cc.innerHTML = _value;
    }

    /**
     *
     * @param _dom
     * @returns {*}
     */
    this.getChecked = function CheckBox_getChecked(_dom)
    {
        var input = D3Api.getChildTag(_dom,'input',0);
        return input.checked;
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setChecked = function CheckBox_setChecked(_dom, _value)
    {
        var input = D3Api.getChildTag(_dom,'input',0);
        input.checked = _value;
    }
}
D3Api.controlsApi['CheckBox'] = new D3Api.ControlBaseProperties(D3Api.CheckBoxCtrl);
D3Api.controlsApi['CheckBox']['value']={get:D3Api.CheckBoxCtrl.getValue,set: D3Api.CheckBoxCtrl.setValue};
D3Api.controlsApi['CheckBox']['valuechecked']={get:D3Api.CheckBoxCtrl.getValueChecked,set: D3Api.CheckBoxCtrl.setValueChecked};
D3Api.controlsApi['CheckBox']['valueunchecked']={get:D3Api.CheckBoxCtrl.getValueUnChecked,set: D3Api.CheckBoxCtrl.setValueUnChecked};
D3Api.controlsApi['CheckBox']['caption']={get:D3Api.CheckBoxCtrl.getCaption,set:D3Api.CheckBoxCtrl.setCaption}
D3Api.controlsApi['CheckBox']['enabled'].set = D3Api.CheckBoxCtrl.setEnabled;
D3Api.controlsApi['CheckBox']['input']={get: D3Api.CheckBoxCtrl.getInput, type: 'dom'};
D3Api.controlsApi['CheckBox']['checked']={set:D3Api.CheckBoxCtrl.setChecked,get: D3Api.CheckBoxCtrl.getChecked};
