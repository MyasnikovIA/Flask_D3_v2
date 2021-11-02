package ru.miacomsoft.d3extclient.Lib;

import android.webkit.WebView;
import android.webkit.WebViewClient;


public class UserWebClient extends WebViewClient {


    @SuppressWarnings("deprecation")
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        view.loadUrl(url);
        return true;
    }
}
