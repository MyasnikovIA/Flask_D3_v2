/**
 *
 * @component
 */
D3Api.LayoutSplitCtrl = new function ()
{
    this.decimalSeparator = (1.1).toLocaleString().substring(1, 2);
    this.thousandSeparator = (1000).toLocaleString().substring(1, 2);
    /**
     *
     * @param _dom
     */
    this.init = function(_dom)
    {
        var inp = D3Api.EditCtrl.getInput(_dom);
        this.init_focus(inp);

        D3Api.addEvent(inp, 'change', function(event){
            D3Api.stopEvent(event);

        }, true);

        D3Api.BaseCtrl.initEvent(_dom,'onchange');
        D3Api.BaseCtrl.initEvent(_dom,'onformat');
    }


    ///**********************************************************************************
    var oldLeft=new Number(0);
    var oldTop=new Number(0);
    var captureX=new Number(0);
    var captureY=new Number(0);
    var modal_win;

    this.mouseDownHor = function(evt){
        console.log("this.mouseDownHor",evt)
    }
    this.mouseDownVert = function(evt){
     	captureX=evt.pageX||evt.x;captureY=evt.pageY||evt.y;
     	var _windowObject=this;
        modal_win = evt.target
    	addEvent(document,'mousemove',docMoveEvent=function (e){_windowObject._onMove(e||window.event);});
    	addEvent(document,'mouseup',docUpEvent=function (e){_windowObject._onMouseUp(e||window.event);});
        console.log("this.mouseDownVert",evt);
    }
    this._onMove = function(evt) {
        this.setPosition(oldLeft-captureX+parseInt(evt.pageX||evt.x),oldTop-captureY+parseInt(evt.pageY||evt.y));
    }
        this.setPosition=function (_left,_top){_left=Math.max(_left,0);_top=Math.max(_top,0);_setPosition.call(this,_left,_top);left=_left;top=_top;}
        var _setPosition=function (_left,_top){setDomPos(modal_win,_left,_top);}

    function setDomPos(_dom,_left,_top) {
        _dom.style.left = _left + 'px';
        _dom.style.top = _top + 'px';
    }
    ///**********************************************************************************

}
D3Api.controlsApi['LayoutSplit'] = new D3Api.ControlBaseProperties(D3Api.LayoutSplitCtrl);

