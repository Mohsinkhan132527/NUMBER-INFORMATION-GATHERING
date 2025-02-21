# 📌 NumInformationGathering

NumInformationGathering ek advanced Python-based tool hai jo **phone number, CNIC, location tracking, face recognition, audio analysis, aur cyber threat detection** ke liye banaya gaya hai. 🚀

---

## 🔹 **Features**

✔ Phone Number Information Lookup\
✔ CNIC-Based SIM Registration Lookup\
✔ Live Face Recognition\
✔ Real-Time Audio Analysis\
✔ Mobile Location Tracking\
✔ Dark Web Phone Number Lookup\
✔ AI-Based Cyber Threat Analysis

---

## 📌 **Installation Guide**

### 1️⃣ **Python Install Karein**

Pehle ensure karein ke **Python 3.x** installed hai:

```sh
python --version
```

Agar Python installed nahi hai, toh is link se install karein:\
🔗 [Download Python](https://www.python.org/downloads/)

---

### 2️⃣ **Project Clone Karein**

Agar aap is project ko GitHub se clone karna chahte hain, toh yeh command run karein:

```sh
git clone https://github.com/yourusername/numinformationgathering.git
cd numinformationgathering
```

Agar aapne **manually download** kiya hai, toh bas **folder open karein** aur **terminal/cmd us folder ke andar open karein**.

---

### 3️⃣ **Dependencies Install Karein**

Yeh command run karein taake saari required libraries install ho jayen:

```sh
pip install requests beautifulsoup4 face_recognition opencv-python numpy librosa soundfile joblib torchaudio pysocks phonenumbers googlemaps geocoder
```

Agar aap Linux ya Mac use kar rahe hain aur `face_recognition` install nahi ho raha, toh yeh command use karein:

```sh
pip install dlib face_recognition
```

---

### 4️⃣ **Tor Setup Karein (Dark Web Lookup Ke Liye)**

Agar aap Dark Web Lookup feature use karna chahte hain, toh **Tor Browser** install karein:\
🔗 [Download Tor](https://www.torproject.org/download/)

Tor ko open karein aur ensure karein ke **SOCKS5 Proxy (127.0.0.1:9050)** running hai.

---

## ▶️ **Usage Guide**

Agar sab kuch setup ho gaya hai, toh script run karne ke liye yeh command use karein:

```sh
python khan.py
```

Script run karne ke baad yeh aap se phone number aur audio file ka path maangega.

**Example Input:**

```
Enter Phone Number: +923001234567
Enter Audio File for Analysis: sample_audio.wav
```

**Example Output:**

```
📞 Number Information Lookup:
📞 Number Registered Name: Ali Khan

🆔 CNIC Lookup:
🆔 CNIC Registered: 42101-1234567-9

📍 Real-Time Location Tracking:
📍 Current Location: [33.6844, 73.0479]

🔴 Live Face Recognition (Press 'q' to stop):
🔍 Live Face Recognition Completed!

🎤 Live Audio Analysis:
🎤 REAL AUDIO

🌑 Dark Web Lookup:
🔴 +923001234567 found on http://hss3uro2hsxfogfq.onion

🕵️ Cyber Threat Analysis:
🔴 Cyber Threat Level: HIGH
```

---

## ❌ **Common Issues & Solutions**

### 🔴 `ModuleNotFoundError`

Agar kisi library ka error aaye, toh manually install karein:

```sh
pip install library_name
```

Example:

```sh
pip install opencv-python
```

### 🔴 Face Recognition Not Working?

Agar **face\_recognition** error de raha hai, toh ensure karein ke `dlib` installed hai:

```sh
pip install dlib face_recognition
```

### 🔴 Tor Not Working?

- Tor browser ko **background me open** karein.
- Check karein ke **SOCKS5 proxy 127.0.0.1:9050** pe running hai.

---

## 🤝 **Contributions**

Agar aap project ko improve karna chahte hain toh pull request bhejein ya issues report karein.

📧 Contact: **923445739751**

---

## 📜 **License**

Yeh project **MIT License** ke under hai. Aap ise freely use aur modify kar sakte hain. ✅

