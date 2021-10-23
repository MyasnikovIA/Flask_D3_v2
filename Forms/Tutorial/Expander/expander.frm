<div cmptype="Form"  name="MAINFORM" caption="" width="60%" height="60%" >
1111111111
   <cmpExpander height="200px" show="false" caption="werqwer" img="Components/Expander/images/arrow_v.png">
       sadfasdfasdf
       asdfasdfasd
       <cmpButton caption="test"/>
       2222222222
   </cmpExpander>
333333

<cmpScript>
  <![CDATA[
    Form.toggleHeight = function(dom, maxHeight) {
        debugger;
        e = document.getElementById("s"); // e = the gray div

        if(e.style.height != '20px') {
            e.style.height = '20px'; // height of one line: 20px
        } else {
            e.style.height = maxHeight + 'px';
        }
    }
   ]]>
</cmpScript>


</div>
