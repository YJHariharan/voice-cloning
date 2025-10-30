import os
import time
import gradio as gr
from threading import Lock
from indextts.infer_v2 import IndexTTS2
from openai import OpenAI

# -----------------------
# Paths
# -----------------------
ROOT = os.path.abspath(os.path.dirname(__file__))
CHECKPOINTS = os.path.join(ROOT, "checkpoints")
VOICES = os.path.join(ROOT, "voices")
OUTPUT = os.path.join(ROOT, "www", "output")
os.makedirs(VOICES, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

# -----------------------
# Initialize OpenAI client
# -----------------------
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("❌ No OpenAI API key found. Please set OPENAI_API_KEY first.")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# -----------------------
# Load IndexTTS
# -----------------------
print("Loading IndexTTS voice model...")
tts = IndexTTS2(
    cfg_path=os.path.join(CHECKPOINTS, "config.yaml"),
    model_dir=CHECKPOINTS,
    use_fp16=False,
    use_cuda_kernel=False,
    use_deepspeed=False
)
print("✅ RADHA TTS ready.")
_tts_lock = Lock()

# -----------------------
# Generate text using GPT-4o
# -----------------------
def generate_text(prompt: str):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are RADHA, an intelligent and friendly voice AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI Error] {e}"

# -----------------------
# Voice synthesis
# -----------------------
def synthesize_reply(reply_text: str, speaker="radha"):
    spk_file = os.path.join(VOICES, f"{speaker}_prompt.wav")
    if not os.path.exists(spk_file):
        raise FileNotFoundError(f"Missing speaker file: {spk_file}")
    out_file = os.path.join(OUTPUT, f"radha_reply_{int(time.time()*1000)}.wav")
    with _tts_lock:
        tts.infer(
            spk_audio_prompt=spk_file,
            text=reply_text,
            output_path=out_file,
            verbose=False
        )
    return out_file

# -----------------------
# Chat + Speak
# -----------------------
def radha_chat(user_text, history):
    if history is None:
        history = []
    reply = generate_text(user_text)
    try:
        wav = synthesize_reply(reply, speaker="radha")
    except Exception as e:
        history.append((user_text, f"[TTS error: {e}]"))
        return history, None
    history.append((user_text, reply))
    return history, wav

# -----------------------
# Gradio UI
# -----------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🎙️ RADHA — ChatGPT Intelligence + Cloned Voice")
    chatbot = gr.Chatbot()
    txt = gr.Textbox(label="Message RADHA")
    audio_out = gr.Audio(type="filepath", label="RADHA's Voice")
    send = gr.Button("Send")
    send.click(radha_chat, inputs=[txt, chatbot], outputs=[chatbot, audio_out])

demo.launch(server_name="0.0.0.0", server_port=7860)
