package ru.miacomsoft.d3extclient;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import ru.miacomsoft.d3extclient.Lib.Android;
import ru.miacomsoft.d3extclient.Lib.UserWebChromeClient;
import ru.miacomsoft.d3extclient.Lib.UserWebClient;

public class MainActivity extends AppCompatActivity {
    public static WebView webView ;
    private Button button;

    @SuppressLint("JavascriptInterface")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        webView = new WebView(this);
        button = (Button) findViewById(R.id.button);
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

    public void onClickButton(View v) {
        EditText infoEdit = (EditText) findViewById(R.id.editText);
        String urlText = infoEdit.getText().toString();
        saveConfig(urlText);
        runWebClient(urlText);
    }

    public void runWebClient(String urlText) {
        setContentView(webView);
        webView.setWebViewClient(new UserWebClient());
        webView.setWebChromeClient(new UserWebChromeClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);  // Включить обработчик JS
        webView.addJavascriptInterface(new Android(this,webView), "Android");
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

}