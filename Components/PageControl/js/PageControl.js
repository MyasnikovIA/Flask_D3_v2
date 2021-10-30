/**
 *
 * @component
 */
D3Api.PageControlCtrl = new function()
{
    /**
     *
     * @param dom
     */
    this.init = function PageControlCreate(dom)
    {
        this.init_focus(dom);
        dom.D3Store.uniqId = D3Api.getProperty(dom,'uniqid','');
        D3Api.PageControlCtrl.setActiveIndex(dom,D3Api.getProperty(dom,'activeindex',0));
        D3Api.BaseCtrl.initEvent(dom,'onpagechange','showIndex,hideIndex');
        D3Api.BaseCtrl.initEvent(dom,'onpageshow','pageIndex');
        D3Api.BaseCtrl.initEvent(dom,'onpagehide','pageIndex');
        dom.D3Form.addEvent('onResize',function(){D3Api.PageControlCtrl.resize(dom)});
        dom.D3Store.ShowIndex=0;
        dom.D3Store.mode = dom.getAttribute('mode');
        D3Api.PageControlCtrl.CalckTabSheetHead(dom);
        D3Api.PageControlCtrl.resize(dom);
    }
    
    /**
     *
     * @param dom
     * @constructor
     */
    this.CalckTabSheetHead= function(dom)
    {
        if (dom.D3Store.mode === 'vertical') return;
        dom.D3Store.HeadWidth=0;
        var ul_dom= D3Api.getDomByAttr(dom, 'cont', 'PageControl_head');
        dom.D3Store.TabSheetHeads = D3Api.getAllDomBy(ul_dom, '[cmptype="TabSheet"]');
        for( var i=0;i<dom.D3Store.TabSheetHeads.length;i++)
        {
           if(D3Api.getControlPropertyByDom(dom.D3Store.TabSheetHeads[i],'visible'))
             dom.D3Store.HeadWidth=dom.D3Store.HeadWidth+dom.D3Store.TabSheetHeads[i].offsetWidth;
        }
    }
    
    /**
     *
     * @param dom
     */
    this.resize = function(dom) {
        if (dom.D3Store.mode === 'vertical') return;

        var ul_dom = D3Api.getDomByAttr(dom, 'cont', 'PageControl_head');
        var scroll_next = D3Api.getDomByAttr(dom, 'cont', 'ScrollNext');
        var scroll_prior = D3Api.getDomByAttr(dom, 'cont', 'ScrollPrior');
        var div_dom = D3Api.getDomByAttr(dom, 'cont', 'div_ul');
        if (div_dom.offsetWidth < dom.D3Store.HeadWidth) {
            if ((-1 * ul_dom.offsetLeft + div_dom.offsetWidth) < dom.D3Store.HeadWidth) {
                D3Api.showDomBlock(scroll_next);
            } else {
                D3Api.hideDom(scroll_next);
            }

            if (ul_dom.offsetLeft == '0') {
                D3Api.hideDom(scroll_prior);
            } else {
                D3Api.showDomBlock(scroll_prior);
            }
        } else {
            D3Api.hideDom(scroll_next);
            D3Api.hideDom(scroll_prior);
            D3Api.setStyle(ul_dom, 'left', '0');
            dom.D3Store.ShowIndex = 0;
        }
    };
    
    /**
     *
     * @param dom
     * @constructor
     */
    this.ScrollNext = function(dom)
    {
         var page_control=D3Api.getControlByDom(dom, 'PageControl');   
         var ul_dom=  D3Api.getDomByAttr(page_control, 'cont', 'PageControl_head');
         var div_dom= D3Api.getDomByAttr(page_control, 'cont', 'div_ul');
         var scroll_lenght=0;
         if (page_control.D3Store.ShowIndex==0) scroll_lenght=-20;
         while ((scroll_lenght<Math.round(div_dom.offsetWidth/2))&&(page_control.D3Store.ShowIndex<page_control.D3Store.TabSheetHeads.length))
             {
                 if(D3Api.getControlPropertyByDom(page_control.D3Store.TabSheetHeads[page_control.D3Store.ShowIndex],'visible'))
                    scroll_lenght=scroll_lenght+page_control.D3Store.TabSheetHeads[page_control.D3Store.ShowIndex].offsetWidth;
                 page_control.D3Store.ShowIndex++;
             }
         D3Api.setStyle(ul_dom,'left',(ul_dom.offsetLeft-scroll_lenght)+'px');
         D3Api.PageControlCtrl.resize(page_control);
    }

    /**
     *
     * @param dom
     * @constructor
     */
    this.ScrollPrior = function(dom)
    {
         var page_control=D3Api.getControlByDom(dom, 'PageControl');   
         var ul_dom=  D3Api.getDomByAttr(page_control, 'cont', 'PageControl_head');
         var div_dom= D3Api.getDomByAttr(page_control, 'cont', 'div_ul');
         var scroll_lenght=0;     
         while ((scroll_lenght<Math.round(div_dom.offsetWidth/2))&&(page_control.D3Store.ShowIndex>0))
             {
                 page_control.D3Store.ShowIndex--;
                 if(D3Api.getControlPropertyByDom(page_control.D3Store.TabSheetHeads[page_control.D3Store.ShowIndex],'visible'))
                    scroll_lenght=scroll_lenght+page_control.D3Store.TabSheetHeads[page_control.D3Store.ShowIndex].offsetWidth;
             }
         if (page_control.D3Store.ShowIndex==0) 
             D3Api.setStyle(ul_dom,'left','0');
         else
             D3Api.setStyle(ul_dom,'left',(ul_dom.offsetLeft+scroll_lenght)+'px');
         D3Api.PageControlCtrl.resize(page_control);
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getActiveIndex = function(dom)
    {
        return dom.D3Store.activeIndex;
    }

    /**
     *
     * @param dom
     * @param index
     */
    this.setActiveIndex = function(dom,index)
    {
        index = +index;
        if (index === dom.D3Store.activeIndex)
            return;
        if (dom.D3Store.activeIndex != undefined)
        {
            var tab = D3Api.getDomBy(dom, '.tab'+dom.D3Store.activeIndex+'_'+dom.D3Store.uniqId);
            D3Api.removeClass(tab, 'active');
            var page = D3Api.getDomBy(dom, '.page'+dom.D3Store.activeIndex+'_'+dom.D3Store.uniqId);
            dom.D3Base.callEvent('onpagehide', dom.D3Store.activeIndex);
            D3Api.hideDom(page);
        }
        tab = D3Api.getDomBy(dom, '.tab'+index+'_'+dom.D3Store.uniqId);
        D3Api.addClass(tab, 'active');
        page = D3Api.getDomBy(dom, '.page'+index+'_'+dom.D3Store.uniqId);
        D3Api.showDomBlock(page);
        dom.D3Base.callEvent('onpageshow', index);
        var hInd = dom.D3Store.activeIndex;
        dom.D3Store.activeIndex = index;
        dom.D3Base.callEvent('onpagechange',index,hInd);
        D3Api.resize();
    }

    /**
     *
     * @param dom
     */
    this.showTab = function showTab(dom)
    {
        var pc = D3Api.getControlByDom(dom, 'PageControl');
        var index = D3Api.getProperty(dom, 'pageindex', 0);
        this.setActiveIndex(pc,index); 
    }

    /**
     *
     * @param dom
     * @param index
     * @returns {*}
     */
    this.getPageByIndex = function(dom,index)
    {
        index = index || dom.D3Store.activeIndex;
        var page = D3Api.getDomBy(dom, '.page'+index);
        if (!page)
            D3Api.debug_msg('Закладка с индесом '+index+' не найдена.');
        return page;
    }

    /**
     *
     * @param dom
     * @param index
     * @returns {*}
     */
    this.getTabByIndex = function(dom,index)
    {
        if(D3Api.isUndefined(index))
            index = dom.D3Store.activeIndex;

        var tab = D3Api.getDomByAttr(dom, 'pageindex', index);
        if (!tab)
            D3Api.debug_msg('Кнопка закладки с индесом '+index+' не найдена.');
        return tab;
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
            case 33: //PageUp
            case 38: //стрелка вверх
            case 37: //стрелка влево
                var activeIndex = D3Api.PageControlCtrl.getActiveIndex(dom);
                var flag = false;

                while (!flag)
                {
                    var nextTab = D3Api.PageControlCtrl.getTabByIndex(dom, activeIndex-1);

                    if(nextTab)
                    {
                        if(D3Api.BaseCtrl.getVisible(nextTab))
                        {
                            D3Api.PageControlCtrl.showTab(nextTab);
                            flag = true;
                        }
                    }
                    else
                        flag = true;

                    activeIndex = nextTab;
                }
                D3Api.stopEvent(e);
                break;
            case 34: //PageDown
            case 40: //стрелка вниз
            case 39: //стрелка вправо
                var activeIndex = D3Api.PageControlCtrl.getActiveIndex(dom);
                var flag = false;

                while (!flag)
                {
                    var nextTab = D3Api.PageControlCtrl.getTabByIndex(dom, activeIndex+1);

                    if(nextTab)
                    {
                        if(D3Api.BaseCtrl.getVisible(nextTab))
                        {
                            D3Api.PageControlCtrl.showTab(nextTab);
                            flag = true;
                        }
                    }
                    else
                        flag = true;

                    activeIndex = nextTab;
                }
                D3Api.stopEvent(e);
                break;
        }
    }
}
D3Api.controlsApi['PageControl'] = new D3Api.ControlBaseProperties(D3Api.PageControlCtrl);
D3Api.controlsApi['PageControl']['activeIndex']={get:D3Api.PageControlCtrl.getActiveIndex,set:D3Api.PageControlCtrl.setActiveIndex};

