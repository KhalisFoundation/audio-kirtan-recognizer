# audio-kirtan-recognizer
Audio Kirtan Recognizer

# authenticate w/ google cloud
```gcloud auth application-default login```

Note: APIs for Automatic speech to text should be enabled

# upload audio files to google cloud storage
* get gs_urls of the audio files
* ghe format will be something like `gs://my_bucket_name//path_to_audio_file`
* edit the main.py file and run it
```
python main.py
```

# convering mp3 to flac
 ffmpeg -i input.mp3 output.flac

# Collab links
[Audio File Segmentation](https://colab.research.google.com/drive/1lTl3DV7D--YcL6d0GpbocdxDdMOwXPw7)

[Music Source separation](https://colab.research.google.com/drive/1KfkPhuNtizmCpNHU0jkSo3tOrrJx6qAR)

[ASR Transcription to BaniDB](https://colab.research.google.com/drive/1q9dHjDWa1A_rorn-QvXVldiCoUm0THrr?usp=sharing)
