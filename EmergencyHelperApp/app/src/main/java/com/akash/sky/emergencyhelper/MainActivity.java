package com.akash.sky.emergencyhelper;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;

public class MainActivity extends AppCompatActivity {
    EditText email;           //email id
    EditText password;         //password
    Button login;            //login
    Button call;             //call button
    SharedPreferences sharedpreferences;    //internal storage
    private FirebaseAuth mAuth;     //for authentication
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        email=(EditText) findViewById(R.id.email);
        password=(EditText) findViewById(R.id.password);
        login=(Button) findViewById(R.id.login);
        mAuth=FirebaseAuth.getInstance();
        call=(Button) findViewById(R.id.call);
        String MY_PREFS_NAME="hello";                      //file name of shared preferences
        SharedPreferences prefs = getSharedPreferences(MY_PREFS_NAME, MODE_PRIVATE);
        String restoredText = prefs.getString("name", null);     //gets the value
       if(restoredText!=null) {callVisibile(); }       //call the visibility manipulator

    }

    public void LoginSign(View view){                           //Login function
        String email1 = email.getText().toString();
        String pass=password.getText().toString();
        if(validId(email1) && validPass(pass)){                 //validation
            String MY_PREFS_NAME="hello";
            SharedPreferences.Editor editor = getSharedPreferences(MY_PREFS_NAME, MODE_PRIVATE).edit();
            editor.putString("name", email1);
            editor.putString("password", pass);
            editor.apply();
            callVisibile();
        }
        else {
            Toast.makeText(getApplicationContext(), "Wrong email id or password",
                    Toast.LENGTH_LONG).show();
        }

    }

    public boolean validId(String id){                  //validation
        char[] array=id.toCharArray();
        for (int i=0;i<id.length();i++)
            if(array[i]=='@'){
            return true;
            }
        return false;
    }
    public boolean validPass(String pass){            //valid pass
        if(pass.length()>4) return true;
        return false;
    }

 public void callVisibile(){                          //make the manipulation
     email.setVisibility(View.INVISIBLE);
     password.setVisibility(View.INVISIBLE);
     login.setVisibility(View.INVISIBLE);
     call.setVisibility(View.VISIBLE);
 }

 public void callToNext(View view){
     Intent intent = new Intent(MainActivity.this, callAmb.class);
     finish();
     startActivity(intent);
 }

}
