import os
import struct
import time
import wave
from typing import List

from pvrecorder import PvRecorder

from AudioProcessing import AudioProcessor


class AudioRecorder:
    """
    Audio recorder class which will record user audio from the selected microphone.
    Saves the audiofile to a base directory followed by a timestamp.
    """
    def __init__(self, microphone_index, output_dir: str="./", frame_length: int=512, base_path_to_file: str = "./"):
        self._recorder: PvRecorder = PvRecorder(frame_length=frame_length, device_index=microphone_index)
        self._audio: List = []
        self._base_path_to_file: str = output_dir

    def record(self):
        """
        Begins recording from microphone
        :return: filepath to audiofile
        """
        print("Once you are done recording, press ctrl+c to finish.")
        # self._recorder.set_debug_logging(True)
        time_stamp = time.time()
        filepath = f"recording_{time_stamp}.wav"

        try:
            self._recorder.start()
            while True:
                frame = self._recorder.read()
                self._audio.extend(frame)
        except KeyboardInterrupt:
            self._recorder.stop()
            with wave.open(filepath, "w") as f:
                f.setparams((1,2,16000,512, "NONE", "NONE"))
                f.writeframes(struct.pack("h" * len(self._audio), *self._audio))
        finally:
            print("Done recording..")
            self._recorder.delete()
            processor = AudioProcessor()
            print("processing... please wait")
            processor.processAudio(filepath)

        return filepath
