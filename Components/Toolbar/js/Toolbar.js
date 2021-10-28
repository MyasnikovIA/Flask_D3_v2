/**
 *
 * @component
 */
D3Api.ToolbarCtrl = new function()
{
    /**
     *
     * @param dom
     */
    this.init = function(dom)
    {
        D3Api.BaseCtrl.initEvent(dom,'onchange');
        dom.D3Base.addEvent('onchange_property',function(property,value){
            if (property == 'value')
            {
                dom.D3Base.callEvent('onchange');
            };
        });
    };

    /**
     *
     * @param dom
     * @param value
     */
    this.setValue= function(dom,value)
    {
        D3Api.setProperty(dom,'value',value);
    };

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getValue= function(dom)
    {
        return D3Api.getProperty(dom,'value','');
    };

    /**
     *
     * @param dom
     * @param value
     */
    this.setUnitcode= function(dom,value)
    {
        D3Api.setProperty(dom,'unitcode',value);
    };

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getUnitcode= function(dom)
    {
        return D3Api.getProperty(dom,'unitcode','');
    };

    /**
     *
     * @param dom
     */
    this.onChangeToolbar = function (dom) {
        if(D3Api.getProperty(dom,'df','')){
            dom.D3Form.refreshDataSet('DS_toolbar_status_list_'+ D3Api.getProperty(dom,'name',''));
        };
        if(D3Api.getProperty(dom,'sttf','')){
            dom.D3Form.refreshDataSet('DS_toolbar_sttf_list_'+ D3Api.getProperty(dom,'name',''));
        };
        if(D3Api.getProperty(dom,'info','')){
            dom.D3Form.setValue('info_about_record_'+ D3Api.getProperty(dom,'name',''), dom.D3Form.getValue(D3Api.getProperty(dom,'name','')));
        };

    };

    /**
     *
     * @param dom
     */
    this.statusHistory = function (dom) {
        dom.D3Form.openForm('df/df_status_history', {
            vars: {
                identifier: dom.D3Form.getValue(D3Api.getProperty(dom,'toolbar',''))
            }
        },D3Api.MainDom);
    };

    /**
     *
     * @param dom
     * @param callback
     */
    this.onChangeDf = function (dom, callback) {
        if(!D3Api.isUserEvent())return;
        var ctrl = dom.D3Form.getControlProperty(D3Api.getProperty(dom,'name',''),'data');

        if (!ctrl.actioncode) return;
        if(ctrl.use_dialog==1){
            if(dom.modeValues){
                dom.D3Form.setValue(dom,dom.modeValues.old_value);
            }
            dom.D3Form.getValue(D3Api.getProperty(dom,'toolbar',''));
            dom.D3Form.openForm('df/df_dialog_generate', {
                request:{
                    df_flow_id:ctrl.df_flow_id,
                    actioncode:ctrl.actioncode,
                    unitcode:ctrl.unitcode,
                    id:dom.D3Form.getValue(D3Api.getProperty(dom,'toolbar',''))
                },
                modal_form: true,
                onclose: function (result) {
                    if (result) {
                        dom.D3Form.refreshDataSet('DS_toolbar_status_list_'+ D3Api.getProperty(dom,'toolbar',''), function () {
                            if (typeof callback === 'function'){
                                callback();
                            };
                        });
                    }
                }
            },D3Api.MainDom);
        }else{
            var req = {
                toolbar:{
                    type: 'Toolbar',
                    params: {
                        unitcode: ctrl.unitcode,
                        actioncode: ctrl.actioncode,
                        id: dom.D3Form.getValue(D3Api.getProperty(dom,'toolbar',''))
                    }
                }
            };
            D3Api.requestServer({
                                    url: 'request.php',
                                    method: 'POST',
                                    urlData:{
                                        action: 'toolbarDfSetStatus'
                                    },
                                    data: {
                                        request: D3Api.JSONstringify(req)
                                    },
                                    contextObj:dom,
                                    onSuccess: function(res) {
                                        if(res.match(/(?:MESSAGE_TEXT:)([\s\S]+?)(?:PG_EXCEPTION_DETAIL:|$)/)){
                                            dom.D3Form.setValue(D3Api.getProperty(dom,'name',''), '');
                                            D3Api.alert_msg(res);
                                            return;
                                        }
                                        var result = JSON.parse(res);
                                        if(result['toolbarDfSetStatus'].error){
                                            D3Api.alert_msg(result['toolbarDfSetStatus'].error);
                                            dom.D3Form.setValue(D3Api.getProperty(dom,'name',''), '');
                                            return;
                                        };
                                        dom.D3Form.refreshDataSet('DS_toolbar_status_list_'+ D3Api.getProperty(dom,'toolbar',''), function () {
                                            if (typeof callback === 'function'){
                                                callback();
                                            };
                                        });
                                    },
                                    onError: function (res) {
                                        D3Api.alert_msg(res);
                                    }
                                });
        }
    };

    /**
     *
     * @param dom
     */
    this.onChangeSttf = function (dom) {
        if(!D3Api.isUserEvent())return;
        var data = dom.D3Form.getControlProperty(D3Api.getProperty(dom,'name',''), 'data')
        if(!data.code)return;

        dom.D3Form.openForm('StatisticForms/sttf_generate', {
            request: {
                sttf_id: data.id,
                sttf_synchronous: 1
            },
            vars: {
                sttf_data: {
                    id: dom.D3Form.getValue(D3Api.getProperty(dom,'toolbar','')),
                }
            }
        }, D3Api.MainDom);
        dom.D3Form.setValue(D3Api.getProperty(dom,'name',''), '');

    }
};

D3Api.controlsApi['Toolbar'] = new D3Api.ControlBaseProperties(D3Api.ToolbarCtrl);
D3Api.controlsApi['Toolbar']['value'] = {get: D3Api.ToolbarCtrl.getValue, set: D3Api.ToolbarCtrl.setValue};
D3Api.controlsApi['Toolbar']['unitcode'] = {get: D3Api.ToolbarCtrl.getUnitcode, set: D3Api.ToolbarCtrl.setUnitcode};
D3Api.controlsApi['ToolbarItemGroup'] = new D3Api.ControlBaseProperties(D3Api.ToolbarCtrl);

