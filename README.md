# 👗 Virtual Try-On Website

> An AR/VR-powered virtual fitting room that lets users try on outfits online — enhancing the online retail experience through real-time computer vision.

**Shortlisted at Smart India Hackathon (SIH) — College-Level Evaluation**

---

## 🧠 Overview

The Virtual Try-On Website is an AI-powered web application that simulates a virtual fitting room experience. Using computer vision and AR/VR concepts, it overlays clothing items onto a user's image or live feed — reducing return rates and improving customer confidence in online shopping.

---

## ✨ Features

- 👤 **Virtual Fitting Room** — Try on clothing items on a live or uploaded image
- 🧥 **Real-Time Overlay** — AR-based garment overlay using pose estimation
- 📦 **Product Catalog** — Browse and select items to try on
- 📊 **Data Pipeline** — Preprocessed and trained on COCO Dataset (25 GB / 1.5M images)
- 🌐 **Web Interface** — Accessible via browser, built with Python & Flask

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Frameworks | TensorFlow, Keras, PyTorch, Scikit-learn |
| ML Libraries | NumPy, Pandas, Matplotlib, Seaborn, Streamlit |
| Dataset | COCO Dataset – 25 GB / 1.5M images |
| Cloud/ML Ops | Snowflake ML |
| Concepts | AR/VR, Pose Estimation, Computer Vision |

---

## 📁 Project Structure

```
virtual-tryon/
├── app.py                  # Flask app entry point
├── model/
│   ├── train.py            # Model training scripts
│   ├── preprocess.py       # Data cleaning & feature engineering
│   └── predict.py          # Inference pipeline
├── static/
│   ├── css/                # Stylesheets
│   └── assets/             # Sample garment images
├── templates/
│   └── index.html          # Main web interface
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip
```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/virtual-tryon.git
cd virtual-tryon

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📊 Dataset

- **Dataset:** [COCO (Common Objects in Context)](https://cocodataset.org/)
- **Size:** ~25 GB / 1.5 Million images
- **Usage:** Used for pose estimation and garment segmentation model training

---

## 🏆 Recognition

- 🥇 **Shortlisted at Smart India Hackathon (SIH)** — College-level evaluation among competing teams

---

## 👩‍💻 Author

**Addepalli Haripriya**  
B.Tech Computer Science, Anil Neerukonda Institute of Technology and Sciences  
📧 haripriyaaddepalli64@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/haripriya-addepalli-764b75350)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
