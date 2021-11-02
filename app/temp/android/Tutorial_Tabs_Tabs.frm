<div  cmptype="Base" name="a4e4f2ec3b8b11ec8f570242ac110002" class="Main ActiveDashBoard box-sizing-force"  caption="Пример компонента Tabs (необходимо дописать)"  oncreate="Form.onCreate()"  formName="Tutorial/Tabs/Tabs" >

    <textarea cmptype=Script name="MainScript" style="display:none;">
       
            Form.onCreate = function() {
            }
       
    </textarea>

    
        <div class="tabs"  >
               <input id="tab4d6da72f0d8454939601b0fec3ada6ad0" type="radio"  name="a4e569523b8b11ec8f570242ac110002" > <label for="tab4d6da72f0d8454939601b0fec3ada6ad0" title="Wordpress">Блок 1</label>  <input id="tab4d6da72f0d8454939601b0fec3ada6ad1" type="radio"  name="a4e569523b8b11ec8f570242ac110002" > <label for="tab4d6da72f0d8454939601b0fec3ada6ad1" title="Wordpress">Блок 2</label>  <input id="tab4d6da72f0d8454939601b0fec3ada6ad2" type="radio"  name="a4e569523b8b11ec8f570242ac110002" checked> <label for="tab4d6da72f0d8454939601b0fec3ada6ad2" title="Wordpress">Блок 3</label>
              <section id="content-tab4d6da72f0d8454939601b0fec3ada6ad0" cmptype="TabsItem" name="a4e81d463b8b11ec8f570242ac110002" caption="Блок 1"  >

            содержимое  блока1
        </section>
         <section id="content-tab4d6da72f0d8454939601b0fec3ada6ad1" cmptype="TabsItem" name="a4eaf4bc3b8b11ec8f570242ac110002" caption="Блок 2"  >

            содержимое  блока2
        </section>
         <section id="content-tab4d6da72f0d8454939601b0fec3ada6ad2" cmptype="TabsItem" name="a4eb2a223b8b11ec8f570242ac110002" caption="Блок 3"  active="true"  >

            содержимое  блока3
        </section>
    
            <style>
                 #tab4d6da72f0d8454939601b0fec3ada6ad0:checked ~ #content-tab4d6da72f0d8454939601b0fec3ada6ad0,   #tab4d6da72f0d8454939601b0fec3ada6ad1:checked ~ #content-tab4d6da72f0d8454939601b0fec3ada6ad1,   #tab4d6da72f0d8454939601b0fec3ada6ad2:checked ~ #content-tab4d6da72f0d8454939601b0fec3ada6ad2, 
                #tab9999990:checked ~ #content-tab9999990 
                {  display: block; }
            </style>
        
        </div>

</div>
<div cmptype="sysinfo" style="display:none;"></div>