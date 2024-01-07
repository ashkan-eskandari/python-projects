import os
from pypdf import PdfReader
import requests

text_to_speech_URL = "http://api.ispeech.org/api/rest?action=convert"
SPEECH_API_KEY = os.environ.get("SPEECH_API_KEY")


def get_audio(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    response = requests.post(
        'https://api.v6.unrealspeech.com/speech',
        headers={
            'Authorization': f'Bearer {SPEECH_API_KEY}'
        },
        json={
            'Text': text,  # Up to 500,000 characters
            "VoiceId": "Liv",
            "Bitrate": "192k",
            "Pitch": 1.02,
            "Speed": 0.1
        }
    )
    data = response.json()
    output_uri = data["OutputUri"]
    audio_response = requests.get(output_uri)
    audio_content = audio_response.content

    audio_file_path = "UPLOADS/audio/audio_path.mp3"
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(audio_content)
    return audio_file_path
