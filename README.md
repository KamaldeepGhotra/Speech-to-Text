# Speech-to-Text
This program will convert speech to text using the chosen microphone on your system. Additionally, you will have the option to input a .wav file which will then also be transcribed to text. This program is implemented with speaker diarization to be able to recognize multiple speakers.

# How to run the Program
pip3 install pvfalcon
pip3 install flask
python -m venv env

source myenv/bin/activate

pip install openai
pip install python-docx

python3 main.py 
