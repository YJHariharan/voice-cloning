import os
from indextts.infer_v2 import IndexTTS2

CHECKPOINTS = "checkpoints"
CFG = os.path.join(CHECKPOINTS, "config.yaml")

tts = IndexTTS2(cfg_path=CFG, model_dir=CHECKPOINTS,
                use_fp16=False, use_cuda_kernel=False, use_deepspeed=False)

prompt = "voices/radha_prompt.wav"
if not os.path.exists(prompt):
    raise SystemExit("❌ Put your sample as voices/radha_prompt.wav")

out = "www/output/test_reply.wav"
os.makedirs(os.path.dirname(out), exist_ok=True)

print("Generating test audio...")
tts.infer(spk_audio_prompt=prompt,
          text="i am from bangalore , who gets fucked by vishwa daily , and suck vishwa cock daily , i love his cock",
          output_path=out,
          verbose=True)
print("✅ Audio saved at:", out)
