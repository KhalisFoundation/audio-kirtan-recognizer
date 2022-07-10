
# Imports the Google Cloud client library
from google.cloud import speech
from urllib.parse import urlparse
import json
from google.protobuf.json_format import MessageToJson


class GurbaniTransciber():
    def __init__(self):
        # Instantiates a client
        self.client = speech.SpeechClient()

    def gcs_audio(self, gcs_uri:str, save_local_json=None):

        audio = speech.RecognitionAudio(uri=gcs_uri)

        if gcs_uri.endswith(".flac"):
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
                sample_rate_hertz=44100,
                language_code="pa-Guru-IN",
                audio_channel_count=2,
            )
        elif gcs_uri.endswith(".wav"):
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=44100,
                language_code="pa-Guru-IN",
                audio_channel_count=2,
            )
        else:
            raise Exception("Unsupported file type")

        # Detects speech in the audio file
        operation = self.client.long_running_recognize(config=config,
                                                       audio=audio,
                                                       )

        print("Waiting for operation to complete...")
        response = operation.result(timeout=60)
        print(f"{type(response)}")
        return response

    @staticmethod
    def print_transcription_response(response):
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        print(f"Billed for {response.total_billed_time}")
        print(f"Output Config {response.output_config}")
        print(f"Output Error {response.output_error}")
        print(f"Segments found {len(response.results)}")
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print(f"channel tag {result.channel_tag}")
            print(f"result_end_time {result.result_end_time}")
            print(f"language Code {result.language_code}")
            print(u"Transcript: {}".format(result.alternatives[0].transcript))
            print("Confidence: {}".format(result.alternatives[0].confidence))

    def stream_audio(self, chunked_audio_data):
        return
