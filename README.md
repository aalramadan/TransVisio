# **TransVisio**
![image](https://github.com/aalramadan/TransVisio/assets/55710790/090c74e7-6d86-428a-853f-4c93154d61f0)

## **💡What does it do?**
**TransVisio** is a tool designed to transcribe and translate text from various input formats, such as video and audio. It utilizes a pipeline of AI models to seamlessly transcribe and translate text in real-time.

## **Transcription Models Supported**
- **Whisper 20231117 (Online)**
- **Faster-Whisper v1.0.3 (Offline)**

## **Translation Models Supported**
- **GPT 4o**
- **GPT 4 Turbo**
- **GPT 3 Turbo**
- **Gemini 1.5 Pro**
- **Gemini 1.5 Flash**

## **Features**
- Inputs supported: </br>
```
Subtitle files (*.srt *.ass *.ssa). 
Video files (*.mp4 *.mkv *.webm *.flv *.avi *.mov *.wmv *.m4v).
Audio files (*.wav *.ogg *.mp3 *.aac *.flac *.m4a *.oga *.opus). 
Excel files (*.xlsx *.csv).
```
- **Input Sentences:** Specify the number of input sentences to translate at once (higher = more context).
- **Pause/Resume:** Control translation process at any point.
- **Reverse Translation:** Switch the direction of the translated output for easier editing in certain languages.
- **Edit and Align:** Remove or edit the translated output and input with automatic row alignment.
- **Specify Start Time and Duration:** Set the starting point and the length of the transcription for video and audio inputs.
- **Temperature Setting:** Control the randomness of the translation model’s output. Lower values make the output more deterministic, while higher values increase diversity.
- **Save Transcriptions:** Export video and audio transcriptions to Excel.
- **Themes:** Choose between light and dark themes.

## **Demo**
> Usage Notes:</br>
> Specify the **Start Time** and **Duration** before selecting the video or audio input.</br>
> Online Whisper requires an API key and is limited to a 25 MB input size.</br>
> Offline Whisper does not require a key but requires downloading a model (e.g., tiny, small) on the first use.

![Animation](https://github.com/aalramadan/TransVisio/assets/55710790/c4d47cb7-ca61-4779-ac78-68bd4591d95e)

## **Disclaimer**
- **TransVisio** is part of a collaborative research funded by the Abdul Hameed Shoman Foundation (Agreement Number: 230800351). </br>
- Hosting Institution: The project is hosted by the English Language and Translation Department at the Applied Science Private University. </br>
- Paper: Abu-Rayyash, H., & Haider, A. S. (2024). Introducing Transvisio: A customizable AI-powered subtitling tool.
