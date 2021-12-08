package ru.miacomsoft.flask_d3_client.Lib;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.hardware.Sensor;
import android.net.Uri;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.text.format.Formatter;
import android.util.Log;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebView;
import android.widget.Toast;

import androidx.annotation.RequiresApi;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.List;

import ru.miacomsoft.flask_d3_client.MainActivity;


/**
 * Created by MyasnikovIA on 01.06.17.
 * Диалоговые окна
 * http://developer.alexanderklimov.ru/android/alertdialog.php
 */
public class Android {
    private long lastUpdate;
    private WebView webView;
    private SQLLiteORM sqlLocal;
    private GPSTracker gPSTracker; // Получение положения GPS сигнала
    List<Sensor> mList;
//       webView.loadUrl("javascript: Accel="+jsonObject.toString()   );

    private MainActivity parentActivity;

    @SuppressLint("NewApi")
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public Android(MainActivity activity, WebView webViewPar,SQLLiteORM sqlLocal) {
        webView = webViewPar;
        parentActivity = activity;
        lastUpdate = System.currentTimeMillis();
        this.sqlLocal =sqlLocal;
        gPSTracker = new GPSTracker(activity,webView);

        /**
         * This is an approved way to pass data back to the html page
         */
        webView.evaluateJavascript("alert('pass here some ...')", new ValueCallback<String>() {
            @Override
            public void onReceiveValue(String s) {

            }
        });
        // webView.loadUrl("javascript: window.RecognizerText = function(text){ console.log('RecognizerText',text); };");
    }


    /** Show a toast from the web page */
    @JavascriptInterface
    public void showToast(String toast) {
        Toast.makeText(parentActivity.getBaseContext(), toast, Toast.LENGTH_SHORT).show();
    }

    /**
     *  Вывод консоли
     * @param msg
     */
    @JavascriptInterface
    public void console_log(String msg){
        Log.d("console.log", msg);
    }

    /**
     *  Вывод консоли
     * @param msg
     */
    @JavascriptInterface
    public void log(String msg){
        Log.d("console.log", msg);
    }

    /**
     * Переход в браузер
     * @param UrlStr - строка запроса
     */
    @JavascriptInterface
    public void getBrouser(String UrlStr){
        if( (UrlStr.toLowerCase().indexOf("http://") == -1) &&(UrlStr.toLowerCase().indexOf("https://") == -1))
        {
            UrlStr+="http://";
        }
        Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(UrlStr)) ;
        parentActivity.startActivity(browserIntent);
    }

    /**
     * Запись текста в файл
     * @param Str
     * @param FileName
     */
    @JavascriptInterface
    public void writeFile(String Str,String FileName){
        try {
            // отрываем поток для записи
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter( parentActivity.openFileOutput(FileName,  parentActivity.MODE_PRIVATE)));
            // пишем данные
            bw.write(Str);
            // закрываем поток
            bw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * Чтение текстового файла
     * @param FileName
     * @return
     */
    @JavascriptInterface
    public String readFile(String FileName){
        StringBuffer sb = new StringBuffer();
        try {
            // открываем поток для чтения
            BufferedReader br = new BufferedReader(new InputStreamReader(parentActivity.openFileInput(FileName)));
            String str = "";
            // читаем содержимое
            while ((str = br.readLine()) != null) {
                sb.append(str);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return   sb.toString();
    }

    /**
     *  JS функция вывода сообщения во вст\плывающем окне
     * @param msg
     */
    @JavascriptInterface
    public void alert(String msg){
        //  Toast.makeText(parentActivity, msg, Toast.LENGTH_LONG).show();
        new AlertDialog.Builder(parentActivity)
                .setMessage(msg)
                //.setTitle(title)
                .setIcon(android.R.drawable.ic_dialog_alert)
                .setCancelable(false)
                .setPositiveButton("OK",
                        new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int id) {
                                // setResult(RESULT_CANCELED);
                                // finish();
                            }
                        }).show();
    }

    @JavascriptInterface
    public String getIP(){
        WifiManager wifiMgr1 = (WifiManager) parentActivity.getApplicationContext() .getSystemService(parentActivity .WIFI_SERVICE);
        WifiInfo wifiInfo1 = wifiMgr1.getConnectionInfo();
        int ip = wifiInfo1.getIpAddress();
        String ipAddress = Formatter.formatIpAddress(ip);
        return ipAddress;
    }
/// ===============================================================
/// ----------------------------SQL lite --------------------------
/// ===============================================================
    /***
     * Провенрка наличия таблицы в локальной SQLlite БД
     * @param tableName
     * @return
     */
    @JavascriptInterface
    public boolean getIsExistTab(String tableName) {
        return sqlLocal.getIsExistTab(tableName);
    }

    /**
     *  Получить запись с указанным ID номером из Таблицы
     * @param tableName - имя таблицы
     * @param id - идентификатор записи
     * @return - JSON объект
     */
    @JavascriptInterface
    public JSONObject getJson(String tableName,long id) {
       return sqlLocal.getJson(tableName, id);
    }

    /***
     * Вставить JSON объект в таблицу
     * @param tableName
     * @param json
     * @return
     */
    @JavascriptInterface
    public long insertJson(String tableName, String json) {
        JSONObject jsonOnj = null;
        try {
            jsonOnj = new JSONObject(json);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return sqlLocal.insertJson(tableName, jsonOnj);
    }

    /***
     * Обновить JSON объект в таблицу ( если записи с ID нет, или таблицы, тогда  создастся таблица и добавиться запись
     * @param tableName
     * @param json
     * @return
     */
    @JavascriptInterface
    public boolean updateJsonSQL(String tableName, JSONObject json) {
        return sqlLocal.updateJson(tableName, json);
    }

    /***
     * Удаление таблицы
     * @param tableName
     */
    @JavascriptInterface
    public void dropTable(String tableName) {
        sqlLocal.dropTable(tableName);
    }

    /***
     *  Получить массив объектов  из таблици по условию
     * @param tableName - Имя таблицы
     * @param where - SQL условие
     * @return
     */
    @JavascriptInterface
    public JSONArray getJsonArray(String tableName , String where) {
        if (where.length()>0) {
            where =" where "+where;
        }
        return sqlLocal.sql("select * from "+tableName+where,null);
    }

    /***
     *  Получить массив объектов из SQL запроса
     * @param SQLtext - SQL запрос
     * @return
     */
    @JavascriptInterface
    public JSONArray SQL(String SQLtext) {
        return sqlLocal.sql(SQLtext,null);
    }

/// ===============================================================
/// ================Работа с GPS ==================================
/// ===============================================================


    @JavascriptInterface
    public boolean startLocation(String provider) {
        if (provider == "net"){
             return gPSTracker.startNetworkLocation();
        }
        if (provider == "gps"){
            return gPSTracker.startGpsLocation();
        }
        return gPSTracker.startGpsLocation();
    }

    @JavascriptInterface
    public void setGpsNetSettings(String provider) {
        gPSTracker.setSettings();
    }


    @JavascriptInterface
    public String getGPS(String provider) {
        return gPSTracker.getGPS();
    }

    @JavascriptInterface
    public String getNetGPS(String provider) {
        return gPSTracker.getNetGPS();
    }


/// ===============================================================
/// ===============================================================
/// ===============================================================

}
