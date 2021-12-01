package ru.miacomsoft.d3extclient;

import static android.content.Context.MODE_PRIVATE;

import android.annotation.SuppressLint;
import android.app.ProgressDialog;
import android.content.Context;
import android.graphics.Bitmap;
import android.os.Build;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Locale;

import ru.miacomsoft.d3extclient.Lib.Android;
import ru.miacomsoft.d3extclient.Lib.SQLLiteORM;
import ru.miacomsoft.d3extclient.Lib.UserWebChromeClient;
import ru.miacomsoft.d3extclient.Lib.UserWebClient;


public class MainActivity extends AppCompatActivity {
    public static WebView webView ;
    private Button button;
    private Android android; // JS библиотека обращения к модулям устройства Андроид
    private ProgressBar progressBar;
    SQLLiteORM sqlLocal;
    TextToSpeech tts;

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @SuppressLint("JavascriptInterface")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //  webView = new WebView(this);
        button = (Button) findViewById(R.id.button);
        String urlText = loadConfig();
        if (urlText.length()==0){
            setContentView(R.layout.activity_main);
            urlText ="http://128.0.24.172:9091";
            saveConfig(urlText);
        } else {
            runWebClient(urlText);
        }
		// webView.loadUrl("file:///android_asset/mypage.html");
        // webView.reload();
    }

    @Override
    protected void onStart() {
        //android.voice.onStart();
        super.onStart();
    }

    @Override
    protected void onPause() {
        super.onPause();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();

    }


    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public void onClickButton(View v) {
        EditText infoEdit = (EditText) findViewById(R.id.editText);
        String urlText = infoEdit.getText().toString();
        saveConfig(urlText);
        runWebClient(urlText);
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public void runWebClient(String urlText) {
        setContentView(R.layout.web_layout);
        sqlLocal = new SQLLiteORM(this);

        webView = (WebView) findViewById(R.id.webview);
        progressBar = findViewById(R.id.progressBar);
        //webView = new WebView(this);
        //setContentView(webView);
        webView.setWebViewClient(new WebViewClient());
        // webView.setWebChromeClient(new UserWebChromeClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);  // Включить обработчик JS
        android = new Android(this,webView,sqlLocal);
        webView.addJavascriptInterface(android, "Android");
        webView.loadUrl(urlText);
    }

    @Override
    public void onBackPressed() {
        // super.onBackPressed();
        // webView.reload(); // перезагрузить браузер
        setContentView(R.layout.activity_main); //  запуск конфигурации для подключения
        EditText infoEdit = (EditText) findViewById(R.id.editText);
        infoEdit.setText(loadConfig());
    }

    public class WebViewClient extends android.webkit.WebViewClient {
        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            super.onPageStarted(view, url, favicon);
        }
        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            view.loadUrl(url);
            return true;
        }
        @Override
        public void onPageFinished(WebView view, String url) {
            super.onPageFinished(view, url);
            progressBar.setVisibility(View.GONE);
        }
    }


    /*
    //метод для сохранение строки json в файл (создание локальной базы)
    protected void write(String answer) {
        try {
            // отрываем поток для записи
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(this.openFileOutput("config.ini", Context.MODE_PRIVATE)));
            // пишем данные
            bw.write(answer);
            // закрываем поток
            bw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // метод для чтения строки json из файла
    public String readFile() {
        String str = "";
        try {
            // открываем поток для чтения
            BufferedReader br = new BufferedReader(new InputStreamReader(this.openFileInput("config.ini")));
            // читаем содержимое
            str = br.readLine();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
    */

    public void saveConfig(String str) {
        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter( this.openFileOutput("config.ini", MODE_PRIVATE)));
            bw.write(str);
            bw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String loadConfig() {
        StringBuffer res= new StringBuffer();
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader( this.openFileInput("config.ini")));
            String str = "";
            while ((str = br.readLine()) != null) {
                res.append(str);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return res.toString();
    }

}