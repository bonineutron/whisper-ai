import whisper

model = whisper.load_model("tiny")
result = model.transcribe("audio.mp3", fp16=False, language="en")
print(result["text"])