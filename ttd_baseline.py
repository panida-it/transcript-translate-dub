import whisper
from googletrans import Translator
from gtts import gTTS
import os
import ffmpeg

# Step 1: Extract Audio from Video
os.system('ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.wav')

# Step 2: Transcribe Audio (using Whisper)
model = whisper.load_model("base")
result = model.transcribe("output_audio.wav")
english_transcript = result["text"]
with open("transcript.txt", "w") as f:
    f.write(english_transcript)

# Step 3: Translate Transcript (using Google Translate)
translator = Translator()
translated = translator.translate(english_transcript, src='en', dest='id')
indonesian_transcript = translated.text
with open("translated_transcript.txt", "w") as f:
    f.write(indonesian_transcript)

# Step 4: Convert Translated Transcript to Speech (using gTTS)
tts = gTTS(indonesian_transcript, lang='id')
tts.save("indonesian_dubbed_audio.mp3")

# Step 5: Merge Dubbed Audio with Video (using FFmpeg)
os.system('ffmpeg -i input_video.mp4 -i indonesian_dubbed_audio.mp3 -c:v copy -map 0:v:0 -map 1:a:0 output_video_with_dub.mp4')
