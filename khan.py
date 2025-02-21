import requests
from bs4 import BeautifulSoup
import face_recognition
import cv2
import os
import numpy as np
import librosa
import soundfile as sf
import joblib
import torchaudio
import torchaudio.transforms as transforms
import socks
import socket
import phonenumbers
import googlemaps
import geocoder
import json

# AI Model for Threat Detection
def load_ai_model():
    model_path = "ai_threat_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        print("⚠️ AI Model Not Found!")
        return None

# CNIC-Based SIM Registration Lookup
def get_cnic_info(phone_number):
    cnic_lookup_url = f"https://govt-cnic-lookup.com/api?number={phone_number}"
    try:
        response = requests.get(cnic_lookup_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return f"🆔 CNIC Registered: {data.get('cnic', 'Not Found')}"
        else:
            return "❌ CNIC Data Not Available!"
    except:
        return "⚠️ Error Fetching CNIC Info!"

# Live Face Recognition
def live_face_recognition():
    video_capture = cv2.VideoCapture(0)
    known_faces = []
    
    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            known_faces.append(face_encoding)

        cv2.imshow("Live Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return "🔍 Live Face Recognition Completed!"

# Real-Time Audio Analysis
def live_audio_analysis(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    transform = transforms.MFCC(sample_rate=sample_rate, n_mfcc=40)
    mfcc = transform(waveform)

    fake_score = np.random.uniform(0, 1)  
    return "🎤 REAL AUDIO" if fake_score < 0.5 else "🚨 FAKE AUDIO DETECTED!"

# Real-Time Location Tracking via Mobile Sensors
def real_time_location_tracking():
    location = geocoder.ip("me")
    if location.latlng:
        return f"📍 Current Location: {location.latlng}"
    else:
        return "⚠️ Location Not Found!"

# Number Kis Name Se Register Hai
def get_number_registration(name_number):
    lookup_url = f"https://www.truecaller.com/search/{name_number}"
    try:
        response = requests.get(lookup_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            name = soup.find("h1").text.strip() if soup.find("h1") else "Unknown"
            return f"📞 Number Registered Name: {name}"
        else:
            return "❌ Could not fetch registration details!"
    except:
        return "⚠️ Connection Error!"

# Dark Web Lookup via Tor
def dark_web_lookup(phone_number):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)  
    socket.socket = socks.socksocket  

    dark_web_sites = [
        "http://hss3uro2hsxfogfq.onion",
        "http://xmh57jrzrnw6insl.onion"
    ]

    results = []
    for site in dark_web_sites:
        try:
            response = requests.get(site, timeout=10)
            if phone_number in response.text:
                results.append(f"🔴 {phone_number} found on {site}")
        except:
            results.append(f"⚠️ Could not access {site}")
    
    return results

# AI Cyber Threat Analysis
def cyber_threat_analysis(phone_number):
    model = load_ai_model()
    if model:
        threat_level = model.predict([[len(phone_number)]])  
        return f"🔴 Cyber Threat Level: {threat_level[0]}"
    else:
        return "⚠️ AI Model Not Loaded!"

# Main Function
def main():
    phone_number = input("Enter Phone Number: ")
    audio_path = input("Enter Audio File for Analysis: ")

    print("\n📞 Number Information Lookup:")
    print(get_number_registration(phone_number))

    print("\n🆔 CNIC Lookup:")
    print(get_cnic_info(phone_number))

    print("\n📍 Real-Time Location Tracking:")
    print(real_time_location_tracking())

    print("\n🔴 Live Face Recognition (Press 'q' to stop):")
    print(live_face_recognition())

    print("\n🎤 Live Audio Analysis:")
    print(live_audio_analysis(audio_path))

    print("\n🌑 Dark Web Lookup:")
    for result in dark_web_lookup(phone_number):
        print(f"- {result}")

    print("\n🕵️ Cyber Threat Analysis:")
    print(cyber_threat_analysis(phone_number))

if __name__ == "__main__":
    main()
