<cmpForm class="Main ActiveDashBoard box-sizing-force"  oncreate="Form.onCreate()" caption="Радактор форм (форма в разработке)" >
    <cmpScript name="MainScript">
       <![CDATA[
          Form.blankName = "Forms/FormDesugner/blank";
          Form.onCreate = function() {
          }

          Form.onCloneBeforeComponent = function (data) {
                //console.log("onCloneBeforeComponent",data)
                //getValue("FiltrComp");
		  }
          Form.onAfterCloneComponent = function (clone, data) {
               if ( getValue("FiltrComp").length>0 ) {
                   if (!data.FULLNAME.toLowerCase().includes(getValue("FiltrComp").toLowerCase())) {
                     clone.style.display="none";
                   }
               }
               console.log("onAfterClone",data)
          }

       ]]>
    </cmpScript>
    <cmpDataSet name="DS_GET_CMP_LIST" query_type="server_python"  activateoncreate="true">
        fileDir=f"""{session["AgentInfo"]['ROOT_DIR']}/Components{os.sep}"""
        files = os.listdir(fileDir)
        ID = -1
        data = []
        for comp in files:
            ID+=1
            data.append({"ID":ID,"FULLNAME":comp})
        data
        <cmpDataSetVar name="form_params" src="form_params" srctype="var"/>
    </cmpDataSet>



   <cmpToolbar  name="tlb_Ctrl" style="bottom: 20px;">
        <cmpToolbarItemGroup align="left">
              <cmpButton caption="Сохранить форму"  width="50px"/>
              <cmpButton caption="Запустить форму"  width="50px"/>
        </cmpToolbarItemGroup>
        <cmpToolbarItemGroup align="right">

        </cmpToolbarItemGroup>
        <cmpToolbarItemGroup>

        </cmpToolbarItemGroup>
    </cmpToolbar>


    <cmpLayout name="MyLayout"  style="height:95%">

        <!-- контейнер -->
        <cmpLayoutContainer   style="width:300px;">
                <cmpTabs>
                    <cmpTabsItem caption="DOM" active="true">
                        <cmpEdit placeholder="Фильтр DOM дерева" />
                    </cmpTabsItem>
                    <cmpTabsItem caption="Компоненты" >
                       <cmpEdit name="FiltrComp" placeholder="Фильтр компонентов"  onkeydown="if (event.keyCode == 13){refreshDataSet('DS_GET_CMP_LIST'); }" />
                       <div  style="height:50%;" >
                           <div dataset="DS_GET_CMP_LIST" repeat="0" keyfield="ID"  repeatername="rpter" onbefore_clone="Form.onCloneBeforeComponent();" onafter_clone="Form.onAfterCloneComponent(clone, data);">
                               <cmpButton   data="value:ID;caption:FULLNAME" />
                           </div>
                       </div>
                    </cmpTabsItem>
                </cmpTabs>
       </cmpLayoutContainer>


            <!-- Разделительны элемент (вертикальный) -->
            <cmpLayoutSplit orientation="vertical"/>


        <!-- Сентральная панель -->
        <cmpLayoutContainer name="centerPanel" >

        </cmpLayoutContainer>


            <!-- Разделительны элемент (вертикальный) -->
            <cmpLayoutSplit orientation="vertical"/>


            <!-- Правая панель -->
            <cmpLayoutContainer name="" style="width:350px">
                <cmpTabs>
                    <cmpTabsItem caption="Cвойства" active="true">
                        <cmpEdit placeholder="Фильтр свойст" />
                    </cmpTabsItem>
                    <cmpTabsItem caption="Стили" >
                        <cmpEdit placeholder="Фильтр стилей" />
                    </cmpTabsItem>
                    <cmpTabsItem caption="События" >
                        <cmpEdit placeholder="Фильтр событий" />
                    </cmpTabsItem>
                </cmpTabs>
            </cmpLayoutContainer>
        <!-- Разделительны элемент (горизонтальный) -->
        <!--
        <cmpLayoutSplit orientation="horizon" direction="top"/>
        <cmpLayoutContainer  colspan="25"  style="height:25px" >
            Нижняя панель
        </cmpLayoutContainer>
        -->
    </cmpLayout>
</cmpForm>

