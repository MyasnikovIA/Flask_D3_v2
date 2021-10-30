<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="Тестовое окно" >
    <cmpScript name="MainScript">
       <![CDATA[
            Form.onCreate = function() {
            }
       ]]>
    </cmpScript>

<div cmptype="PageControl" name="cmp617c7ebf2ce7f" title="" tabindex="0" class="ctrl_pageControl bg box-sizing-force"  uniqid="pc617c7ebf2ceb6" mode="horizontal" id="d3ctrl101635548858541">
    <div cont="div_ul" class="div_ul box-sizing-force">
        <ul cont="PageControl_head" class="ctrl_pageControlTabs bg" style="left: 0px;">
            <li class="ctrl_pageControlTabBtn tab0_pc617c7ebf2ceb6 active" pageindex="0" cmptype="TabSheet" name="cmp617c7ebf2dbaf" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl131635548858541"><a class="centerTB" cont="tabcaption">1111111111</a></li>
            <li class="ctrl_pageControlTabBtn tab1_pc617c7ebf2ceb6  " pageindex="1" cmptype="TabSheet" name="cmp617c7ebf2e608" title="" onclick="D3Api.PageControlCtrl.showTab(this);" id="d3ctrl161635548858541"><a class="centerTB" cont="tabcaption">22222222</a></li>
        </ul>
        <div cont="ScrollNext" class="button_scroll next_scroll" onclick="D3Api.PageControlCtrl.ScrollNext(this);" style="display: none;"></div>
        <div cont="ScrollPrior" class="button_scroll prior_scroll" onclick="D3Api.PageControlCtrl.ScrollPrior(this);" style="display: none;"></div>
    </div>

    <div cont="page0_pc617c7ebf2ceb6" class="ctrl_pageControlTabPage page0_pc617c7ebf2ceb6 " style="display: block;">
        содержимое1111
    </div>
    <div cont="page1_pc617c7ebf2ceb6" class="ctrl_pageControlTabPage page1_pc617c7ebf2ceb6 ">
        содержимое2222
    </div>
</div>

</cmpForm>

