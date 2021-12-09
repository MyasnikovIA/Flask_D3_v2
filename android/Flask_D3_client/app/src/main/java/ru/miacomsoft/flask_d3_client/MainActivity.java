package ru.miacomsoft.flask_d3_client;

import android.annotation.SuppressLint;
import android.graphics.Bitmap;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
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

import ru.miacomsoft.flask_d3_client.Lib.Android;
import ru.miacomsoft.flask_d3_client.Lib.SQLLiteORM;


public class MainActivity extends AppCompatActivity {
    public static WebView webView ;
    private Button button;
    SQLLiteORM sqlLiteORM;
    ProgressBar progressBar ;


    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @SuppressLint("JavascriptInterface")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.webview_main);
        webView = new WebView(this);
        webView.getSettings().setAppCacheEnabled(true);
        webView.getSettings().setAppCachePath(this.getCacheDir().getPath());
        // webView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);
        webView.getSettings().setCacheMode(WebSettings.LOAD_CACHE_ELSE_NETWORK);
        webView.getSettings().setAppCacheMaxSize(1024*1024*8);

        //webView = (WebView) findViewById(R.id.webView);
        progressBar = (ProgressBar) findViewById(R.id.progressBar);

        setContentView(R.layout.activity_main);
        button = (Button) findViewById(R.id.button);

        sqlLiteORM = new SQLLiteORM(this);
        String urlText = loadConfig();
        if (urlText.length()==0){
            setContentView(R.layout.activity_main);
            urlText ="http://128.0.24.172:9091";
            saveConfig(urlText);
        }else{
            runWebClient(urlText);
        }
        // webView.loadUrl("file:///android_asset/mypage.html");
        // webView.reload();
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
        setContentView(webView);
        //setContentView(R.layout.webview_main);
        webView.setWebViewClient(new WebViewClient());
        // webView.setWebChromeClient(new WebChromeClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);  // Включить обработчик JS
        webView.addJavascriptInterface(new Android(this,webView,sqlLiteORM), "Android");
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


    public void saveConfig(String str) {
        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(openFileOutput("config.ini", MODE_PRIVATE)));
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
            BufferedReader br = new BufferedReader(new InputStreamReader( openFileInput("config.ini")));
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



    public class WebChromeClient extends android.webkit.WebChromeClient {
        public void onProgressChanged(WebView view, int progress) {
             /*
            if(progress < 100 && progressBar.getVisibility() == ProgressBar.GONE){
                progressBar.setVisibility(ProgressBar.VISIBLE);
                txtview.setVisibility(View.VISIBLE);
            }

            progressBar.setProgress(progress);
            if(progress == 100) {
                progressBar.setVisibility(ProgressBar.GONE);
                txtview.setVisibility(View.GONE);
            }
              */
        }
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
            // progressBar.setVisibility(View.GONE);
        }
    }

}