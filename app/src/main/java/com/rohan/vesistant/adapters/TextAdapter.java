package com.rohan.vesistant.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.rohan.vesistant.R;
import com.rohan.vesistant.models.Text;

import java.util.ArrayList;
import java.util.Random;

public class TextAdapter extends RecyclerView.Adapter<TextAdapter.MyViewHolder>{

    Context context;
    ArrayList<String> responses;

    public TextAdapter(Context context, ArrayList<String> responses) {
        this.context = context;
        this.responses = responses;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.text_item, parent, false);
        final MyViewHolder myViewHolder = new MyViewHolder(view);

        int[] androidColors = view.getResources().getIntArray(R.array.androidcolors);
        int randomColors = androidColors[new Random().nextInt(androidColors.length)];

        myViewHolder.responseCard.setBackgroundColor(randomColors);

        return myViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
         String text = responses.get(position);

         holder.responseText.setText(text);
    }

    @Override
    public int getItemCount() {
        return responses.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        CardView responseCard;
        TextView responseText;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);

            responseCard = itemView.findViewById(R.id.response_card);
            responseText = itemView.findViewById(R.id.response_text);
        }
    }
}
