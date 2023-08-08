# openAI-whisper-SpeechToText
**A speech-to-text model** is a type of artificial intelligence model designed to convert spoken language or audio input into written text. This technology is commonly used in applications like transcription services, voice assistants, and accessibility tools for individuals with hearing impairments. The model analyzes audio signals and predicts the corresponding text output.

**Whisper** is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.
## Installation

We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends on a few Python packages, most notably OpenAI's tiktoken for their fast tokenizer implementation. You can download and install (or update to) the latest release of Whisper with the following commands:

```bash
pip install -U openai-whisper
```
```bash
pip install pydub
```
```bash
pip install ipython
```
```bash
choco install ffmpeg
```

## file formats are supported

audio.flac 

audio.mp3 

audio.wav 

audio.mp4

audio.m4a

audio.webm

audio.mpga

audio.mpeg

## Usage

Put your voice file in the same project folder,

```python
def main():
    model = whisper.load_model("base")

    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("your_mp3_file.mp3")
    ...
```

## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed.

| **Size** | **Parameters**| **English-only model**|**Multilingual model**|**Required VRAM**|**	Relative speed**|
| -------- | --------------|-----------------------|----------------------|-----------------|-------------------|
| tiny     |      39 M     |        tiny.en        |         tiny         |     ~1 GB       |      ~32x         |
| base     |      74 M     |        base.en        |         base         |     ~1 GB       |      ~16x         |
| small    |     244 M     |        small.en       |         small        |     ~2 GB       |      ~6x          |
| medium   |     769 M     |        medium.en      |         medium       |     ~5 GB       |      ~2x          |
| large    |    1550 M     |          N/A          |         large        |     ~10 GB      |       1x          |

The .en models for English-only applications tend to perform better, especially for the tiny.en and base.en models. We observed that the difference becomes less significant for the small.en and medium.en models.

## Languages are supported 

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

## Next step

Now you have your own speech to text model! 
