/**
 *
 * @component
 */
D3Api.LayoutSplitCtrl = new function ()
{
    //this.decimalSeparator = (1.1).toLocaleString().substring(1, 2);
    //this.thousandSeparator = (1000).toLocaleString().substring(1, 2);
    /**
     *
     * @param _dom
     */
    this.init = function(_dom) {
        var inp = D3Api.EditCtrl.getInput(_dom);
        this.init_focus(inp);
        //D3Api.addEvent(inp, 'change', function(event){ D3Api.stopEvent(event); }, true);
        //D3Api.BaseCtrl.initEvent(_dom,'onchange');
        //D3Api.BaseCtrl.initEvent(_dom,'onformat');
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
    var new_x = 0;
    var new_y = 0;

    this.touchSplit=function(evt,direction) {

           if ((typeof direction === 'undefined')||( direction == '')) {
              direction = "left";
           }
           if (direction == "top") {
              blockEdit = evt.changedTouches[0].target.parentElement.previousSibling.firstChild;
           }
           if (direction == "bottom") {
               blockEdit = evt.changedTouches[0].target.parentElement.nextElementSibling.firstChild;
           }
           if (direction == "left"){
               blockEdit =evt.changedTouches[0].target.previousElementSibling;
           }
           if (direction == "right"){
               blockEdit =evt.changedTouches[0].target.nextElementSibling;
           }
           block = evt.changedTouches[0].target;
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
           // document.addEventListener('mouseup', clearXY, false);
           // document.addEventListener('mouseout', clearXY, false);
      	   addEvent(document,'mouseup',clearXY);
      	   addEvent(document,'mouseout',clearXY);

           /* При нажатии кнопки мыши попадаем в эту функцию */
           function saveXY(obj_event) {
             /* Получаем текущие координаты курсора */
             x = window.event.clientX;
             y = window.event.clientY;
             x_block = rect.width;
             y_block = rect.height;
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
             if (op || ff) {
                //block.removeEventListener("onmousedown", saveXY, false);
                //removeEvent(document,'mousemove',moveBlock);
             } else {
               // document.onmousemove = null; // При отпускании мыши убираем обработку события движения мыши
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
                 //obj_event.target.style.width = new_x + "px";
                 blockEdit.style.width = new_x + "px";
              }
              if (direction == "top") {
                 new_y = delta_y + y;
                 //obj_event.target.style.height = new_y + "px";
                 blockEdit.style.height = new_y + "px";
              }
              if (direction == "bottom") {
                 // В контейнере окно необходимо инвертировать  перемещение  нижнего блока
                 new_y =  delta_y + y;
                 //obj_event.target.style.height = new_y + "px";
                 blockEdit.style.height = new_y + "px";
              }
           }
           return false;
    }
    this.moveSplit=function(evt,direction) {
           if ((typeof direction === 'undefined')||( direction == '')) {
              direction = "left";
           }
           if (direction == "top") {
              blockEdit = evt.target.parentElement.previousSibling.firstChild;
           }
           if (direction == "bottom") {
               blockEdit = evt.target.parentElement.nextElementSibling.firstChild;
           }
           if (direction == "left"){
               blockEdit =evt.target.previousElementSibling;
           }
           if (direction == "right"){
               blockEdit =evt.target.nextElementSibling;
           }
           block = evt.target;
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
           // document.addEventListener('mouseup', clearXY, false);
           // document.addEventListener('mouseout', clearXY, false);
      	   addEvent(document,'mouseup',clearXY);
      	   addEvent(document,'mouseout',clearXY);

           /* При нажатии кнопки мыши попадаем в эту функцию */
           function saveXY(obj_event) {
             /* Получаем текущие координаты курсора */
             x = window.event.clientX;
             y = window.event.clientY;
             x_block = rect.width;
             y_block = rect.height;
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
             if (op || ff) {
                //block.removeEventListener("onmousedown", saveXY, false);
                //removeEvent(document,'mousemove',moveBlock);
             } else {
               // document.onmousemove = null; // При отпускании мыши убираем обработку события движения мыши
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
                 //obj_event.target.style.width = new_x + "px";
                 blockEdit.style.width = new_x + "px";
              }
              if (direction == "top") {
                 new_y = delta_y + y;
                 //obj_event.target.style.height = new_y + "px";
                 blockEdit.style.height = new_y + "px";
              }
              if (direction == "bottom") {
                 // В контейнере окно необходимо инвертировать  перемещение  нижнего блока
                 new_y =  delta_y + y;
                 //obj_event.target.style.height = new_y + "px";
                 blockEdit.style.height = new_y + "px";
              }
           }
           return false;
        }
    ///**********************************************************************************

}
D3Api.controlsApi['LayoutSplit'] = new D3Api.ControlBaseProperties(D3Api.LayoutSplitCtrl);
//D3Api.controlsApi['Button']['caption']={get:D3Api.ButtonCtrl.getCaption,set:D3Api.ButtonCtrl.setCaption};
//D3Api.controlsApi['Button']['height'] = undefined;
