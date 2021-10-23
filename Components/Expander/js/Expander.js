/**
 *
 * @component
 */
D3Api.ExpanderCtrl = new function() {
    var _this = this;

    /**
     *
     * @param dom
     */
    this.init = function(dom) {
        /*
        dom.D3Store.value = true;
        dom.D3Store.mode = D3Api.getProperty(dom, 'mode', 'horizontal');
        dom.D3Store.height = D3Api.getProperty(dom, 'hgt');
        dom.D3Store.width = D3Api.getProperty(dom, 'wdt','auto');
        dom.D3Store.caption_hide = D3Api.getProperty(dom, 'caption_hide');
        dom.D3Store.caption_show = D3Api.getProperty(dom, 'caption_show');
        dom.D3Store.value = D3Api.hasClass(dom, 'show');
        dom.D3Store.captionCont = D3Api.getAllDomBy(dom, '[cont="captionCont"]');
        dom.D3Store.captionCont = dom.D3Store.captionCont[dom.D3Store.captionCont.length-1];
        */
        D3Api.BaseCtrl.initEvent(dom, 'onchange');
        this.init_focus(dom);
    };

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getValue = function Expander_getValue(dom) {
        return dom.D3Store.value;
    };

    this.getHeightValue = function Expander_getValue(dom) {
        var _ctrl =dom;
        if ((_ctrl.getAttribute("height") !== null) &&(_ctrl.getAttribute("height").length > 0)) {
           _height = _ctrl.getAttribute("height");
        } else {
           _height = (_ctrl.parentNode.getBoundingClientRect()).height+"px";
        }
        if (!isNaN(_height)) {
              _height+="px";
         }
        return _height;
    };

    this.setHeightValue = function Expander_getValue(dom,_heightValue) {
        var _ctrl =dom;
        if (!isNaN(_heightValue)) {
              _heightValue+="px";
         }
        _ctrl.setAttribute("height",_heightValue)
        this.toggleHeight(dom);
    };

    this.toggleHeight = function Expander_setValue(dom, value) {
        var _ctrl =dom.parentNode;
        var _height = value;

        if ((_ctrl.getAttribute("height") !== null) &&(_ctrl.getAttribute("height").length > 0)) {
           _height = _ctrl.getAttribute("height");
        } else {
           _height = (_ctrl.parentNode.getBoundingClientRect()).height+"px";
        }
        // value = _ctrl.getAttribute("show") === 'true';
        // if (typeof value === undefined ){        }
        if (!isNaN(_height)) {
              _height+="px";
         }
        if(_ctrl.style.height != '20px') {
            _ctrl.style.height = '20px'; // height of one line: 20px
            dom.classList.remove('show');
            dom.style.backgroundPosition="4px -7px";
        } else {
            dom.classList.add('show');
            dom.style.backgroundPosition="4px 10px";
            _ctrl.style.height = _height;
        }
    }
    /**
     *
     * @param dom
     * @param value
     * @returns {boolean}
     */
    this.setValue = function Expander_setValue(dom, value) {
        if (value === undefined) {
            value = false ;
        }
        var srcVal = dom.getAttribute("value") === 'true';
        var mode =  dom.getAttribute("mode");
        var caption_hide =  dom.getAttribute("caption_hide");
        var caption_show =  dom.getAttribute("caption_show");

        if(srcVal !== value) {
            if( mode == 'horizontal') {
               D3Api.setStyle(dom, 'height', dom.style.height);
            } else if(mode == 'vertical') {
               D3Api.setStyle(dom, 'height', dom.style.width);
            }

            D3Api.addClass(dom, 'show');
            if(caption_hide || caption_show) {
                 _this.setCaption(dom, caption_hide);
            }
            dom.setAttribute("value",srcVal !== value);
        }
        D3Api.resize();
        // dom.callEvent('onchange');

        /*
        if (typeof dom.D3Store.value === undefined){
            dom.D3Store.value = dom.getAttribute("value") === 'true';
        }
        value = (value === undefined) ? !dom.D3Store.value : !!value;
        if(dom.D3Store.value !== value) {
            if(dom.D3Store.value = value) {
                if(dom.D3Store.mode == 'horizontal')
                    D3Api.setStyle(dom, 'height', dom.D3Store.height);
                else if(dom.D3Store.mode == 'vertical')
                    D3Api.setStyle(dom, 'width', dom.D3Store.width);
                
                D3Api.addClass(dom, 'show');
                if(dom.D3Store.caption_hide || dom.D3Store.caption_show) {
                    _this.setCaption(dom, dom.D3Store.caption_hide);
                }
            }
            else {
                D3Api.removeClass(dom, 'show');
                if(dom.D3Store.mode == 'horizontal')
                    D3Api.setStyle(dom, 'height', '');
                else if(dom.D3Store.mode == 'vertical')
                    D3Api.setStyle(dom, 'width', '');
                    
                if(dom.D3Store.caption_hide || dom.D3Store.caption_show) {
                    _this.setCaption(dom, dom.D3Store.caption_show);
                }
            }
            D3Api.resize();
            dom.D3Base.callEvent('onchange');
        }*/
        return value;
    };

    /**
     *
     * @param dom
     * @returns {*}
     */
    this.getCaption = function Expander_getCaption(dom) {
        return D3Api.getTextContent(dom.D3Store.captionCont);
    };

    /**
     *
     * @param dom
     * @param value
     * @returns {string}
     */
    this.setCaption = function Expander_setCaption(dom, value) {
        value = (D3Api.empty(value)) ? '' : String(value);
        D3Api.addTextNode(dom.D3Store.captionCont, value, true);
        return value;
    };

    /**
     *
     * @param dom
     * @returns {string}
     */
    this.getCaptionHide = function Expander_getCaptionHide(dom) {
        return dom.D3Store.caption_hide;
    };

    /**
     *
     * @param dom
     * @param value
     * @returns {*}
     */
    this.setCaptionHide = function Expander_setCaptionHide(dom, value) {
        return dom.D3Store.caption_hide = (D3Api.empty(value)) ? undefined : String(value);
    };
    
    /**
     *
     * @param dom
     * @returns {string}
     */
    this.getCaptionShow = function Expander_getCaptionShow(dom) {
        return dom.D3Store.caption_show;
    };

    /**
     *
     * @param dom
     * @param value
     * @returns {*}
     */
    this.setCaptionShow = function Expander_setCaptionShow(dom, value) {
        return dom.D3Store.caption_show = (D3Api.empty(value)) ? undefined : String(value);
    };

    /**
     *
     * @param dom
     * @param e
     */
    this.CtrlKeyDown = function(dom, e)
    {
        switch (e.keyCode)
        {
            case 39: //стрелка вправо - развернуть
            case 32://пробел
                D3Api.ExpanderCtrl.setValue(dom, true) ;
                D3Api.stopEvent(e);
                break;
            case 37: //стрелка влево - свернуть
            case 8: // Backspase
                D3Api.ExpanderCtrl.setValue(dom, false) ;
                D3Api.stopEvent(e);
                break;
        }
    }

    ///**********************************************************************************
    var oldLeft=new Number(0);
    var oldTop=new Number(0);
    var captureX=new Number(0);
    var captureY=new Number(0);
    var docMoveEvent=function(){};
    var docUpEvent=function(){};
    var modal_win;

    var blockEdit =null;
    var blockSpliter =null;
    var new_x = 0;
    var new_y = 0;
    this.moveSplit=function(evt,direction) {
           if ((typeof direction === 'undefined')||( direction == '')) {
              direction = "top";
           }
           if (direction == "top") {
              blockEdit = evt.target.previousSibling;
           }
           /*
           if (direction == "left"){
               blockEdit =evt.target.previousElementSibling;
           }
           if (direction == "right"){
               blockEdit =evt.target.nextElementSibling;
           }
           */
           blockSpliter = evt.target;
           rect = blockEdit.getBoundingClientRect()
           blockEdit.style.width = rect.width + "px";
           blockEdit.style.height = rect.height + "px";
           blockEdit.style.left =  rect.left + "px";
           blockEdit.style.top =  rect.top + "px";
           var ie = 0;
           var op = 0;
           var ff = 0;
           var browser = navigator.userAgent;
           if (browser.indexOf("Opera") != -1) op = 1;
           else {
             if (browser.indexOf("MSIE") != -1) ie = 1;
             else {
               if (browser.indexOf("Firefox") != -1) ff = 1;
             }
           }
           delta_x = 0;
           delta_y = 0;
           /* Ставим обработчики событий на нажатие и отпускание клавиши мыши */
           saveXY();
      	   addEvent(document,'mouseup',clearXY);
      	   addEvent(document,'mouseout',clearXY);

           /* При нажатии кнопки мыши попадаем в эту функцию */
           function saveXY(obj_event) {
             /* Получаем текущие координаты курсора */
             x = window.event.clientX;
             y = window.event.clientY;
             x_block = rect.width;
             y_block = rect.height-5;
             delta_x = x_block - x;
             delta_y = y_block - y;
             if (op || ff) {
   	    	     addEvent(document,'mousemove',moveBlock,false);
   	    	     // document.addEventListener('mousemove', saveXY, false);
                 // block.addEventListener("onmousemove", moveBlock, false);
             } else {
                 document.onmousemove = moveBlock;
             }
           }
           function clearXY() {
               var heightStr = blockEdit.style.height;
               heightNum = +heightStr.replace(/[a-zа-яё]/gi, '');
               if (heightNum > 100) {
                   heightStr = heightStr.replace(/[0-9]/g, '');
                   blockEdit.setAttribute("height",heightNum+heightStr);
               }
           }
           function moveBlock(obj_event) {
              if (obj_event.buttons !== 1){
                 if (op || ff) {
                    removeEvent(document,'mousemove',moveBlock);
                 } else {
                    document.onmousemove = null; // При отпускании мыши убираем обработку события движения мыши
                 }
                 return false
              }
              /* Получаем новые координаты курсора мыши */
              x = window.event.clientX;
              y = window.event.clientY;
              /* Вычисляем новые координаты блока */
              if ((direction == "left")||(direction == "right")) {
                 new_x = delta_x + x;
                 blockEdit.style.width = new_x + "px";
              }
              if (direction == "top") {
                 new_y = delta_y + y;
                 blockEdit.style.height = new_y + "px";
              }
           }
           return false;
        }
    ///**********************************************************************************

};
D3Api.controlsApi['Expander'] = new D3Api.ControlBaseProperties(D3Api.ExpanderCtrl);
D3Api.controlsApi['Expander']['value'] = {get: D3Api.ExpanderCtrl.getValue, set: D3Api.ExpanderCtrl.setValue};
D3Api.controlsApi['Expander']['caption'] = {get: D3Api.ExpanderCtrl.getCaption, set: D3Api.ExpanderCtrl.setCaption};
D3Api.controlsApi['Expander']['captionHide'] = {get: D3Api.ExpanderCtrl.getCaptionHide, set: D3Api.ExpanderCtrl.setCaptionHide};
D3Api.controlsApi['Expander']['captionShow'] = {get: D3Api.ExpanderCtrl.getCaptionShow, set: D3Api.ExpanderCtrl.setCaptionShow};
