package com.akash.sky.emergencyhelper;

import android.Manifest;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.annotation.RequiresPermission;
import android.support.v4.app.ActivityCompat;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class callAmb extends Activity {
    static final int REQUEST_LOCATION=1;
    LocationManager locationManager;
    double latti,longi;
    Button map;
    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference myRef = database.getReference("Management/Emergency");
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.callamb);
        String MY_PREFS_NAME="hello";                      //file name of shared preferences
        SharedPreferences prefs = getSharedPreferences(MY_PREFS_NAME, MODE_PRIVATE);
        String restoredText = prefs.getString("name", null);     //gets the value
        //Log.d("new",restoredText);
        map =(Button) findViewById(R.id.maps);

        locationManager=(LocationManager)getSystemService(Context.LOCATION_SERVICE);
        getLocation();
        //Log.d("latitude",Double.toString(latti));
        myRef.child("user1/Location/Latitude").setValue(latti,"new");
        myRef.child("user1/Location/Longitude").setValue(longi,"new");
        myRef.child("user1/Location/Name").setValue(restoredText,"new");
}
void getLocation(){
        if(ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this,Manifest.permission.ACCESS_COARSE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this,new String []{Manifest.permission.ACCESS_FINE_LOCATION}, REQUEST_LOCATION);
        }else{
            Location location=locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
            if(location !=null){
                latti=location.getLatitude();
                longi=location.getLongitude();
            }
        }
    }

    public void callMap(View view){
        Intent intent = new Intent(callAmb.this, MapsActivity.class);
        startActivity(intent);
    }
}
