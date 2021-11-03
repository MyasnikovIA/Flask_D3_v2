
D3Api.OpenStreetMapCtrl = new function()
{
    var map;                                              // слой карты
    var markers;        // слой маркеров
    var fromProjection;  // Transform from WGS 1984
    var toProjection;  // to Spherical Mercator Projection
    var click;
    var uniqid ; // Уникальный ID  сомпонента(генерируется)
    this.init = function(_dom)
    {
        var uniqid = _dom.getAttribute("uniqid")

        var mapBodyConteyner = _dom.querySelector('.MapContent'+uniqid);
        if (mapBodyConteyner) {
             setTimeout(function sayHi() {
                _dom.querySelector('.olControlAttribution').style.display="none"; // убираем  логотип OSM

               // Добавить кнопки + - по селекторам
               //   + olControlZoomIn olButton
               //   - olControlZoomOut olButton
             }, 200);
             /*
                 console.log(_dom.parentNode);
                 console.log(_dom.parentNode.parentNode);
                 console.log(_dom.parentNode.parentNode.getBoundingClientRect());
             */
             var rectPar = _dom.parentNode.getBoundingClientRect();
             var height = _dom.getAttribute("height")
             var width = _dom.getAttribute("width")
             if (!width){
                mapBodyConteyner.style.height = rectPar.height + "px";
                _dom.style.height = rectPar.height + "px";
             }

             if (!height){
                mapBodyConteyner.style.height = rectPar.height + "px";
                _dom.style.height = rectPar.height + "px";
             }
             /*
                 blockEdit.style.left =  rect.left + "px";
                 blockEdit.style.top =  rect.top + "px";
                 rect = _dom.getBoundingClientRect();
                 mapBodyConteyner.style.width = rect.width + "px";
                 mapBodyConteyner.style.height = rect.height + "px";
                 console.log(mapBodyConteyner)
             */

        }


        markers = new OpenLayers.Layer.Markers("Markers");        // слой маркеров
		fromProjection = new OpenLayers.Projection('EPSG:4326');  // Transform from WGS 1984
		toProjection = new OpenLayers.Projection('EPSG:900913');  // to Spherical Mercator Projection
        map = new OpenLayers.Map('basicMap'+uniqid);
        map.addLayer(markers);
        var mapnik = new OpenLayers.Layer.OSM();
        var position = new OpenLayers.LonLat(83.03330, 54.97525).transform(fromProjection, toProjection);
        var zoom = 15;
        map.addLayer(mapnik);
        map.setCenter(position, zoom);
        OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {
						defaultHandlerOptions: {
							'single': true,
							'double': false,
							'pixelTolerance': 0,
							'stopSingle': false,
							'stopDouble': false
			},
            initialize: function (options) {
                this.handlerOptions = OpenLayers.Util.extend({}, this.defaultHandlerOptions);
                OpenLayers.Control.prototype.initialize.apply(this, arguments);
                this.handler = new OpenLayers.Handler.Click(this, {'click': this.trigger}, this.handlerOptions);
            },
            trigger: function (event) {
                var lonlat = map.getLonLatFromViewPortPx(event.xy)
                lonlat.transform(new OpenLayers.Projection('EPSG:900913'), new OpenLayers.Projection('EPSG:4326'));
                var locatObjUrl = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + lonlat.lat + "&lon=" + lonlat.lon + "&zoom=18&addressdetails=1";
				D3Api.OpenStreetMapCtrl.ajax_get(locatObjUrl, function (data, status,...args) {
				     console.log("Дописать метод обработки полученной информации о геоданных 'onclickmap':")
				     console.log("data",data)
				     var codeOnclick = _dom.getAttribute("onclickmap")
                     _dom.D3Form.execDomEventFunc(_dom, {func: codeOnclick, args: data});
                     //chk = _dom.D3Form.execDomEventFunc(ctrl, {func: desc[2], args: 'value'});
				     //form.execDomEventFunc(dom, {func: prop, args: 'clone'}));
				     //dom.D3Dependences.repeater.addEvent('onclone_remove',function(){D3Api.DependencesCtrl.refresh(dom);});
				     //var codeOnclick = _dom.getAttribute("onclickmap")
				     //codeOnclick && eval(codeOnclick) // переписать
                });
            }
        });
        click = new OpenLayers.Control.Click();
        map.addControl(click);
        click.activate();
    }


     // Процедура поиска Гео-объекта по фразе
     // @param foundObj
     this.getGisObjest = function (foundObj,callback) {
         var urlLoad = 'http://nominatim.openstreetmap.org/?format=json&addressdetails=1&q=' + encodeURIComponent(foundObj);
         var data = this.ajax_get(urlLoad);
         if (typeof data === 'object' ){
                // Рисуем метки
                for (var ind in data) {
                    var position = new OpenLayers.LonLat(data[ind].lon, data[ind].lat).transform(fromProjection, toProjection);
                    markers.addMarker(new OpenLayers.Marker(position));
                }
                // перемезаемся на первую точку
                if (data[0]){
                    var position = new OpenLayers.LonLat(data[0].lon, data[0].lat).transform(fromProjection, toProjection);
                    map.setCenter(position);
                }
          }
         return data;
     }

    this.setLocate = function TextArea_SetValue(_dom,_value)
    {
        //_dom = D3Api.getChildTag(_dom,'textarea',0);
        //_dom.value = (_value == null)?'':_value;
    }

    this.getLocate = function TextArea_GetValue(_dom)
    {
        return {};
    }
    this.ajax_get = function(url, callback,...args) {
        var xmlhttp = new XMLHttpRequest();
        if (callback) {
            xmlhttp.onreadystatechange = function() {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    // console.log('responseText:' + xmlhttp.responseText);
                    try {
                        var data = JSON.parse(xmlhttp.responseText);
                    } catch(err) {
                        console.log(err.message + " in " + xmlhttp.responseText);
                    }
                    callback && callback(data,xmlhttp.status,...args);
                }
            };
            xmlhttp.open("GET", url, true);
            xmlhttp.send();
        } else{
            xmlhttp.open("GET", url, false);
            xmlhttp.send();
            // 4. Если код ответа сервера не 200, то это ошибка
            if (xmlhttp.status != 200) {
              // обработать ошибку
              return statusText;
            } else {
                 try {
                     return JSON.parse(xmlhttp.responseText);
                 } catch(err) {
                    return xmlhttp.responseText;
                 }
            }
        }
	}
}

D3Api.controlsApi['OpenStreetMap'] = new D3Api.ControlBaseProperties(D3Api.OpenStreetMapCtrl);
// D3Api.controlsApi['OpenStreetMap']['locate']={get:D3Api.OpenStreetMapCtrl.setLocate,set:D3Api.TextAreaCtrl.setLocate};
// D3Api.controlsApi['OpenStreetMap']['value']={get:D3Api.OpenStreetMapCtrl.getValue,set:D3Api.TextAreaCtrl.setValue};
// D3Api.controlsApi['OpenStreetMap']['enabled'].set = D3Api.OpenStreetMapCtrl.setEnabled;
// D3Api.controlsApi['OpenStreetMap']['input']={get: D3Api.OpenStreetMapCtrl.getInput, type: 'dom'};
