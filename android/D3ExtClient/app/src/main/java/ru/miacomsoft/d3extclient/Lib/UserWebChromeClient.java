package ru.miacomsoft.d3extclient.Lib;

import android.util.Log;
import android.webkit.ConsoleMessage;
import android.webkit.WebChromeClient;
import android.webkit.WebView;

public class UserWebChromeClient extends WebChromeClient {

    @Override
    public boolean onConsoleMessage(ConsoleMessage consoleMessage) {
        //Log.d("d3extclient", consoleMessage.message() + "|"
        //        +consoleMessage.toString()+"|-- From line " +
        //        consoleMessage.lineNumber() + " of " + consoleMessage.sourceId());
        Log.d("console.log", "================Line:"+consoleMessage.lineNumber()+"====== "+consoleMessage.sourceId()+" ============");
        Log.d("console.log", consoleMessage.message());
        return true;
    }

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
