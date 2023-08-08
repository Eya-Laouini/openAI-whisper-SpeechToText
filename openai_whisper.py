import whisper
import numpy as np
from pydub import AudioSegment
from IPython.display import Audio, display

def main():
    model = whisper.load_model("base")

    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("model.mp3")
    audio = whisper.pad_or_trim(audio)

    # Convert NumPy array to AudioSegment for playback
    audio_segment = AudioSegment(
        data=np.int16(audio * 32767),  # Convert to 16-bit signed PCM
        sample_width=2,  # 16-bit audio
        frame_rate=audio.shape[0] // 30,  # Set the frame rate
        channels=1  # Assuming mono audio
    )

    # Display the audio using IPython.display.Audio
    display(Audio(data=audio_segment.raw_data, rate=audio_segment.frame_rate))

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")

    # Decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    #Print the recognized text
    print("Recognized text:")
    print(result.text)

if __name__ == "__main__":
    main()