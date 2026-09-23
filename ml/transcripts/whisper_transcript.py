import whisper


class WhisperTranscriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file):
        """
        Convert audio/video speech into timestamped transcript segments.
        """

        result = self.model.transcribe(
            audio_file,
            verbose=False
        )

        segments = []

        for segment in result["segments"]:
            segments.append({
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"].strip()
            })

        return segments