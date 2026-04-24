# 🧠 Brain Tumor Detection using Deep Learning

A deep learning project that detects brain tumors from MRI images using a Convolutional Neural Network (CNN).  
The model is trained on MRI scans and predicts whether the image contains a **tumor** or is **normal**.

This project also includes a simple web interface where users can upload MRI images and get predictions.

---

# 🚀 Features

- Brain MRI image classification
- Tumor vs Normal detection
- Deep Learning model using CNN
- Web interface for easy predictions
- Fast model inference

---

# 🛠 Tech Stack

- Python
- PyTorch
- Streamlit
- NumPy
- Torchvision
- OpenCV

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

- Tumor
- Normal

Training is performed using image datasets with labeled MRI scans.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/brain-tumor-ai.git
```

Move into the project folder:

```bash
cd brain-tumor-ai
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# 🏋️ Training the Model

To train the deep learning model run:

```bash
python train.py
```

After training finishes, the trained model will be saved as:

```
brain_model.pth
```

---

# 🌐 Run the Web Application

This project includes a simple web interface built with Streamlit.

Run the application:

```bash
python -m streamlit run app.py
```

Open the following link in your browser:

```
http://localhost:8501
```

Upload an MRI image and the system will predict whether a **tumor is present or not**.

---

# 📊 Dataset

The dataset contains MRI images of the human brain classified into:

- Tumor
- Normal

The dataset is used to train the deep learning model to recognize tumor patterns.

Note: The dataset is not uploaded to GitHub due to its large size.




# 📸 Screenshots (Working Model Output)

## 1️⃣ Uploaded Brain MRI

![Screenshot](./Screenshot/Screenshot%202026-04-23%20154108.png)

## 2️⃣ Normal Brain Result

![Screenshot](./Screenshot/Screenshot%202026-04-23%20154121.png)

## 3️⃣ Uploaded Brain MRI

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153307.png)

## 4️⃣ Low Grade Tumor Detection

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153316.png)

## 5️⃣ Uploaded Brain MRI

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153422.png)

## 6️⃣ High Grade Tumor Detection

![Screenshot](./Screenshot/Screenshot%202026-04-23%20153431.png)

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