/**
 *
 * @component
 */
D3Api.TabSheetCtrl = new function()
{

    /**
     *
     * @param dom
     * @param value
     */
    this.setVisible = function(dom, value)
    {
        D3Api.BaseCtrl.setVisible(dom,value);
        
        var pc = D3Api.getControlByDom(dom, 'PageControl');
        var ind = D3Api.getProperty(dom, 'pageindex', false);
        var page = D3Api.getDomByAttr(pc, 'cont', 'page'+ind+'_'+pc.D3Store.uniqId);
        
        if(!page)
            return;
        D3Api.BaseCtrl.setVisible(page,value);
        D3Api.PageControlCtrl.CalckTabSheetHead(pc);
        D3Api.PageControlCtrl.resize(pc);
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getIndex = function(dom)
    {
        return D3Api.getProperty(dom, 'pageindex', null);
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getCaption = function(dom)
    {
        var cc = D3Api.getDomByAttr(dom, 'cont', 'tabcaption');
        return D3Api.getTextContent(cc);
    }

    /**
     *
     * @param dom
     * @param value
     * @returns {boolean}
     */
    this.setCaption = function(dom,value)
    {
        var cc = D3Api.getDomByAttr(dom, 'cont', 'tabcaption');
        D3Api.addTextNode(cc, value, true);
        return true;
    }
}

D3Api.controlsApi['TabSheet'] = new D3Api.ControlBaseProperties(D3Api.TabSheetCtrl);
D3Api.controlsApi['TabSheet']['visible'].set = D3Api.TabSheetCtrl.setVisible;
D3Api.controlsApi['TabSheet']['index']={get:D3Api.TabSheetCtrl.getIndex};
D3Api.controlsApi['TabSheet']['caption']={get: D3Api.TabSheetCtrl.getCaption, set: D3Api.TabSheetCtrl.setCaption};
