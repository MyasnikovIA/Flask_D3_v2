/**
 *
 * @component
 */
D3Api.FormCtrl = new function(){

    /**
     *
     * @param dom
     */
    this.init = function(dom)
    {
        var fd = dom.D3Form.formData.sized;
        var sized = D3Api.getBoolean(D3Api.getProperty(dom,'sized',!!fd));
        if(fd)
        {
            fd.height && D3Api.setControlPropertyByDom(dom,'height',fd.height);
            fd.width && D3Api.setControlPropertyByDom(dom,'width',fd.width);
        }
        D3Api.FormCtrl.setSized(dom,sized);
    }
    function domInsertEvent(formDom)
    {
        D3Api.FormCtrl.setSized(formDom,formDom.D3Store.sized);
    }
    function domRemoveEvent(formDom)
    {
        if(formDom.D3Store.sized)
        {
            D3Api.removeClass(formDom.D3Form.container.DOM,'formSizedContainer');
        }
        formDom.D3Store.frameDom && D3Api.removeDom(formDom.D3Store.frameDom);
    }
    function domDestroyEvent(formDom)
    {
        var cf = formDom.D3Form.container.currentForm;
        if(cf && cf.DOM && cf.DOM.D3Store && !cf.DOM.D3Store.sized)
        {
            D3Api.removeClass(formDom.D3Form.container.DOM,'formSizedContainer');
        }
        formDom.D3Store.frameDom && D3Api.removeDom(formDom.D3Store.frameDom);
    }

    /**
     *
     * @param dom
     * @returns {boolean}
     */
    this.getSized = function(dom)
    {
        return !!dom.D3Store.sized;
    }
    function setFormCaption(caption)
    {
        var cDom = D3Api.getDomByAttr(this.DOM.D3Store.frameDom,'cont','caption');

        if(cDom) {
            D3Api.addTextNode(cDom, caption, true);
            D3Api.setProperty(cDom,'title',caption);
        }

    }

    /**
     *
     * @param dom
     * @param value
     */
    this.setSized = function(dom,value)
    {
        dom.D3Store.sized = value;
        if(dom.D3Store.sized)
        {
            D3Api.addClass(dom,'formSized');
            D3Api.addClass(dom.D3Form.container.DOM,'formSizedContainer');
            !dom.D3Store.sizedUidIns && (dom.D3Store.sizedUidIns = dom.D3Form.addEvent('onform_dominsert',domInsertEvent));
            !dom.D3Store.sizedUidRem && (dom.D3Store.sizedUidRem = dom.D3Form.addEvent('onform_domremove',domRemoveEvent));
            !dom.D3Store.sizedUidDes && (dom.D3Store.sizedUidDes = dom.D3Form.addEvent('onform_destroy',domDestroyEvent));
            !dom.D3Store.sizedUidResize && (dom.D3Store.sizedUidResize = dom.D3Form.addEvent('onResize',function(){calcPos(dom)}));
            !dom.D3Store.sizedUidCaption && (dom.D3Store.sizedUidCaption = dom.D3Form.addEvent('onformcaption',setFormCaption));
            if(!dom.D3Store.frameDom)
            {
                dom.D3Store.frameDom = D3Api.createDom('<div class="formFrame"><div class="frameCaption" cont="caption"></div><div class="frameClose" cmpparse="true" onclick="close();">X</div></div>');
                dom.D3Form.parse(dom.D3Store.frameDom);
                setFormCaption.call(dom.D3Form,dom.D3Form.getFormCaption());
            }
            D3Api.insertBeforeDom(dom,dom.D3Store.frameDom);
            calcPos(dom);
        }else
        {
            D3Api.removeClass(dom,'formSized');
            D3Api.removeClass(dom.D3Form.container.DOM,'formSizedContainer');
            dom.D3Form.removeEvent('onform_dominsert',dom.D3Store.sizedUidIns);
            dom.D3Store.sizedUidIns = null;
            dom.D3Form.removeEvent('onform_domremove',dom.D3Store.sizedUidRem);
            dom.D3Store.sizedUidRem = null;
            dom.D3Form.removeEvent('onform_destroy',dom.D3Store.sizedUidDes);
            dom.D3Store.sizedUidDes = null;
            dom.D3Form.removeEvent('onResize',dom.D3Store.sizedUidResize);
            dom.D3Store.sizedUidResize = null;
            D3Api.setStyle(dom,'margin-top','0');
            dom.D3Store.frameDom && D3Api.removeDom(dom.D3Store.frameDom);
        }
    }
    function calcPos(dom)
    {
        var contSize = D3Api.getAbsoluteClientRect(dom.D3Form.container.DOM);
        var frmSize = D3Api.getAbsoluteClientRect(dom);
        var frameBorderTop = +D3Api.getStyle(dom.D3Store.frameDom,'padding-top').replace('px','');
        var frameBorderLeft = +D3Api.getStyle(dom.D3Store.frameDom,'padding-left').replace('px','');
        var mTop = (contSize.height- frmSize.height+ frameBorderTop )/2;

        D3Api.setStyle(dom,'margin-top',(mTop<frameBorderTop?frameBorderTop:mTop)+'px');

        dom.D3Store.frameDom.style.height = frmSize.height+"px";
        dom.D3Store.frameDom.style.width = frmSize.width+"px";
        dom.D3Store.frameDom.style.top = (mTop<frameBorderTop?0:(mTop-frameBorderTop))+"px";
        dom.D3Store.frameDom.style.left = (frmSize.x-frameBorderLeft)+"px";
    }

    /**
     * Проверка прав на просмотр и редактирование записи раздела
     * @param dom - форма
     * @param unit - раздел
     * @param primary - значение primary записи раздела
     * @param isView - значение режима просмотра на форме
     * @param onSuccess - callback-функция
     */
    this.checkPrivs = function(dom, unit, primary, isView, onSuccess){
        var req = {
            checkPrivs: {type: 'Form', params: {
                unitcode: unit,
                id: primary,
                is_view: isView ? true : null
            }}
        };

        D3Api.requestServer({
            url: 'request.php',
            method: 'POST',
            urlData:{action: 'privs'},
            data: {request: D3Api.JSONstringify(req)},
            contextObj:dom,
            onSuccess: function(resp) {
                r = JSON.parse(resp);
                if (r.view != "1") {
                    D3Api.notify('Сообщение сервера', 'Нет права на просмотр записи', {modal: true});
                    dom.close();
                    return false;
                }
                dom.formEditMode = r.edit == "1" ? true : false;
                if (typeof onSuccess === 'function') onSuccess.call(dom, r);
            }
        });
    }

    /* Помечаем пользовательское событие onCreate как завершенное */
        /**
     *
     * @param dom
     */
    this.setCreated = function(dom){
        dom.isCreated = true;
    }
}

D3Api.controlsApi['Form'] = new D3Api.ControlBaseProperties(D3Api.FormCtrl);
D3Api.controlsApi['Form']['sized'] = {get:D3Api.FormCtrl.getSized, set:D3Api.FormCtrl.setSized};