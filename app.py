from flask import Flask, request, jsonify, render_template
# Import your custom classes for recording, processing, and transcribing
from Record import AudioRecorder
from Record import AudioProcessor
from Transcribe import Transcriber


app = Flask(__name__)

# Initialize the AudioProcessor here (if it doesn't require arguments upon initialization)
audio_processor = AudioProcessor()

# Global variable to hold the recorder instance
audio_recorder = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_record', methods=['POST'])
def start_record():
    global audio_recorder  # Declare as global to modify the global instance
    microphone_index = int(request.json['microphoneIndex'])
    audio_recorder = AudioRecorder(microphone_index)  # Initialize with the selected microphone index
    audio_recorder.start_recording()
    return jsonify(status="success", message=f"Recording started with microphone {microphone_index}")

@app.route('/stop_record', methods=['POST'])
def stop_record():
    global audio_recorder  # Access the global recorder instance
    if audio_recorder:
        file_path = audio_recorder.stop_recording()
        segments = audio_processor.process_audio(file_path)  # Process the audio file
        # You might want to store file_path and segments for later use in transcription
        return jsonify(status="success", message="Recording stopped", filePath=file_path, segments=segments)
    else:
        return jsonify(status="error", message="No active recording")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    file_path = request.json['filePath']
    segments = request.json['segments']
    # Initialize the Transcriber here with the required arguments
    transcriber = Transcriber(file_path, segments)
    transcription = transcriber.transcribe()
    return jsonify(status="success", transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True)
