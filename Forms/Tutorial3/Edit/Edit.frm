
<div cmptype="Form" class="Main ActiveDashBoard box-sizing-force" name="MAINFORM" title="Тестовое окно" >
    <!--
        openD3Form('Tutorial/Edit/Edit')
        D3Api.showForm('Tutorial/Edit/Edit', $(".D3MainContainer").get(0), {history: false});
    -->

        <cmpEdit name="FILTER_CONTACT" width="100%"
                    mask_check_regular="^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$"
                    mask_template_regular="^\d*$"
                    trim="true"
        />
    <cmpMask controls="FILTER_CONTACT" />
</div>



