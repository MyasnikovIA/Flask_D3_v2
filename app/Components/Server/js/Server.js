window.runScript = function(MethodName) {
       var IntervalRunJobMilSec=2000;
       var GlobalIDString="";
       var FunBegin=null;
       var FunCallBack=null;
       var FunProgress=null;
       var async=false;
       var arr=new Array();
       if ((''+window.runScript.arguments[1])=='[object Arguments]') {
          arr.push(window.runScript.arguments[0]);
          for (var ind in window.runScript.arguments[1]) { if (window.runScript.arguments[1][ind]==undefined){continue;} arr.push(window.runScript.arguments[1][ind]); }
       } else {
          for (var ind in window.runScript.arguments) { if (window.runScript.arguments[ind]==undefined){continue;} arr.push(window.runScript.arguments[ind]); }
       }
       var count=0;
       var isCallQuery=false;
       if (arr.length>1) {
            for (ind in arr) {
               count++;
               if (typeof arr[ind] === 'function') {
                  FunCallBack = arr[ind];
                  arr.splice(ind, 1);
               }
            }
            if (FunCallBack != null) {
	            async=true ;
            }
       }
       var data = "WEVENT=" + MethodName.replace(/&amp;/,'&');
       arr.splice(0, 1);
       console.log(JSON.stringify(arr));
       data = data + "&ARGS=" + encodeURIComponent(JSON.stringify(arr));
       var requestRunJob = new XMLHttpRequest();
       requestRunJob.open('POST', 'runScript.php', false);
       requestRunJob.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
       if (async==false) {
           requestRunJob.send(data);
           requestRunJob.ontimeout = function (e) {
               alert('Время ожидания ответа вышло!!!!');
           }
           if (requestRunJob.status !== 200) {
              return {"error":requestRunJob.status}
           }
           retObj=JSON.parse(requestRunJob.responseText);
           for(var  key in retObj) {
               setVar(key, retObj[key]);
           }
           return retObj;
       } else {
           requestRunJob.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                if (typeof FunCallBack === 'function') {
                   retObj=JSON.parse(this.responseText);
                   for(var  key in retObj) {
                       setVar(key, retObj[key]);
                   }
                   FunCallBack(retObj);
                }
             }
           };
           requestRunJob.send(data);
           return requestRunJob;
       }
     }

/**
 *
 * @component
 */
D3Api.ServerCtrl = new function() {
    /**
     *
     * @param dom
     */
    this.init = function(dom){ };
};

D3Api.controlsApi['Server'] = new D3Api.ControlBaseProperties(D3Api.ServerCtrl);
