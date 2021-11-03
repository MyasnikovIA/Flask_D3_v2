package ru.miacomsoft.d3extclient;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;

import androidx.appcompat.app.AppCompatActivity;

import ru.miacomsoft.d3extclient.Lib.Android;
import ru.miacomsoft.d3extclient.Lib.UserWebChromeClient;
import ru.miacomsoft.d3extclient.Lib.UserWebClient;

public class MainActivity extends AppCompatActivity {
    private WebView webView ;

    @SuppressLint("JavascriptInterface")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        webView = new WebView(this);
        setContentView(webView);
        webView.setWebViewClient(new UserWebClient());
        webView.setWebChromeClient(new UserWebChromeClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true); // включить обработчик JS
        webView.addJavascriptInterface(new Android(this,webView), "Android");
        webView.loadUrl("http://128.0.24.172:9091");
		// webView.loadUrl("file:///android_asset/mypage.html");

        //webView.reload();
    }

    @Override
    public void onBackPressed() {
        //super.onBackPressed();
        webView.reload();
    }

}