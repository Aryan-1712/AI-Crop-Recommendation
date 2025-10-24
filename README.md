🌾 AI Crop Recommendation System

🔍 Overview

The AI Crop Recommendation System helps farmers and agricultural experts identify the most suitable crop to grow based on soil and environmental parameters such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

It uses a machine learning model trained on agricultural data to make accurate predictions and visualize insights.

🚀 Features

✅ GUI-based interface built using Tkinter

✅ Predicts best-suited crop instantly

✅ Clear visualization using Matplotlib and Seaborn

✅ Easy to use — enter parameters → click Predict → get results

✅ “Clear All” button to reset inputs

✅ Data visualization for better understanding of crop distribution

🧠 Tech Stack

Programming Language: Python
Libraries Used      : numpy, pandas, matplotlib, seaborn, scikit-learn, tkinter, pickle
Model	Random Forest Classifier (trained on crop dataset)

🧩 Working

Input Parameters — User enters soil and climate data

Model Prediction — Pre-trained ML model processes input

Output Display — Best crop is displayed within the GUI

Visualization — Shows crop distribution and insights

🖼️ Sample Visualization

Below is an example of how the dataset’s crop distribution looks:

🖥️ GUI Preview

When you run the program, you’ll see a clean interface like this:

+---------------------------------------------------+
| AI CROP RECOMMENDATION SYSTEM                     |
|---------------------------------------------------|
| N: [   ]  P: [   ]  K: [   ]                     |
| Temperature: [   ]  Humidity: [   ]              |
| pH: [   ]  Rainfall: [   ]                       |
|                                                   |
| [ Predict Crop ]   [ Clear All ]                  |
| Recommended Crop:  [ Wheat 🌾 ]                   |
+---------------------------------------------------+

⚙️ How to Run

      Clone the repository:
            git clone https://github.com/Aryan-1712/AI-Crop-Recommendation.git
            cd "AI-Crop-Recommendation"
      
      Install dependencies:
            pip install -r requirements.txt
      
      Run the program:
            python main.py

📊 Dataset

The dataset used contains agricultural data for various crops based on soil nutrients and climatic conditions.
Each crop has 100 samples, ensuring balanced training for the ML model.

🏆 Future Improvements

Integrate live weather data via API

Add fertilizer and soil treatment recommendations

Build web dashboard using Streamlit or Flask

👨‍💻 Author

Aryan Sharma
📍 B.Tech CSE (Data Science) @ SRM Delhi NCR

💡 Passionate about AI, Data Science & Innovation

🔗 GitHub Profile : https://github.com/Aryan-1712
