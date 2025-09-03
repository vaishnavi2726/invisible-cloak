# 🧥 Invisible Cloak 🪄  

Turn your ordinary webcam feed into magic! This project creates an **“invisibility cloak” effect** using Python & OpenCV by detecting a specific color and replacing it with the background.  

---

## ✨ Features  
- 🎥 Real-time webcam video processing  
- 🎨 Detects cloak color (e.g., red, blue, green)  
- 🪄 Makes the cloak area invisible by blending with the background  
- ⚡ Runs smoothly with OpenCV in Python  

---

## 🚀 Tech Stack  
- **Python** 🐍  
- **OpenCV** 🎥  
- **NumPy** 🔢  

---

## ⚙️ How It Works  
1. Capture the static background for a few seconds.  
2. Detect the cloak color using HSV color space.  
3. Replace cloak pixels with the background → cloak disappears!  

---

## 📸 Demo  
> 🎬 Add a GIF or screenshot of your cloak effect here (optional).  

---

## 🔧 Installation  
```bash
# Clone the repo
git clone https://github.com/<username>/invisible-cloak.git
cd invisible-cloak

# Install dependencies
pip install -r requirements.txt

# Run the script
python cloak.py
