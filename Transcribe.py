from typing import List

import whisper
from pydub import AudioSegment



class Transcriber:
    def __init__(self, path_to_audio_file, segments):
        self.segments: List = segments
        self.transcriptions: List = []
        self._model: whisper = whisper.load_model("base")
        self._audio: AudioSegment = AudioSegment.from_file(path_to_audio_file)

    def transcribe(self):
        for segment in self.segments:
            start_ms = int(segment.start_sec * 1000)  # Convert seconds to milliseconds
            end_ms = int(segment.end_sec * 1000)
            speaker = f"Speaker {segment.speaker_tag}"

            # Segment the audio
            audio_segment = self._audio[start_ms:end_ms]

            # Export the segment to a temporary file
            temp_filename = "temp_segment.wav"
            audio_segment.export(temp_filename, format="wav")

            # Transcribe the audio segment
            result = self._model.transcribe(temp_filename)
            transcription = result["text"]

            # Add the transcription and speaker to the list
            self.transcriptions.append((speaker, transcription))
            for speaker, text in self.transcriptions:
                print(f"{speaker} said: {text}")
