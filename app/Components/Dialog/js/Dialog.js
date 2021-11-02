/**
 *
 * @component
 */
D3Api.DialogCtrl = new function()
{

    /**
     *
     * @param dom
     */
    this.init = function(dom)
    {
    };

    /**
     *
     * @param dom
     * @param value
     */
    this.setValue= function(dom,value)
    {
        var ctrlName = D3Api.getProperty(dom,'name','');
        var domTextControl = D3Api.getDomByName(dom, ctrlName +'_text');
        D3Api.LabelCtrl.setCaption(domTextControl, value);
    };

    /**
     *
     * @param dom
     */
    this.getValue= function(dom)
    {
        var ctrlName = D3Api.getProperty(dom,'name','');
        var domTextControl = D3Api.getDomByName(dom, ctrlName +'_text');
        return D3Api.LabelCtrl.getCaption(domTextControl);
    };

    /**
     *
     * @param dom
     * @param value
     * @returns {string}
     */
    this.setVisible = function (dom, value) {
        var ctrlName = D3Api.getProperty(dom,'name','');
        if(!ctrlName)return 'Компонент с именем ' + ctrlName + ' не найден!';
        if(value){
            D3Api.addClass(D3Api.getDomByName(D3Api.MainDom, ctrlName), "active");
            D3Api.addClass(D3Api.getDomByName(D3Api.MainDom, ctrlName + "_background"), "active");
        }else {
            D3Api.removeClass(D3Api.getDomByName(D3Api.MainDom, ctrlName), "active");
            D3Api.removeClass(D3Api.getDomByName(D3Api.MainDom, ctrlName + "_background"), "active");
        };
    };

    /**
     *
     * @param dom
     * @param value
     */
    this.setCaption = function (dom, value) {
        var ctrlName = D3Api.getProperty(dom,'name','');
        var domTextControl = D3Api.getDomByName(dom, ctrlName +'_caption');
        D3Api.LabelCtrl.setCaption(domTextControl, value);
    };

    /**
     *
     */
    this.getCaption = function (dom) {
        var ctrlName = D3Api.getProperty(dom,'name','');
        var domTextControl = D3Api.getDomByName(dom, ctrlName +'_caption');
        return D3Api.LabelCtrl.getCaption(domTextControl);
    };
};

D3Api.controlsApi['Dialog'] = new D3Api.ControlBaseProperties(D3Api.DialogCtrl);
D3Api.controlsApi['Dialog']['value'] = {get: D3Api.DialogCtrl.getValue, set: D3Api.DialogCtrl.setValue};
D3Api.controlsApi['Dialog']['visible'] = {set: D3Api.DialogCtrl.setVisible};
D3Api.controlsApi['Dialog']['caption'] = {get:D3Api.DialogCtrl.getCaption, set: D3Api.DialogCtrl.setCaption};