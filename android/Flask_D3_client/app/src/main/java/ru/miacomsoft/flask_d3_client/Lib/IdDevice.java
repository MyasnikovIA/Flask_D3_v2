package ru.miacomsoft.flask_d3_client.Lib;

import android.content.Context;
import android.provider.Settings;
import android.telephony.TelephonyManager;

import java.util.UUID;

/**
 * Created by MyasnikovI on 29.08.13.

 *
 *                     // Возможно понадобится добавить
 *                     //  AndroidManifest.xml
 *                     // <uses-permission android:name="android.permission.READ_PHONE_STATE" />
 *
 *    -----------------------------------------------
 *                      Применение
 *           IdDevice id = new IdDevice(this);
 *           tv2.setText(id.deviceId);
 *    -----------------------------------------------
 */
public class IdDevice {

    public String Device="";
    public String Serial="";
    public String androidId="";
    public String UUIDId="";
    public String deviceId="";
    public String IMEI="";

    public IdDevice(Context context) {
        final TelephonyManager tm = (TelephonyManager) context.getSystemService(context.TELEPHONY_SERVICE);
        Device = "" + tm.getDeviceId();
        Serial = "" + tm.getSimSerialNumber();
        androidId = "" + Settings.Secure.getString(context.getContentResolver(), Settings.Secure.ANDROID_ID);

        UUID deviceUuid = new UUID(androidId.hashCode(), ((long)Device.hashCode() << 32) | Serial.hashCode());
        UUIDId = deviceUuid.toString();
        deviceId = Settings.Secure.getString(context.getContentResolver(), Settings.Secure.ANDROID_ID);

        //      public String BluetoothAdress;
        //  BluetoothAdapter m_BluetoothAdapter = null; // Local Bluetooth adapter
        //  m_BluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        //  BluetoothAdress = m_BluetoothAdapter.getAddress();

        //     public String WiFiMac;
        //      WifiManager wm = (WifiManager)context.getSystemService(Context.WIFI_SERVICE);
        //      WiFiMac = wm.getConnectionInfo().getMacAddress();

        TelephonyManager TelephonyMgr = (TelephonyManager) context.getSystemService(context.TELEPHONY_SERVICE);
        IMEI = TelephonyMgr.getDeviceId(); // Requires READ_PHONE_STATE

    }

}
