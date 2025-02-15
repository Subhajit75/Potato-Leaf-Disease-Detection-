

---

# 🥔🥬 Potato Leaf Disease Detection  

## 🌟 Overview  
This project aims to detect potato leaf diseases using deep learning. It classifies leaves as Healthy, Early Blight, or Late Blight using a Convolutional Neural Network (CNN) model and provides a web-based interface for easy usage.

## 📌 Features  
✅ Upload a potato leaf image for disease analysis  
j;k;;
✅ Instant classification into **Healthy, Early Blight, or Late Blight**  
✅ Confidence score for each prediction  
✅ Web-based interface powered by **Streamlit**  
✅ Lightweight **TFLite** model for efficient inference  

## 🛠️ Tech Stack  
- **Python** (for backend and model integration)  
- **TensorFlow Lite** (for optimized model inference)  
- **Streamlit** (for web-based UI)  
- **NumPy & PIL** (for image processing)  

## 🚀 Installation  

1️⃣ **Clone the Repository**  
```sh
git clone (https://github.com/Subhajit75/Potato-Leaf-Disease-Detection-.git)
cd Potato-Leaf-Disease-Detection
```
  
2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3️⃣ **Run the Application**  
```sh
streamlit run app.py
```

## 📁 Dataset  
The dataset consists of potato leaf images classified into three categories:  
- **Healthy Leaves 🌱**
- **Early Blight 🍂**
- **Late Blight 🍁** 

**📌 Source: https://github.com/JayRathod341997/AICTE-Internship-files**
The dataset is preprocessed using resizing, normalization, and augmentation to improve model performance.

## 📖 How It Works
- **1️⃣ Upload Image: The user uploads an image of a potato leaf.**
- **2️⃣ Preprocessing: The image is resized and normalized before feeding it to the model.**
- **3️⃣ Model Prediction: The trained CNN model classifies the image into Healthy, Early Blight, or Late Blight.**
- **4️⃣ Display Results: The prediction is shown along with a confidence score.**
- **5️⃣ Treatment Recommendations: If a disease is detected, suggestions for treatment methods are displayed.**

## 📖 Model Details  
- **Architecture:** Convolutional Neural Network (CNN)  
- **Training Framework:** TensorFlow/Keras  
- **Optimization:** Trained and converted to **TensorFlow Lite (TFLite)** for efficient mobile & web deployment  

## 🔬 Results
The CNN model achieved the following accuracy on test data:
✔ Overall Accuracy: 96.5%
✔ Precision: 94%
✔ Recall: 97%

✅ Healthy Leaves – 98% Accuracy
✅ Early Blight – 94% Accuracy
✅ Late Blight – 96% Accuracy

## 🔗 References
- **Research Paper - Deep Learning for Plant Disease Detection**
- **TensorFlow Lite Documentation - https://www.tensorflow.org/lite**
- **Jay Rathod - https://github.com/JayRathod341997/AICTE-Internship-files**

## 🎓 Acknowledgment
This project is developed as part of the TechSaksham AICTE Internship 2024 under the guidance of Jay Rathod.

## 🤝 Contributors  
- Subhajit  (GitHub: [Subhajit75](https://github.com/Subhajit75)))  

## 📜 License  
This project is open-source and available under the **MIT License**.  


