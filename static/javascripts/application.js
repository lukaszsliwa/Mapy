    var map = null;
    var geocoder = null;
    var poly = null;
    var options = { geodesic: true };
    var color = "#FF0000";
    var marker = null;
    var markset = false;
    var mapsset = false;
    var markers = [];
    var listeners = [];
    var maps = [];
    var mapslisteners = [];
    var mgr = null;

    function init() {
      if (GBrowserIsCompatible()) {
        map = new GMap2(document.getElementById("map"));
        geocoder = new GClientGeocoder();
        map.setCenter(new GLatLng(52.32191088594773, 19.072265625), 6);
        map.setUIToDefault();
        map.enableRotation();
	mgr = new MarkerManager(map);

        poly = new GPolyline([], color);
	map.addControl(new TextualZoomControl());

      }
    }

    function init_marker() {
	if(marker == null) {
          var micon = new GIcon();
	  micon.image = "/static/images/sc-star.png";
	  micon.iconSize = new GSize(30,30);
	  micon.iconAnchor = new GPoint(15, 20);

	  marker = new GMarker(map.getCenter(), { icon : micon, draggable: true});
	  GEvent.addListener(marker, "dragstart", function() {
 	    map.closeInfoWindow();
  	  });
	  GEvent.addListener(marker, "dblclick", function() {
            openPointsDialog();
  	  });
	  map.addOverlay(marker);	
	} else {
	  marker.setLatLng(map.getCenter());
	}
    }
    function openPointsDialog() {
	if (marker != null){
	    var latlng = marker.getLatLng();
            $('#id_latit').val(latlng.lat());
            $('#id_longi').val(latlng.lng());
	    $('#dialog-point').dialog('open');
	}
    }



    function search(address) {
      if(geocoder) {
        geocoder.getLatLng(
          address,
          function(point) {
            if(!point) {
              alert("Nie znaleziono " + address);
            } else {
              map.setCenter(point, 13);
            }
          }
        );
      }
    }

    function km() {
        var length = Math.round(poly.getLength() / 10) / 100;
        $('#length').html(length + " km");
        $('#id_distance').val(length);
    }

    function start() {
        draw(poly, km);
    }

    function stop() {
        poly.disableEditing();
    }

    function draw(poly, onUpdate) {
      map.addOverlay(poly);
      poly.enableDrawing(options);
      poly.enableEditing({onEvent: "mouseover"});
      poly.disableEditing({onEvent: "mouseout"});
      GEvent.addListener(poly, "lineupdated", onUpdate);
      GEvent.addListener(poly, "endline", function() {
        GEvent.addListener(poly, "click", function(latlng, index) {
          if (typeof index == "number") {
              if (poly.getVertexCount() > 2)
                poly.deleteVertex(index);
              else
                poly.enableDrawing(options);
          }
        });
      });
    }

    function latlngsToString(poly) {
        var str = "";
        for(i = 0; i < poly.getVertexCount(); i++) {
            str += poly.getVertex(i).lat() + ',' + poly.getVertex(i).lng() + ';';
        }
        return str;
    }

function TextualZoomControl() {
}

TextualZoomControl.prototype = new GControl();

TextualZoomControl.prototype.initialize = function(map) {
  var container = document.createElement("div");

  var zoomInDiv = document.createElement("div");
  zoomInDiv.setAttribute("id","points_button");
  this.setButtonStyle_(zoomInDiv);
  container.appendChild(zoomInDiv);
  zoomInDiv.appendChild(document.createTextNode("Punkty"));
  GEvent.addDomListener(zoomInDiv, "click", function() {
	if(markset){ 
		markset = false;
		destroyPoints();
		document.getElementById("points_button").style.backgroundColor = "white";
	} else { 
		markset = true; 
		importPoints(); 
		document.getElementById("points_button").style.backgroundColor = "yellow";
	}
  });


  var zoomOutDiv = document.createElement("div");
  zoomOutDiv.setAttribute("id","traces_button");
  this.setButtonStyle_(zoomOutDiv);
  container.appendChild(zoomOutDiv);
  zoomOutDiv.appendChild(document.createTextNode("Trasy"));
  GEvent.addDomListener(zoomOutDiv, "click", function() {
	if(mapsset){ 
		mapsset = false;
		destroyMaps();
		document.getElementById("traces_button").style.backgroundColor = "white";
	} else {
		if(map.getZoom() > 11) {
			mapsset = true;
			importMaps();
			document.getElementById("traces_button").style.backgroundColor = "yellow";
		} 
	}
  });

  map.getContainer().appendChild(container);
  return container;
}

TextualZoomControl.prototype.getDefaultPosition = function() {
  return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(7, 7));
}

TextualZoomControl.prototype.setButtonStyle_ = function(button) {
  button.style.backgroundColor = "white";
  button.style.font = "small Arial";
  button.style.border = "1px solid black";
  button.style.padding = "2px";
  button.style.marginTop = "35px";
  button.style.marginBottom = "-30px";
  button.style.textAlign = "center";
  button.style.width = "6em";
  button.style.cursor = "pointer";
}

 function importMaps() {
    maps = [];
    mapslisteners = [];
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    $.getJSON("/mapy/"+SW.lat()+"/"+SW.lng()+"/"+NE.lat()+"/"+NE.lng()+"/",
        function(data){
          $.each(data.maps, function(i,item){
	    var new_map = [];
	    $.each(item.latlngs, function(i,mitem){
		new_map.push(new GLatLng(mitem[0],mitem[1]));
	    });
	    var poly2 = new GPolyline(new_map, color, 2, 0.7);
	    var evlis = GEvent.addListener(poly2, "click", function() {
	    	window.location = 'mapy/' + item.id + '/' + item.slug+'/';
  	      });
            map.addOverlay(poly2);
	    maps.push( poly2 );
	    mapslisteners.push( evlis );
          });
        });
  }

  function destroyMaps() {
	for ( i in maps ){
		map.removeOverlay(maps[i]);
	}
	for ( i in mapslisteners ){
		GEvent.removeListener(mapslisteners[i]);
	}
  }

 function importPoints() {
    markers = [];
    listeners = [];
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    $.getJSON("/punkt/"+SW.lat()+"/"+SW.lng()+"/"+NE.lat()+"/"+NE.lng()+"/",
        function(data){
          $.each(data.points, function(i,item){
	    var point = new GMarker(new GLatLng(item.lat,item.lng));
	    var evlis = GEvent.addListener(point, "click", function() {
	    	point.openInfoWindowHtml(item.desc);
  	      });
	    markers.push( point );
	    listeners.push(evlis);
          });
     	mgr.addMarkers(markers.slice(0,markers.length/2),6);
     	mgr.addMarkers(markers,11);
        mgr.refresh();
        });
  }

  function destroyPoints() {
	mgr.clearMarkers();
	for ( i in listeners ){
		GEvent.removeListener(listeners[i]);
	}
  }

