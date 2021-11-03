/**
 *
 * @component
 */
D3Api.ButtonCtrl = new function()
{
     /**
     *
     * @param dom
     */
    this.init = function(dom)
    {
        this.init_focus(dom);
    }

    /**
     *
     * @param _dom
     * @param _value
     * @returns {boolean}
     */
    this.setCaption = function Button_setCaption(_dom,_value)
    {
        var c = _dom.querySelector('.btn_caption');

        if (c)
        {
            c.innerHTML = _value;
            return true;
        }
        return false;
    }

    /**
     *
     * @param _dom
     * @returns {string}
     */
    this.getCaption = function Button_getCaption(_dom)
    {
        var c = _dom.querySelector('.btn_caption');
        if (c)
            return c.innerHTML;
        return '';
    }

    /**
     *
     * @param dom
     * @param e
     */
    this.CtrlKeyDown = function(dom, e)
    {
        switch (e.keyCode)
        {
            case 32: //Пробел
            case 13: //Enter
                dom.click();
                D3Api.stopEvent(e);
                break;
        }
    }
    /* Функция прорисовки popupmenu, координаты контрола берутся
     * из dom с помощью функции getBoundingClientRect  */
    /**
     *
     * @param anyDom
     * @param menuName
     */
    this.showPopupMenu = function(anyDom,menuName)
    {
        var ctrl = D3Api.getControlByDom(anyDom);
        var menu = ctrl.D3Form.getControl(menuName);
        if (menu)
        {
            var coords = {
                left: ctrl.getBoundingClientRect().left +6,
                top:  ctrl.getBoundingClientRect().bottom + 6
            };
            menu.D3Store.popupObject = ctrl || menu.D3Store.popupObject;
            D3Api.PopupMenuCtrl.show(menu,coords);
        }
    }

    this.touchstartClick = function(event,_onClickFun){
        // Необходимо решить проблему запуска кнопки на заднем фоне, если закрывают модальное окно
        // console.log(event)
        // console.log(event.changedTouches[0].target.getAttribute("name"))
        // event.changedTouches[0]
        _onClickFun && _onClickFun();
    }
}

D3Api.controlsApi['Button'] = new D3Api.ControlBaseProperties(D3Api.ButtonCtrl);
D3Api.controlsApi['Button']['caption']={get:D3Api.ButtonCtrl.getCaption,set:D3Api.ButtonCtrl.setCaption};
D3Api.controlsApi['Button']['height'] = undefined;
