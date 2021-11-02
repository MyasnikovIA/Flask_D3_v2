/**
 *
 * @component
 */
D3Api.PopupMenuCtrl = new function()
{
    /**
     *
     * @param dom
     */
    this.init = function(dom)
    {
        if(!D3Api.BROWSER.msie)
            dom.style.zIndex = 10;
        var jm = D3Api.getProperty(dom,'join_menu',false) || (D3Api.getProperty(dom,'join_menu_var',false) ? dom.D3Form.getVar(D3Api.getProperty(dom,'join_menu_var','')) : false);
        if(jm)
        {
            var jmc = dom.D3Form.getControl(jm);
            if(!jmc)
                return;
            var joinGroupName = D3Api.getProperty(dom,'join_group',false) || 'additionalMainMenu';
            var groupAmm = D3Api.getDomByAttr(jmc, 'name', joinGroupName);
            if(!groupAmm)
                return;
            D3Api.BaseCtrl.initEvent(dom,'onpopup','coords,show',undefined,jmc);
            var items = D3Api.PopupMenuCtrl.getItems(dom,true);
            for(var i = 0, c = items.length; i < c; i++)
                D3Api.PopupMenuCtrl.addItemDom(groupAmm, items[i]);
            return;
        }
        D3Api.PopupMenuCtrl.setWaitAction(dom,D3Api.getProperty(dom,'onpopup_action',false));
        dom.D3Store.popupObjects = [];

        var po = D3Api.getProperty(dom,'popupobject',false);
        if (po)
        {
            var pod = dom.D3Form.getControl(po);
            if (pod)
            {
                D3Api.PopupMenuCtrl.setPopupObject(dom,pod);
            }    
        }
        
        D3Api.BaseCtrl.initEvent(dom,'onpopup','coords,show');
        this.init_focus(dom);
        var ctrls = D3Api.getAllDomBy(dom.D3Form.currentContext || dom.D3Form.DOM,'[popupmenu="'+D3Api.getProperty(dom,'name','')+'"]');
        
        for(var i = 0, c = ctrls.length; i < c; i++)
        {
            D3Api.PopupMenuCtrl.setPopupObject(dom,ctrls[i]);
        }
        
        D3Api.addDom(dom.D3Form.DOM, dom);

        for(var collectionGroup = D3Api.getAllDomBy(dom, '[cont="groupitem"][separator]'), i = 0; i < collectionGroup.length; i++) {
            var placeSep = D3Api.getProperty(collectionGroup[i], 'separator'),
                     sep = D3Api.createDom('<div class="item separator" item_split="true" cmptype="PopupItem"></div>');
            dom.D3Form.parse(sep);
            if(!collectionGroup[i].children.length) D3Api.addClass(sep, 'ctrl_hidden');
            collectionGroup[i].D3Store.separator = (placeSep === 'before') && D3Api.insertBeforeDom(collectionGroup[i], sep) || 
                                                   (placeSep === 'after')  && D3Api.insertAfterDom(collectionGroup[i], sep)  ||
                                                   null;
        }
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getPopupObject = function PopupMenuCtrl_GetPopupObject(dom)
    {
        return dom.D3Store.popupObject;
    }

    /**
     *
     * @param dom
     * @param objDom
     */
    this.setPopupObject = function PopupMenuCtrl_SetPopupObject(dom,objDom)
    {
        if (dom.D3Store.popupObjects.indexOf(objDom) >= 0)
        {
            return;
        }
        function popup(e)
        {
            var evt = D3Api.getEvent(e);
            var coords = getClientEventCoords(evt); 
 
            if((evt.button && evt.button == 2) || (evt.which && evt.which == 3))
            {
                    dom.D3Store.popupObject = objDom || dom.D3Store.popupObject;
                    D3Api.PopupMenuCtrl.show(dom,coords);
                    D3Api.stopEvent(evt);
            }
        }
        
        if (objDom)
        {
            dom.D3Store.popupObjects.push(objDom);
            D3Api.addEvent(objDom,'mousedown',popup);
        }
    }

    /**
     *
     * @param dom
     * @param coords
     */
    this.show = function PopupMenuCtrl_Show(dom,coords)
    {
        if(dom.D3Store.waitAction)
        {
            D3Api.addClass(dom, 'waitAction');
            dom.D3Form.getAction(dom.D3Store.waitAction).execute();
        }else
        {
            D3Api.removeClass(dom, 'waitAction');
            var reqAmount = 0;
            var reqUids = {};
            if(dom.D3Store.uidBReq)
            {
                D3Api.Base.removeEvent('onRequestServerBegin',dom.D3Store.uidBReq);
            }
            if(dom.D3Store.uidEReq)
            {
                D3Api.Base.removeEvent('onRequestServerEnd',dom.D3Store.uidEReq);
            }
            dom.D3Store.uidBReq = D3Api.Base.addEvent('onRequestServerBegin', function(reqObj,reqUid){
                if(reqAmount == 0)
                    D3Api.addClass(dom, 'waitAction');
                reqAmount++;
                reqUids[reqUid] = true;
            });
            dom.D3Store.uidEReq = D3Api.Base.addEvent('onRequestServerEnd', function(reqObj,reqUid){
                if(reqUids[reqUid])
                    reqAmount--;
                if(reqAmount > 0)
                    return;
                
                if(dom.D3Store.uidBReq)
                {
                    D3Api.Base.removeEvent('onRequestServerBegin',dom.D3Store.uidBReq);
                    dom.D3Store.uidBReq = null;
                }
                if(dom.D3Store.uidEReq)
                {
                    D3Api.Base.removeEvent('onRequestServerEnd',dom.D3Store.uidEReq);
                    dom.D3Store.uidEReq = null;
                }
                
                if(dom.D3Store.hideFunc == null)
                    return;
                
                var res = dom.D3Base.callEvent('onpopup',coords,true);
                if(res === false)
                {
                    dom.D3Store.hideFunc();
                    return;
                }
                D3Api.removeClass(dom, 'waitAction');
                calcPos();
            });
            var res = dom.D3Base.callEvent('onpopup',coords);
            if(res === false)
                return;
            
            if(reqAmount == 0)
            {
                if(dom.D3Store.uidBReq)
                {
                    D3Api.Base.removeEvent('onRequestServerBegin',dom.D3Store.uidBReq);
                    dom.D3Store.uidBReq = null;
                }
                if(dom.D3Store.uidEReq)
                {
                    D3Api.Base.removeEvent('onRequestServerEnd',dom.D3Store.uidEReq);
                    dom.D3Store.uidEReq = null;
                }
            }
        }
        D3Api.removeClass(dom, 'notactive');
        var iact = D3Api.getAllDomBy(dom, '.item.active');
        for(var i = 0, c = iact.length; i < c; i++)
            D3Api.removeClass(iact[i], 'active');
        
        var calcPos = function(){
            var sX = D3Api.getBodyScrollLeft();
            var sY = D3Api.getBodyScrollTop();
            D3Api.showDomBlock(dom);
            var el_size = D3Api.getAbsoluteClientRect(dom);
            el_size.x = coords.left-5;
            el_size.y = coords.top-5;

            var page = D3Api.getPageWindowSize();

            var h = page.windowHeight+sY;
            var mcY = el_size.y+el_size.height;

            if (mcY-h > 0)
                el_size.y -=mcY-h+7;

            var w = page.windowWidth+sX;
            var mcX = el_size.x+el_size.width;

            if (mcX-w > 0)
                el_size.x -=mcX-w+7;

            dom.style.left = el_size.x+'px';
            dom.style.top  = el_size.y+'px';
        }
        calcPos();
        dom.D3Store.hideFunc = function(event)
        {
            if(event)
            {
                var t = D3Api.getEventTarget(event);
                t = D3Api.getControlByDom(t, 'PopupMenu');
                if(t == dom)
                    return;
            }
            D3Api.setDomDisplayDefault(dom);
            dom.D3Store.selected_item = null;
            dom.D3Store.parent_item = new Array();
            //setTimeout(function(){D3Api.hideDom(dom)},100);
            D3Api.removeEvent(document,"mousedown",dom.D3Store.hideFunc,true);
            dom.D3Store.hideFunc = null;
            D3Api.stopEvent(event);
        }
        
        D3Api.addEvent(document,"mousedown",dom.D3Store.hideFunc,true);
        //setTimeout(function(){D3Api.setDomDisplayDefault(dom)},1000);
    }
    function getClientEventCoords(evt)
    {
            var coords = {left:0, top:0};

            coords.left = evt.clientX;
            coords.top = evt.clientY;

            return coords;
    }

    /**
     *
     * @param event
     * @param anyDom
     * @param menuName
     */
    this.showPopupMenu = function(event,anyDom,menuName)
    {
        var ctrl = D3Api.getControlByDom(anyDom);
        var menu = ctrl.D3Form.getControl(menuName);
        if (menu)
        {
            menu.D3Store.popupObject = ctrl || menu.D3Store.popupObject;
            var evt = D3Api.getEvent(event);
            var coords = getClientEventCoords(evt); 
            D3Api.PopupMenuCtrl.show(menu,coords);      
        }
    }

    /**
     *
     * @param dom
     * @param itemDom
     * @param itemCont
     */
    this.addItemDom = function(dom,itemDom,itemCont)
    {
        if(itemCont)
        {
            itemCont = D3Api.getDomByAttr(itemCont, 'cont', 'menu');
        }else
            itemCont = dom;
        D3Api.addDom(itemCont, itemDom);
    }

    /**
     *
     * @param dom
     * @param rootOnly
     * @param onlySeparators
     * @returns {*}
     */
    this.getItems = function(dom,rootOnly,onlySeparators)
    {
        return D3Api.getAllDomBy(dom, '[cmptype="PopupItem"'+(rootOnly?'][rootitem="true"':'')+(onlySeparators===true?'][item_split="true"':'')+']');
    }

    /**
     *
     * @param dom
     * @returns {*|boolean}
     */
    this.getEnabled = function(dom)
    {
        return D3Api.hasClass(dom, 'ctrl_disable');
    }

    /**
     *
     * @param dom
     * @param value
     * @returns {boolean}
     */
    this.setEnabled = function(dom,value)
    {
        var items = D3Api.PopupMenuCtrl.getItems(dom,true);
        
        for(var i = 0, c = items.length; i < c; i++)
        {
            D3Api.setControlPropertyByDom(items[i], 'enabled', value, true);
        }
        if(D3Api.getBoolean(value))
            D3Api.removeClass(dom,'ctrl_disable');
        else
            D3Api.addClass(dom,'ctrl_disable');
        return true;
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getWaitAction = function(dom)
    {
        return dom.D3Store.waitAction;
    }

    /**
     *
     * @param dom
     * @param value
     * @returns {boolean}
     */
    this.setWaitAction = function(dom,value)
    {
        if(dom.D3Store.waitAction)
            dom.D3Form.getAction(dom.D3Store.waitAction).removeEvent('onafter_execute',dom.D3Store.waitActionAUid);
        if(D3Api.empty(value))
        {
            dom.D3Store.waitAction = value;
            return true;
        }
        var act = dom.D3Form.getAction(value);
        if(!act)
            return false;
        
        dom.D3Store.waitAction = value;
        //Значит в загрузке
        dom.D3Store.waitActionAUid = act.addEvent('onafter_execute',function(){
            if(!dom.D3Store.hideFunc)
                return;
            
            var res = dom.D3Base.callEvent('onpopup');
            if(res === false)
            {
                dom.D3Store.hideFunc();
                return;
            }
            
            D3Api.removeClass(dom, 'waitAction');
        });
    }

    /**
     *
     * @param dom
     * @param item
     * @param name
     * @returns {*}
     */
    this.addGroupItem = function(dom, item, name) {
        name = (typeof name === 'string') ? 'name="' + name + '"' : '';
        var groupitem = D3Api.createDom('<div ' + name + ' class="popupGroupItem" cont="groupitem" cmptype="PopupGroupItem"></div>');
        dom.D3Form.parse(groupitem);
        item = typeof item === 'string' && D3Api.getDomByAttr(dom, 'name', item) || typeof item === 'object' && item || null;
        if(item) 
            return D3Api.insertAfterDom(item, groupitem);
        return D3Api.addDom(dom, groupitem);
    };

    /**
     *
     * @param dom
     * @param attrs
     * @param rootItem
     * @param rootGroup
     * @param boolBefore
     * @param posItem
     * @returns {null|*}
     */
    this.addItem = function(dom,attrs,rootItem,rootGroup,boolBefore,posItem)
    {
        posItem = typeof posItem === 'string' && D3Api.getDomByAttr(dom, 'name', posItem) || typeof posItem === 'object' && posItem || null;
        if(!rootItem)
            rootItem = posItem && posItem.D3Store.parentItem?posItem.D3Store.parentItem:dom;
        else if(typeof(rootItem) == 'string')
            rootItem = D3Api.getDomByAttr(dom, 'name', rootItem);
        else
            rootItem = rootItem;
        rootGroup = typeof rootGroup === 'string' && D3Api.getDomByAttr(rootItem, 'name', rootGroup) || null;
                
        var rootItemCont = rootItem;
        if (D3Api.getProperty(rootItem, 'cmptype') == 'PopupItem')
        {
            D3Api.addClass(rootItem, 'haveItems');
            var submenu = D3Api.getDomByAttr(rootItem, 'cont', 'menu');
            if(!submenu)
            {
                var rootItemNew = (rootItem.outerHTML)?D3Api.createDom(rootItem.outerHTML):rootItem.cloneNode(true);
                D3Api.insertBeforeDom(rootItem, rootItemNew);
                D3Api.removeDom(rootItem);
                rootItem = null;
                rootItem = rootItemNew;
                var itemCont = D3Api.getDomByAttr(rootItem, 'cont', 'item');
                D3Api.setProperty(itemCont, 'onmouseover', ((attrs['onmouseover']) ? attrs['onmouseover']+';' : '') + 'D3Api.PopupItemCtrl.hoverItem(this);');
                D3Api.setProperty(itemCont, 'onclick', 'D3Api.PopupItemCtrl.hoverItem(this,true);');
                dom.D3Form.parse(rootItem);
            
                submenu = D3Api.createDom('<div class="popupMenu subItems" cont="menu"></div>');
                D3Api.addDom(rootGroup || rootItem,submenu);
            }
            rootItemCont = submenu;          
        }
        var attrStr = 'cmptype="PopupItem" '+(rootItemCont == dom?'rootitem="true" ':'');
        var events = '';
        var itemText = '';
        var item;
        if(attrs['caption'] && attrs['caption'] == '-')
        {
            itemText = '<div class="item separator" '+attrStr+(attrs['name'] && attrs['name']!=''?' name="'+attrs['name']+'"':'')+' item_split="true" ></div>';
        }else
        {
            if(attrs['onclick'])
            {
                events += ' onclick="'+attrs['onclick']+'; D3Api.PopupItemCtrl.clickItem(this);"';
                attrs['onclick'] = undefined;
                delete attrStr['onclick'];
            }
            if(attrs['onmouseover'])
            {
                events += ' onmouseover="'+attrs['onmouseover']+'; D3Api.PopupItemCtrl.hoverItem(this);"';
                attrs['onmouseover'] = undefined;
                delete attrs['onmouseover'];
            }
            else {
                events += ' onmouseover="D3Api.PopupItemCtrl.hoverItem(this);"';
            }
            for(var a in attrs)
            {
                if(attrs.hasOwnProperty(a)){
                    attrStr += ' '+a+'="'+attrs[a]+'"';
                }
            }
            itemText = '<div class="item" '+attrStr+' ><table style="width:100%" cmpparse="PopupItem" '+events+' cont="item"><tr><td class="itemCaption"><img src="'+(attrs['icon'] || '')+'" cont="itemIcon" class="itemIcon"/><span cont="itemCaption">'+attrs['caption']+'</span></td><td class="caret">&nbsp;&nbsp;</td></tr></table></div>';
        }
        item = D3Api.createDom(itemText);
        if(!item)
            return null;
        dom.D3Form.parse(item);
        var rootEl = rootGroup || rootItemCont;
        if(posItem)
        {
            if(boolBefore) 
                D3Api.insertBeforeDom(posItem, item);
            else
                D3Api.insertAfterDom(posItem, item);
        }else
        {
            if(boolBefore && rootEl.firstChild) 
                D3Api.insertBeforeDom(rootEl.firstChild, item);
            else 
                D3Api.addDom(rootEl, item);
            if(rootGroup && rootGroup.D3Store && rootGroup.D3Store.separator) {
                D3Api.removeClass(rootGroup.D3Store.separator, 'ctrl_hidden');
            }
        }
        item.D3Store.parentItem = rootItem;
        dom.D3Base.callEvent('onitem_add',item,rootEl);
        return item;
    }

    /**
     *
     * @param dom
     * @param itemDom
     */
    this.deleteItem = function(dom,itemDom)
    {
        var rootEl = itemDom.parentNode;
        if(dom.D3Base.callEvent('onitem_delete',itemDom,rootEl) !== false)
            D3Api.removeDom(itemDom);     
    }

    /**
     *
     * @param dom
     */
    this.defaultAction = function(dom)
    {
        var item = D3Api.getDomBy(dom,'[cmptype="PopupItem"][default="true"]>table[cont="item"]');

        if (item) {
            item.dispatchEvent(new CustomEvent('click'));
        }
    }

    /**
     *
     * @param dom
     * @param e
     */
    this.CtrlKeyDown = function(dom, e)
    {
        switch (e.keyCode) {
            case 40: //стрелка вниз
                D3Api.PopupMenuCtrl.setNextItem(dom, 1);
                D3Api.stopEvent(e)
                break;
            case 38: //стрелка вверх
                D3Api.PopupMenuCtrl.setNextItem(dom, -1);
                D3Api.stopEvent(e)
                break;
            case 39: //стрелка вправо
                var submenu = D3Api.getDomByAttr(D3Api.PopupMenuCtrl.getSelectedItem(dom), 'cont', 'menu');
                if(submenu)
                {
                    if(!dom.D3Store.parent_item)
                        dom.D3Store.parent_item = new Array();
                    dom.D3Store.parent_item.push(D3Api.PopupMenuCtrl.getSelectedItem(dom));
                    dom.D3Store.selected_item = null;
                    D3Api.PopupMenuCtrl.setNextItem(dom, 1);
                }
                D3Api.stopEvent(e)
                break;
            case 37: //стрелка влево
                if(!dom.D3Store.parent_item)
                    break;
                var parent_item = dom.D3Store.parent_item[dom.D3Store.parent_item.length - 1];

                if(!parent_item)
                    break;
                D3Api.PopupItemCtrl.hoverItem(parent_item);
                dom.D3Store.parent_item.pop();
                var items = D3Api.PopupMenuCtrl.getItemsOfActiveMenu(dom);
                for(var i = 0; i < items.length; i++) {
                    if (items[i] == parent_item) {
                        dom.D3Store.selected_item = i+1;
                        D3Api.PopupMenuCtrl.setNextItem(dom, -1);
                        break;
                    }
                }
                D3Api.stopEvent(e)
                break;
            case 13://Enter
                var selected_item=D3Api.PopupMenuCtrl.getSelectedItem(dom);
                var cont_item = D3Api.getDomByAttr(selected_item, 'cont', 'item');
                cont_item.click();
                D3Api.stopEvent(e)
                break;
            case 27: //Esc
                dom.D3Store.hideFunc();
                if(dom.D3Form.lastFocusControl)
                    dom.D3Form.lastFocusControl.focus();
                D3Api.stopEvent(e)
                break;
        }
    }
    ///delta = 1 движение вниз по меню
    ///delta = -1 движение вверх по меню

    /**
     *
     * @param dom
     * @param delta
     * @returns {*}
     */
    this.setNextItem = function(dom, delta)
    {
        var n = dom.D3Store.selected_item;

        if(n === undefined || n === null)
            n = 0;
        else
        {
            n += delta;
        }

        n = this.setSelectedItemIndex(dom, n);
        if(n && D3Api.hasClass(D3Api.PopupMenuCtrl.getSelectedItem(dom), 'separator'))
        {
            n += delta;
            n = this.setSelectedItemIndex(dom, n);
        }

        return n;
    };

    /**
     *
     * @param dom
     * @param index
     * @returns {*}
     */
    this.setSelectedItemIndex = function(dom, index)
    {
        var active_menu_items = D3Api.PopupMenuCtrl.getItemsOfActiveMenu(dom);
        if(active_menu_items && index != -1 && index !== false &&
            index < active_menu_items.length &&
            active_menu_items[index])
        {
            dom.D3Store.selected_item = index;
            D3Api.PopupItemCtrl.hoverItem(active_menu_items[index]);
        }

        return dom.D3Store.selected_item;
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getSelectedItem = function(dom)
    {
        return D3Api.PopupMenuCtrl.getItemsOfActiveMenu(dom)[dom.D3Store.selected_item];
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getItemsOfActiveMenu = function(dom)
    {
        if(!dom.D3Store.parent_item || dom.D3Store.parent_item.length == 0)
        {
            return  D3Api.PopupMenuCtrl.getItems(dom, true);
        }
        else
        {
            var submenu = D3Api.getDomByAttr(dom.D3Store.parent_item[dom.D3Store.parent_item.length - 1], 'cont', 'menu');
            if(!submenu)
                return;

            return D3Api.PopupMenuCtrl.getItems(submenu);
        }
    }
}
D3Api.controlsApi['PopupMenu'] = new D3Api.ControlBaseProperties(D3Api.PopupMenuCtrl);
D3Api.controlsApi['PopupMenu']['popupobject']={get:D3Api.PopupMenuCtrl.getPopupObject,set: D3Api.PopupMenuCtrl.setPopupObject};
D3Api.controlsApi['PopupMenu']['enabled']={get:D3Api.PopupMenuCtrl.getEnabled,set: D3Api.PopupMenuCtrl.setEnabled};
D3Api.controlsApi['PopupMenu']['onpopup_action']={get:D3Api.PopupMenuCtrl.getWaitAction,set: D3Api.PopupMenuCtrl.setWaitAction};
D3Api.controlsApi['PopupMenu']['item']={set: D3Api.PopupMenuCtrl.setSelectedItemIndex};


/**
 *
 * @component
 */
D3Api.PopupItemCtrl = new function()
{

    /**
     *
     * @param dom
     */
    this.clickItem = function(dom)
    {
        var m = D3Api.getControlByDom(dom, 'PopupMenu');
        
        m.D3Store.hideFunc && m.D3Store.hideFunc();
    }
    
    /**
     *
     * @param dom
     * @param click
     */
    this.hoverItem = function(dom,click)
    {
        var event = D3Api.getEvent();
        if(D3Api.BROWSER.msie && !click) {
            var toElement = event.relatedTarget || event.fromElement;
            while(toElement && toElement !== dom) {
                toElement = toElement.parentNode;
            }
            if(toElement === dom) return;
        }
        var item = D3Api.getControlByDom(dom, 'PopupItem');
        var toogle = D3Api.hasClass(item, 'active');
        if(D3Api.getEventTarget() != D3Api.getEventCurrentTarget() && toogle && event.type != 'click' && event.type != 'keydown')
            return;     
        var menu = D3Api.getDomByDomAttr(dom, 'cont', 'menu');
        if(!menu)
            return;
        D3Api.removeClass(menu, 'notactive');
        var iact = D3Api.getAllDomBy(menu, '.item.active');
        for(var i = 0, c = iact.length; i < c; i++)
            D3Api.removeClass(iact[i], 'active');
        
        if(toogle)
            return;
        
        D3Api.addClass(item, 'active');
        
        var submenu = D3Api.getDomByAttr(item, 'cont', 'menu');
        if(!submenu)
            return;
        D3Api.addClass(menu, 'notactive');
        D3Api.removeClass(submenu, 'notactive');
        
        var rect = D3Api.getAbsoluteClientRect(item);
        
        
        var sX = D3Api.getBodyScrollLeft();
        var sY = D3Api.getBodyScrollTop();
        var el_size = D3Api.getAbsoluteClientRect(submenu);

        var page = D3Api.getPageWindowSize();

        var h = page.windowHeight+sY;
        var mcY = rect.y+el_size.height;

        var dY = 0;
        if (mcY-h > 0)
            dY = -(mcY-h);

        var w = page.windowWidth+sX;
        var mcX = rect.x+rect.width+el_size.width;

        var dX = rect.width-5;
        if (mcX-w > 0)
            dX = -(el_size.width-5);

        submenu.style.left = dX+'px';
        submenu.style.top  = dY+'px';
        submenu.style.zIndex = 10;
    }

    /**
     *
     * @param _dom
     * @param _value
     */
    this.setVisible = function PopupItem_setVisible(_dom, _value)
    {
        D3Api.BaseCtrl.setVisible(_dom,_value);
        var items = _dom.parentNode.childNodes, item = false, splitItem = null, isSplit = false;

        for(var i = 0, c = items.length; i < c; i++)
        {
            if(D3Api.hasProperty(items[i],'item_split'))
            {
                if(!item)
                {
                    if(splitItem)
                    {    
                        if(splitItem != _dom) D3Api.BaseCtrl.setVisible(splitItem, true);
                    }
                    D3Api.BaseCtrl.setVisible(items[i],false);
                }else
                {
                    splitItem = items[i];
                    item = false;
                }
            }else if(['PopupItem','PopupGroupItem'].indexOf(D3Api.getProperty(items[i],'cmptype')) != -1 && D3Api.BaseCtrl.getVisible(items[i]))
            {
                item = true;
                if(splitItem)
                {    
                    if(splitItem != _dom) D3Api.BaseCtrl.setVisible(splitItem, true);
                    splitItem = null;
                }
            }                     
        }    
        if(splitItem)
            D3Api.BaseCtrl.setVisible(splitItem,false);
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getCaption = function PopupItemCtrl_getCaption(dom)
    {
        var cont = D3Api.getDomByAttr(dom, 'cont', 'itemCaption');
        return D3Api.getTextContent(cont);
    }

    /**
     *
     * @param dom
     * @param value
     */
    this.setCaption = function PopupItemCtrl_setCaption(dom,value)
    {
        var cont = D3Api.getDomByAttr(dom, 'cont', 'itemCaption');
        D3Api.addTextNode(cont, D3Api.empty(value) ? '' : value, true);
    }

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getIcon = function PopupItemCtrl_getIcon(dom)
    {
        var cont = D3Api.getDomByAttr(dom, 'cont', 'itemIcon');
        return cont.src;
    }

    /**
     *
     * @param dom
     * @param value
     */
    this.setIcon = function PopupItemCtrl_setIcon(dom,value)
    {
        var cont = D3Api.getDomByAttr(dom, 'cont', 'itemIcon');
        cont.src = D3Api.empty(value) ? '' : value;
    }
}
D3Api.controlsApi['PopupItem'] = new D3Api.ControlBaseProperties(D3Api.PopupItemCtrl);
D3Api.controlsApi['PopupItem']['visible'].set = D3Api.PopupItemCtrl.setVisible;
D3Api.controlsApi['PopupItem']['caption'] = {get: D3Api.PopupItemCtrl.getCaption, set: D3Api.PopupItemCtrl.setCaption};
D3Api.controlsApi['PopupItem']['icon'] = {get: D3Api.PopupItemCtrl.getIcon, set: D3Api.PopupItemCtrl.setIcon};

/**
 *
 * @component
 */
D3Api.PopupGroupItemCtrl = new function()
{
    
}

D3Api.controlsApi['PopupGroupItem'] = new D3Api.ControlBaseProperties(D3Api.PopupGroupItemCtrl);
