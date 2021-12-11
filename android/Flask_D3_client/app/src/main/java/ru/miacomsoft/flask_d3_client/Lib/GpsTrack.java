package ru.miacomsoft.flask_d3_client.Lib;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.GpsStatus;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.webkit.WebView;
import android.widget.TextView;

import androidx.annotation.RequiresApi;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Locale;

import ru.miacomsoft.flask_d3_client.MainActivity;

public class GpsTrack {
    /*
       // добавить в MainActivity
       public static final int REQUEST_PERMISSION_LOCATION = 255; // int should be between 0 and 255  // Идентификатор вызова окна  разрешения  доступа к GPS данным

       @Override
       public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
           super.onRequestPermissionsResult(requestCode, permissions, grantResults);
           if (requestCode == REQUEST_PERMISSION_LOCATION) {
               if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                   // Включение доступ к GPS
                   // gps1 = new gps(context);
               }
           }
       }

   */
    private static final long MINIMUM_DISTANCE_CHANGE_FOR_UPDATES = 1;  // ТОчность позицианирования
    private static final long MINIMUM_TIME_BETWEEN_UPDATES = 3000;      // Через какое время опрашивать датчик в милисекундах

    private MainActivity activity;
    private Context context;
    private WebView webView;
    private SQLLiteORM sqlLocal;

    private LocationManager LM;
    private MyLocationListener myLocationListener;

    public double lon = 0;
    public double lat = 0;
    public String NMEA;

    public StringBuffer NMEAtmp;
    private String CallbackFunctionText="";
    private JSONObject jsonResult ;

    public GpsTrack(MainActivity activity, WebView webView, SQLLiteORM sqlLocal) {
        this.activity = activity;
        this.context = activity.getBaseContext();
        this.webView = webView;
        this.sqlLocal = sqlLocal;
        LM = (LocationManager) this.activity.getSystemService(Context.LOCATION_SERVICE);
        myLocationListener = new MyLocationListener();
        NMEAtmp = new StringBuffer("");
        jsonResult = new JSONObject();
        NMEA = "";
    }

    public void setGpsCallback(String functionText) {
        CallbackFunctionText = functionText;
    }


    @SuppressLint({"NewApi", "MissingPermission"})
    public boolean setGpsSetings() {
        ActivityCompat.requestPermissions(activity,new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);
        if (ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            activity.requestPermissions(new String[]{Manifest.permission.ACCESS_COARSE_LOCATION}, MainActivity.REQUEST_PERMISSION_LOCATION);
            Log.v("MainActivity", "------------true-----------");
            return true;
        }
        Log.v("MainActivity", "------------false-----------");
        return false;
    }

    @SuppressLint({"NewApi", "MissingPermission"})
    public void startGPS() {
        setGpsSetings();
        LM.requestLocationUpdates(LocationManager.GPS_PROVIDER, MINIMUM_TIME_BETWEEN_UPDATES, MINIMUM_DISTANCE_CHANGE_FOR_UPDATES, myLocationListener);
        LM.addNmeaListener(new GpsStatus.NmeaListener() {
            public void onNmeaReceived(long timestamp, String nmea) {
                String lowerNmea = nmea.toLowerCase(Locale.ENGLISH);
                if (nmea.startsWith("$GPGSA")) {
                    // tv2.setText("\n-------------------------\n");
                    Log.v("MainActivity", "-----------------------");
                    NMEA = NMEAtmp.toString();
                    if (CallbackFunctionText.length()>0){
                        try {
                            jsonResult.put("lon", lon);
                            jsonResult.put("NMEA", NMEAtmp.toString());
                            jsonResult.put("lat", lat);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                        Log.v("MainActivity", "javascript: "+CallbackFunctionText+"("+jsonResult.toString()+"); ");
                        /*
                        new Handler(Looper.getMainLooper()).post(new Runnable() {
                            @Override
                            public void run() {
                                webView.loadUrl("javascript: "+CallbackFunctionText+"('"+jsonResult.toString()+"');");
                            }
                        });
                         */
                    }
                    NMEAtmp.setLength(0);
                    NMEAtmp.append("Timestamp:"+String.valueOf(timestamp)+"\r\n");
                }
                NMEAtmp.append(nmea);
                Log.v("MainActivity", nmea);
                /*
                     http://yug-gps.narod.ru/docs/000x/st007.htm

                    2021-12-10 09:37:08.463 12979-12979/? V/MainActivity: -----------------------
                    2021-12-10 09:37:08.464 12979-12979/? V/MainActivity: $GPGSA,A,1,,,,,,,,,,,,,,,*1E
                    2021-12-10 09:37:08.465 12979-12979/? V/MainActivity: $GNGSA,A,1,,,,,,,,,,,,,,,*00
                    2021-12-10 09:37:08.468 12979-12979/? V/MainActivity: $PQGSA,A,1,,,,,,,,,,,,,,,*08
                    2021-12-10 09:37:08.469 12979-12979/? V/MainActivity: $GPVTG,,T,,M,,N,,K,N*2C
                    2021-12-10 09:37:08.470 12979-12979/? V/MainActivity: $GPRMC,,V,,,,,,,,,,N*53
                    2021-12-10 09:37:08.471 12979-12979/? V/MainActivity: $GPGGA,,,,,,0,,,,,,,,*66
                    2021-12-10 09:37:09.420 12979-12979/? V/MainActivity: $GPGSV,3,1,10,08,21,281,,10,87,324,,14,02,358,,15,08,063,*71
                    2021-12-10 09:37:09.458 12979-12979/? V/MainActivity: $GPGSV,3,2,10,18,14,158,,21,21,314,,23,53,104,,24,41,075,*7C
                    2021-12-10 09:37:09.461 12979-12979/? V/MainActivity: $GPGSV,3,3,10,27,16,248,,32,45,227,*73
                    2021-12-10 09:37:09.464 12979-12979/? V/MainActivity: $GLGSV,2,1,08,74,07,002,,66,71,026,,82,53,278,,76,19,112,*60
                    2021-12-10 09:37:09.466 12979-12979/? V/MainActivity: $GLGSV,2,2,08,65,15,070,,83,24,330,,81,33,206,,67,42,268,*66
                    2021-12-10 09:37:09.471 12979-12979/? V/MainActivity: $GAGSV,1,1,0,*74
                    2021-12-10 09:37:09.473 12979-12979/? V/MainActivity: $PQGSV,1,1,0,*73
                    2021-12-10 09:37:09.475 12979-12979/? V/MainActivity: $PQGSV,1,1,0,*73
                    2021-12-10 09:37:09.477 12979-12979/? V/MainActivity: -----------------------
                */
            }
        });
    }

    public String getLocation() {
        try {
            jsonResult.put("lon", lon);
            jsonResult.put("NMEA", NMEAtmp.toString());
            jsonResult.put("lat", lat);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonResult.toString();
    }

    public void stopGPS() {
        if (LM != null) {
            LM.removeUpdates(myLocationListener);
        }
    }

    private class MyLocationListener implements LocationListener {
        @Override
        public void onLocationChanged(Location location) {
            lon = location.getLongitude();
            lat = location.getLatitude();
        }

        @Override
        public void onProviderDisabled(String provider) {

        }

        @Override
        public void onProviderEnabled(String provider) {

        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {

        }
    }

}
