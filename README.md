# 🧠 Voice Cloning using Deep Learning

## NOTE : It can only run on cmd , this is the sample version , will update the advanced version !

## 📌 Overview
The **Voice Cloning Project** is a deep learning–based system that can replicate a human voice using a small sample of speech.  
By combining **Text-to-Speech (TTS)** synthesis, **Speaker Embeddings**, and **Neural Vocoders**, this project generates natural and expressive cloned speech that closely matches the target speaker’s tone, pitch, and style.

---

## 🎯 Problem Statement
The challenge is to build a model capable of cloning a speaker’s voice using limited voice samples.  
The cloned voice should maintain **clarity, emotional tone**, and **linguistic accuracy** across various text inputs.

---

## 🔍 Scope
This project focuses on implementing and evaluating a **neural speech synthesis pipeline** that integrates:
- Speaker encoding networks to capture vocal identity  
- Text-to-speech models for linguistic content  
- Neural vocoders (like **WaveGlow** or **HiFi-GAN**) for realistic audio generation  

**Applications include:**
- Personalized virtual assistants  
- Audiobook and film dubbing  
- Accessibility tools for speech-impaired users  
- Interactive gaming and entertainment

---

## ⚙️ Tools & Tech Stack
| Category | Tools/Frameworks |
|-----------|------------------|
| Programming Language | Python |
| Deep Learning | PyTorch, TensorFlow |
| Audio Processing | Librosa, Soundfile, NumPy |
| Visualization | Matplotlib |
| Frameworks | Tacotron2, WaveGlow, Real-Time Voice Cloning |
| IDE | Visual Studio Code / Google Colab |
| Dataset | LibriSpeech, VCTK Corpus |
| OS | Windows / Linux (GPU Recommended) |

---

## 🧩 Project Structure
Voice-Cloning/
├── data/ # Dataset (Not included due to size)
├── models/ # Pre-trained models (Download link below)
├── src/ # Python source code
├── output/ # Generated audio samples
├── requirements.txt # Dependencies list
├── README.md # Project documentation
└── report.pdf # Final report document


---

## 🗃️ Download Large Files
Due to GitHub’s storage limits, the trained models and datasets are hosted externally.

📦 **Download Here:**  
🔗 https://drive.google.com/drive/folders/1IdUcPRMrdm8sL6u1uU8u8CcXvb4OtpK3?usp=drive_link
*(Includes trained models, datasets, and example cloned audio.)*

---

## 🚀 How to Run
🧱 Step 1 — Clone the Repository
git clone https://github.com/yourusername/voice-cloning.git
cd voice-cloning

🐍 Step 2 — Create a Virtual Environment
python -m venv venv

⚡ Step 3 — Activate the Virtual Environment

Windows (CMD / PowerShell):

venv\Scripts\activate


Mac / Linux / WSL:

source venv/bin/activate


✅ You’ll see (venv) appear in your terminal, which means the virtual environment is active.

📦 Step 4 — Upgrade PIP
pip install --upgrade pip

📚 Step 5 — Install Dependencies

If you have a requirements.txt file:

pip install -r requirements.txt


Or, if you’re setting up manually (for your voice cloning stack):

pip install torch torchvision torchaudio
pip install tensorflow==2.12.0
pip install librosa soundfile numpy matplotlib
pip install pydub tqdm

🎧 Step 6 — Install FFmpeg (for audio processing)

Windows:

Download from https://ffmpeg.org/download.html

Extract and add the /bin path to your System Environment Variables.

Linux (Ubuntu/Debian):

sudo apt update
sudo apt install ffmpeg


Mac (Homebrew):

brew install ffmpeg

🧠 Step 7 — Add Checkpoints, Models, and Samples

Since large files aren’t uploaded to GitHub, download them from your Google Drive link and place them like this:

voice-cloning/
├── checkpoints/
├── models/
├── tts_samples/
└── src/

🚀 Step 8 — Run the Project
 run sample_tts.py
 run python.py
 run main.py
 run app.py

Example command to generate cloned speech:

python src/clone_voice.py --input_text "Hello! This is an AI cloned voice." --speaker sample.wav

💾 Step 9 — Output Location

Generated audio files will appear in:

output/
└── cloned_voice.wav

🧹 Step 10 — Deactivate the Virtual Environment

When you’re done:

deactivate
