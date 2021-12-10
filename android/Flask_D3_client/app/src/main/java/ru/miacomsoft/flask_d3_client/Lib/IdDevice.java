package ru.miacomsoft.flask_d3_client.Lib;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.pm.PackageManager;
import android.provider.Settings;
import android.telephony.SignalStrength;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.UUID;

import ru.miacomsoft.flask_d3_client.MainActivity;

/**
 * Created by MyasnikovI on 10.12.2021.
 *
 *    // Возможно понадобится добавить
 *    //  AndroidManifest.xml
 *    // <uses-permission android:name="android.permission.READ_PHONE_STATE" />
 *
 */
public class IdDevice {

    private MainActivity activity;
    private Context context;

    public IdDevice(MainActivity activity) {
        this.activity = activity;
        this.context = activity.getBaseContext();
    }

    @SuppressLint("MissingPermission")
    public String getDeviceInfo() {
        if (setTelephoneSetings()){
            return "";
        };
        JSONObject obj = new JSONObject();
        try {
            TelephonyManager manager = (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
            if(android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) { // API Level 26.
                String imei = manager.getImei();
                int phoneCount = manager.getPhoneCount();
                obj.put("PhoneNumber",manager.getLine1Number());
                obj.put("IMEI",imei);
                obj.put("PhoneCount",phoneCount);
                obj.put("Device",manager.getDeviceId());
                obj.put("AndroidId", Settings.Secure.getString(context.getContentResolver(), Settings.Secure.ANDROID_ID));
                obj.put("Serial",manager.getSimSerialNumber());
                // obj.put("UUID",new UUID(androidId.hashCode(), ((long)Device.hashCode() << 32) | Serial.hashCode()).toString());
                obj.put("UUIDId",Settings.Secure.getString(context.getContentResolver(), Settings.Secure.ANDROID_ID));
            }
            if(android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.P) { // API Level 28.
                SignalStrength signalStrength = manager.getSignalStrength();
                int level = signalStrength.getLevel();
                obj.put("StrengthLevel",level);
            }

        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return obj.toString();
    }

    public boolean setTelephoneSetings() {
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) { // 23
            int readPhoneStatePermission = ActivityCompat.checkSelfPermission(context, Manifest.permission.READ_PHONE_STATE);
            if ( readPhoneStatePermission != PackageManager.PERMISSION_GRANTED) {
                activity.requestPermissions( new String[]{Manifest.permission.READ_PHONE_STATE}, MainActivity.MY_PERMISSION_REQUEST_CODE_PHONE_STATE);
                return true;
            }
        }
        return false;
    }

}
