package ru.miacomsoft.d3extclient.Lib;

import android.Manifest;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.media.AudioManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.speech.tts.TextToSpeech;
import android.speech.tts.UtteranceProgressListener;
import android.util.Log;

import androidx.core.content.ContextCompat;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Locale;

/// <uses-permission android:name="android.permission.RECORD_AUDIO" />
public class Voisee implements TextToSpeech.OnInitListener {
    private Context context;
    private TextToSpeech tts;
    public SpeechRecognizer speech = null;
    public Intent recognizerIntent;
    public AudioManager myAudioManager;
    public HashMap<String, String> params = new HashMap<String, String>();
    // ArrayList<String> names = new ArrayList<String>(Arrays.asList("A","B","C","D"));
    ArrayList<String> speechTextList = new ArrayList<String>();


    public Voisee(Context contect) {
        this.context = contect;
        utteranceProgressListener TextSpeech = new utteranceProgressListener(); //Экземпляр класса слушателя
        tts = new TextToSpeech(this.context, this);
        tts.setOnUtteranceProgressListener(TextSpeech); //Установка слушателя синтеза речи
        // Создание экземпляра класса AudioManager
        myAudioManager = (AudioManager) this.context.getSystemService(Context.AUDIO_SERVICE);
    }


    public void send(String text){
        speechTextList.add(text);
    }

    public void getRecognizerText(String text){

    }

    public void getRecognizerError(String text) {

    }

    public void onSpeech() {
        // Object[] peopleArray = speechTextList.toArray();
        speak_on(); // Включаем динамики
        params.put(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, "HELLO");
        for (int i = 0; i < speechTextList.size(); i++) {
            tts.speak(speechTextList.get(i), TextToSpeech.QUEUE_ADD, params);// Синтезировать речь
        }
        // for(Object person : speechTextList.toArray()){
        //
        // }
        speechTextList.clear();
    }


    public void start() {
        speak_off();
        bspeesh(); // Вызов метода для активизации распознавателя голоса
        speech.startListening(recognizerIntent); // Начать прослушивание речи
    }

    public void stop() {
        if (speech != null) {
            speech.stopListening(); //Прекратить слушать речь
            speech.destroy();       // Уничтожить объект SpeechRecognizer
        }
    }

