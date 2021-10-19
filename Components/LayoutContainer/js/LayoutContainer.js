/**
 *
 * @component
 */
D3Api.LayoutContainerCtrl = new function ()
{

    /**
     *
     * @param _dom
     */
    this.init = function (dom) {
        D3Api.BaseCtrl.initEvent(dom, 'onformat');
    };
}
D3Api.controlsApi['LayoutContainer'] = new D3Api.ControlBaseProperties(D3Api.LayoutContainerCtrl);
//D3Api.controlsApi['Button']['caption']={get:D3Api.ButtonCtrl.getCaption,set:D3Api.ButtonCtrl.setCaption};
//D3Api.controlsApi['Button']['height'] = undefined;
