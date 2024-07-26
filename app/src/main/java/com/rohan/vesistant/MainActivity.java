package com.rohan.vesistant;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

import com.alan.alansdk.AlanCallback;
import com.alan.alansdk.AlanConfig;
import com.alan.alansdk.button.AlanButton;
import com.alan.alansdk.events.EventCommand;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.rohan.vesistant.adapters.TextAdapter;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

   /* private TextView response_text;
    private CardView response_textView;*/
    private ArrayList<String> responses;
    private TextAdapter textAdapter;
    private RecyclerView recyclerView;
    private TextView introText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        BottomNavigationView bottomNavigationView = findViewById(R.id.bottom_navigation);

        bottomNavigationView.setSelectedItemId(R.id.home);
       /* response_text = findViewById(R.id.response_text);*/
       /* response_textView = findViewById(R.id.response_textview);*/
        introText = findViewById(R.id.intro_text);
        responses = new ArrayList<String>();
        recyclerView = findViewById(R.id.recycler_view);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setHasFixedSize(true);

        bottomNavigationView.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()){
                    case R.id.home:
                        return true;
                    case R.id.about:
                        startActivity(new Intent(getApplicationContext(), AboutActivity.class));
                        overridePendingTransition(0,0);
                        finish();
                        return true;
                    case R.id.contact:
                        startActivity(new Intent(getApplicationContext(), ContactActivity.class));
                        overridePendingTransition(0,0);
                        finish();
                        return true;
                }

                return false;
            }
        });

        /// Define the project key
//        AlanConfig config = AlanConfig.builder().setProjectId("e73ae1974c8178bb4a4d6def2bafd62c2e956eca572e1d8b807a3e2338fdd0dc/testing").build();
//        AlanButton alanButton = findViewById(R.id.alan_button);
//        alanButton.initWithConfig(config);


//        AlanCallback alanCallback = new AlanCallback() {
//            /// Handle commands from Alan Studio
//            @Override
//            public void onCommand(final EventCommand eventCommand) {
//                introText.setVisibility(View.GONE);
//                try {
//                    JSONObject command = eventCommand.getData();
//                    for(int i=1; i<command.length(); i++){
//                        String commandName = command.getJSONObject("data").getString("command");
//                        String data = command.getJSONObject("data").getString("answer");
//                        Log.d("AlanButton", "onCommand: commandName: " + commandName + " " + data);
//                        /*response_textView.setVisibility(View.VISIBLE);*/
//                        String response = data.toString();
//                        /*response_text.setText(response);*/
//                        responses.add(response);
//                    }
//                    Log.d("Response", "onCommand: "+ responses.size());
//                    textAdapter = new TextAdapter(MainActivity.this, responses);
//                    recyclerView.setAdapter(textAdapter);
//                    recyclerView.smoothScrollToPosition(textAdapter.getItemCount());
//
//                } catch (JSONException e) {
//                    Log.e("AlanButton", e.getMessage());
//                }
//            }
//        };
//
///// Register callbacks
//        alanButton.registerCallback(alanCallback);
    }
}