    public void checkVoiceCommandPermission(Context context) {
        // Включить разрешение  прослушивать микрофон в настройках
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (!(ContextCompat.checkSelfPermission(context, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED)) {
                Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.parse("package:" + context.getPackageName()));
                context.startActivity(intent);
            }
        }
    }

    public void onDestroy() {
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
    }
    public void speak_off() { // Метод для выключение внешних динамиков планшета
        myAudioManager.setStreamVolume(AudioManager.STREAM_MUSIC, 0, AudioManager.FLAG_REMOVE_SOUND_AND_VIBRATE);
    }

    public void speak_on() { // Метод включения внешних динамиков планшета
        myAudioManager.setStreamVolume(AudioManager.STREAM_MUSIC, 20, AudioManager.FLAG_REMOVE_SOUND_AND_VIBRATE);
    }


    @Override
    public void onInit(int status) {   // Инициализация перед синтезом речи
        if (status == TextToSpeech.SUCCESS) {
            int result = tts.setLanguage(Locale.getDefault());
            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            }
        } else {
            Log.e("TTS", "Init Failed!");
        }

    }

    public void bspeesh() {
        speech = SpeechRecognizer.createSpeechRecognizer(context); //Создание объекта распознавателя речи
        speech.setRecognitionListener(thiss); //Установить обработчик событий распознавания
        recognizerIntent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_CALLING_PACKAGE, context.getPackageName());
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_WEB_SEARCH);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE, 1); // Включить Офлайновое распознование
    }

    RecognitionListener thiss = new RecognitionListener() {
        @Override
        public void onBeginningOfSpeech() {
        }

        @Override
        public void onBufferReceived(byte[] buffer) {
        }

        @Override
        public void onEndOfSpeech() {
            // oText.setText("НЕ ГОВОРИ");
        }

        @Override
        public void onError(int errorCode) {
            speak_off();  //Выключить звук в случае любой ошибки
            String errorMessage = getErrorText(errorCode); // Вызов метода расшифровки ошибки
            getRecognizerError(errorMessage + "; Ошибка=№" + errorCode);
            // ErrText.setText(errorMessage + "; Ошибка=№" + errorCode);
            // tts.speak(errorMessage + "; Ошибка=№" + errorCode, TextToSpeech.QUEUE_ADD, params);// Синтезировать речь
            onSpeech(); // проговорить очередь сообщений из списка
            speech.destroy();
            bspeesh();
            // oText.setText("Слушаю");
            // Log.i("TEST", errorMessage + "; Ошибка=№" + errorCode);
            speech.startListening(recognizerIntent);
        }

        @Override
        public void onEvent(int arg0, Bundle arg1) {

        }

        @Override
        public void onPartialResults(Bundle arg0) {
            ArrayList data = arg0.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
            // String word = (String) data.get(data.size() - 1);
            String sp = data.get(0).toString();
            int value = 100;
            // returnedText.setText(sp);
            // Log.i("TEST", "partial_results: " + sp);
        }

        @Override
        public void onReadyForSpeech(Bundle arg0) {

        }

        @Override
        public void onResults(Bundle results) {  // Результаты распознавания
            ArrayList data = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
            String sp = data.get(0).toString();
            getRecognizerText(sp);
            // Log.i("TEST", "partial_results: " + sp);
            int value = 100;
            onSpeech(); // проговорить очередь сообщений из списка
            speak_off(); // Если фразы и команды не описаны, выполняется распознавание речи, вывод результата
            // в виде строки при выключенных динамиках
            speech.stopListening(); //Прекратить слушать речь
            speech.destroy();       // Уничтожить объект SpeechRecognizer
            bspeesh();
            speech.startListening(recognizerIntent);
            //returnedText.setText(sp);
            //spout = sp;
            /*
            if (r0 == 0 || r1 == 0 || r2 == 0 || r3 == 0 || r4 == 0 || r5 == 0 || r6 == 0 || r10 == 0 || r11 == 0 || r12 == 0 || r13 == 0 || r14 == 0 || r15 == 0 || r16 == 0 || r19 == 0 || value == 54) // Синтез речи
            // выполняется в случае наличия команд и фраз в памяти
            {
                speak_on(); // Включаем динамики
                params.put(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, "HELLO");
                tts.speak(spout, TextToSpeech.QUEUE_ADD, params);// Синтезировать речь
            } else {
                speak_off(); // Если фразы и команды не описаны, выполняется распознавание речи, вывод результата
                // в виде строки при выключенных динамиках
                speech.stopListening(); //Прекратить слушать речь
                speech.destroy();       // Уничтожить объект SpeechRecognizer
                bspeesh();
                oText.setText("Слушаю");
                speech.startListening(recognizerIntent);
            }
            */
            /*
            speak_on(); // Включаем динамики
            params.put(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, "HELLO");
            tts.speak("ты сказал "+spout, TextToSpeech.QUEUE_ADD, params);// Синтезировать речь
            */
        }

        @Override
        public void onRmsChanged(float rmsdB) {

        }

    };

    // распознавания голоса
    public class utteranceProgressListener extends UtteranceProgressListener {
        @Override
        public void onDone(String utteranceId) { // Действия после окончания речи синтезатором
            ((Activity) context).runOnUiThread(new Runnable() {
                @Override
                public void run() {
                     /*
                    r19 = sp.compareTo(sp19);
                    if (r19 != 0) { // Если не "конец связи", то активити распознавания голоса запускается вновь
                        oText.setText("Слушаю");
                        speech.startListening(recognizerIntent);
                    }
                    */
                    speech.startListening(recognizerIntent);
                }

            });
        }

        @Override
        public void onStart(String utteranceId) {
        }

        @Override
        public void onError(String utteranceId) {
        }
    }
    public static String getErrorText(int errorCode) { // Метод возврата ошибки по ее коду
        String message;
        switch (errorCode) {
            case SpeechRecognizer.ERROR_AUDIO:
                message = "Audio recording error";
                break;
            case SpeechRecognizer.ERROR_CLIENT:
                message = "Client side error";
                break;
            case SpeechRecognizer.ERROR_INSUFFICIENT_PERMISSIONS:
                message = "Insufficient permissions";
                break;
            case SpeechRecognizer.ERROR_NETWORK:
                message = "Network error";
                break;
            case SpeechRecognizer.ERROR_NETWORK_TIMEOUT:
                message = "Network timeout";
                break;
            case SpeechRecognizer.ERROR_NO_MATCH:
                message = "No match";
                break;
            case SpeechRecognizer.ERROR_RECOGNIZER_BUSY:
                message = "RecognitionService busy";
                break;
            case SpeechRecognizer.ERROR_SERVER:
                message = "error from server";
                break;
            case SpeechRecognizer.ERROR_SPEECH_TIMEOUT:
                message = "No speech input";
                break;
            default:
                message = "Didn't understand, please try again.";
                break;
        }
        return message;
    }


}
