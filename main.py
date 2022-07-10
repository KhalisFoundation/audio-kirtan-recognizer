from asr.transcribe import GurbaniTransciber

if __name__ == "__main__":
    gurbani_transcriber = GurbaniTransciber()

    vocal_files = [
        "gs://anand-sahib/vocals/Sample01_Anand_Sahib_vocals.flac",
        "gs://anand-sahib/vocals/Song1/segment0/vocals.wav"
        # "gs://anand-sahib/audio/Song1/segment0.wav" - has an error
    ]

    for v_file in vocal_files:
        response = gurbani_transcriber.gcs_audio(v_file)
        GurbaniTransciber.print_transcription_response(response)


    # audio_files = [
    #     "gs://anand-sahib/audio/Sample01_Anand_Sahib.flac",
    #     "gs://anand-sahib/audio/Sample02_Anand_Sahib.flac",
    #     "gs://anand-sahib/audio/Sample03_Anand_Sahib.flac",
    # ]
    #
    # for a_file in audio_files:
    #     gurbani_transcriber.gcs_audio(a_file)
