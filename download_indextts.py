from huggingface_hub import snapshot_download

print("⬇️ Downloading IndexTTS checkpoints into ./checkpoints ...")
snapshot_download(repo_id="IndexTeam/IndexTTS-2", local_dir="checkpoints", resume_download=True)
print("✅ Done! Files are in ./checkpoints")
