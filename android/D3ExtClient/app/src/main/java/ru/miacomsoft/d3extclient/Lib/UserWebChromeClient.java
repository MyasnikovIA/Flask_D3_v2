package ru.miacomsoft.d3extclient.Lib;

import android.webkit.WebChromeClient;
import android.webkit.WebView;

public class UserWebChromeClient extends WebChromeClient {
    @Override
    public void onProgressChanged(WebView view, int newProgress) {
        /*
        progressBar.setProgress(newProgress);
        if(newProgress==100)
            progressBar.setVisibility(View.GONE);
        else
            progressBar.setVisibility(View.VISIBLE);
         */
    }
}
