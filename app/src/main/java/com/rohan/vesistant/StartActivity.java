package com.rohan.vesistant;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.WindowManager;

public class StartActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start);

        // It will make our splash screen Full screen on Device higher then Marshmallow
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
            getWindow().setFlags(WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS, WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS);
        }

        Thread thread = new Thread(){
            public void run(){
                try {
                    sleep(3000);
                    startActivity(new Intent(StartActivity.this, MainActivity.class));
                    finish();
                }catch (Exception e){

                }
            }
        };

        thread.start();
    }
}