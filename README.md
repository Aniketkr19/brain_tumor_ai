# 🧠 Brain Tumor Detection using Deep Learning

A deep learning project that detects brain tumors from MRI images using a Convolutional Neural Network (CNN).
The model is trained on MRI scans and predicts whether the image contains a **tumor** or is **normal**.

This project also includes a simple web interface where users can upload MRI images and get predictions.

---

# 🚀 Features

* Brain MRI image classification
* Tumor vs Normal detection
* Deep Learning model using CNN
* Web interface for easy predictions
* Fast model inference

---

# 🛠 Tech Stack

* Python
* PyTorch
* Streamlit
* NumPy
* Torchvision
* OpenCV

---

# 📂 Project Structure

```
brain_tumor_ai
│
├── app.py                # Streamlit web application
├── train.py              # Model training script
├── model.py              # CNN model architecture
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation
├── .gitignore            # Files ignored by Git
└── dataset/              # MRI dataset (not uploaded to GitHub)
```

---

# 🧠 Model Architecture

The project uses a **Convolutional Neural Network (CNN)** implemented using **PyTorch**.

The model learns patterns from MRI images and classifies them into:

* Tumor
* Normal

---

# ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/brain-tumor-ai.git
cd brain-tumor-ai
pip install -r requirements.txt
```

---

# 🌐 Run the Web Application

```bash
python -m streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📸 Screenshots (Working Model Output)

## 1️⃣ Upload MRI & UI

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153307.png)

## 2️⃣ MRI Preview

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153316.png)

## 3️⃣ Normal Brain Result

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153431.png)

## 4️⃣ Upload Tumor MRI

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153422.png)

## 5️⃣ High Grade Tumor Detection

![Screenshot](./Screenshot/Screenshot%202026-04-23%20154108.png)

## 6️⃣ Low Grade Tumor Detection

![Screenshot](./Screenshot/Screenshot%202026-04-23%20154121.png)

---

# 📌 Future Improvements

* Tumor location detection using Grad-CAM
* Tumor segmentation
* Improve model accuracy
* Deploy online

---

# 👨‍💻 Author

**Aniket Kumar**

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
