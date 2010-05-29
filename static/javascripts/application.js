    var map = null;
    var geocoder = null;
    var poly = null;
    var options = { geodesic: true };
    var color = "#FF0000";
    var marker = null;

    function init() {
      if (GBrowserIsCompatible()) {

        map = new GMap2(document.getElementById("map"));
        geocoder = new GClientGeocoder();
        map.setCenter(new GLatLng(52.32191088594773, 19.072265625), 6);
        map.setUIToDefault();
        map.enableRotation();

        poly = new GPolyline([], color);
      }
    }

    function init_marker() {
	if(marker == null) {
	  marker = new GMarker(map.getCenter(), {draggable: true});
	
	  GEvent.addListener(marker, "dragstart", function() {
 	    map.closeInfoWindow();
  	  });

	  GEvent.addListener(marker, "dblclick", function() {
	    //marker.openInfoWindowHtml("lol");
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
