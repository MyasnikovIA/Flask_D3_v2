package ru.miacomsoft.d3extclient;

import android.annotation.SuppressLint;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import ru.miacomsoft.d3extclient.Lib.Android;
import ru.miacomsoft.d3extclient.Lib.UserWebChromeClient;
import ru.miacomsoft.d3extclient.Lib.UserWebClient;

public class MainActivity extends AppCompatActivity {
    public static WebView webView ;
    private Button button;

    @RequiresApi(api = Build.VERSION_CODES.O)
    @SuppressLint("JavascriptInterface")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String urlText = loadConfig();
        if (urlText.length()==0){
            urlText ="http://128.0.24.172:9091";
            saveConfig(urlText);
            button = (Button) findViewById(R.id.button);
            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    EditText infoEdit = (EditText) findViewById(R.id.editText);
                    String urlText = infoEdit.toString();
                    saveConfig(urlText);
                    runWebClient(urlText);
                }
            });
        }else{
            runWebClient(urlText);
        }
		// webView.loadUrl("file:///android_asset/mypage.html");
        // webView.reload();
    }

    public void runWebClient(String urlText){
        webView = new WebView(this);
        webView.setWebViewClient(new UserWebClient());
        webView.setWebChromeClient(new UserWebChromeClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);  // Включить обработчик JS
        webView.addJavascriptInterface(new Android(this,webView), "Android");
        setContentView(webView);
        webView.loadUrl(urlText);
    }

    @Override
    public void onBackPressed() {
        //super.onBackPressed();
        webView.reload();
    }


    @RequiresApi(api = Build.VERSION_CODES.O)
    public static String loadConfig() {
        String fileName="config.ini";
        File file = new File (fileName);
        if (!file.exists()){
            return "";
        }
        String everything = "";
        try {
            everything = new String(Files.readAllBytes(Paths.get(fileName)));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return everything;
    }

    public static void saveConfig(String str) {
        String fileName="config.ini";
        BufferedWriter writer = null;
        try {
            writer = new BufferedWriter(new FileWriter(fileName));
            writer.write(str);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}