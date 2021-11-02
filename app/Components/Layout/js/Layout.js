/**
 *
 * @component
 */
D3Api.LayoutCtrl = new function ()
{
    this.decimalSeparator = (1.1).toLocaleString().substring(1, 2);
    this.thousandSeparator = (1000).toLocaleString().substring(1, 2);
    /**
     *
     * @param _dom
     */
    this.init = function(_dom) {
        var inp = D3Api.EditCtrl.getInput(_dom);
        this.init_focus(inp);
        // Если Layout не расположен в модальном окне, тогда разварачиваем его на весь экран, через сеоектор "position = 'fixed'"
        //if(!_dom.parentElement.parentElement.classList.contains("WinContentBody")){
        //    _dom.style.position = "fixed";
        //}
    }
}
D3Api.controlsApi['Layout'] = new D3Api.ControlBaseProperties(D3Api.LayoutCtrl);
//D3Api.controlsApi['Button']['caption']={get:D3Api.ButtonCtrl.getCaption,set:D3Api.ButtonCtrl.setCaption};
//D3Api.controlsApi['Button']['height'] = undefined;
