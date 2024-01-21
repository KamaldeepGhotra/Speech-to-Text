from pvrecorder import PvRecorder

from Record import AudioRecorder
from AudioProcessing import AudioProcessor
from Transcribe import Transcriber


def main():
    voice_or_file = int(input("Would you like to record your voice (1) or input a audio file (2): "))

    # User wants to record voice
    if voice_or_file == 1:
        # display all current microphones in the system
        for index, device in enumerate(PvRecorder.get_available_devices()):
            print(f"[{index}] {device}")

        # Ask user for what microphone they would like to use
        microphone_selection = int(input("Enter the microphone index: "))

        recorder = AudioRecorder(microphone_index=microphone_selection)
        path_to_file = recorder.record()
    else:
        # User would like to input a wav file
        path_to_file = input("Please enter the path to the audio file: ")

    audio_processer = AudioProcessor() # Instantiate falcon using default key
    segments = audio_processer.processAudio(path_to_file) # list of segments
    transcriber = Transcriber(path_to_file, segments) # whisper
    transcriber.transcribe()

main()