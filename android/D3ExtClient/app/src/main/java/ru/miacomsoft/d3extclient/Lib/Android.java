package ru.miacomsoft.d3extclient.Lib;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.hardware.Sensor;
import android.net.Uri;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.text.format.Formatter;
import android.webkit.WebView;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.List;

import ru.miacomsoft.d3extclient.MainActivity;

/**
 * Created by MyasnikovIA on 01.06.17.
 * Диалоговые окна
 * http://developer.alexanderklimov.ru/android/alertdialog.php
 */
public class Android {
    private long lastUpdate;
    private WebView webView;
    List<Sensor> mList;
//       webView.loadUrl("javascript: Accel="+jsonObject.toString()   );


    private MainActivity parentActivity;
    public Android(MainActivity activity, WebView webViewPar)  {
        webView=webViewPar;
        parentActivity = activity;
        lastUpdate = System.currentTimeMillis();
    }

    /**
     * Переход в браузер
     * @param UrlStr - строка запроса
     */
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

    public String getIP(){
        WifiManager wifiMgr1 = (WifiManager) parentActivity.getApplicationContext() .getSystemService(parentActivity .WIFI_SERVICE);
        WifiInfo wifiInfo1 = wifiMgr1.getConnectionInfo();
        int ip = wifiInfo1.getIpAddress();
        String ipAddress = Formatter.formatIpAddress(ip);
        return ipAddress;
    }





}
