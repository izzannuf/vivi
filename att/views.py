from django.http import JsonResponse
from django.shortcuts import render
import openai
from pydub import AudioSegment
import openai
import tempfile
import os
import math

openai.api_key = "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"

# Create your views here.
def index(request):
    return render(request, 'att.html')

def transcribe(request):
    if request.method == 'POST' and request.FILES['audio-file']:
        # handle audio file
        audio_file = request.FILES['audio-file']

        result = split_audio_file(audio_file)

        transcript = {"text": result}

        return JsonResponse(transcript)
        
    return render(request, 'audio_to_text.html')

def split_audio_file(uploaded_file):
    # Initialize the result variable
    result = ""

    # Open the audio file using PyDub
    audio = AudioSegment.from_file(uploaded_file.file, format=uploaded_file.name.split('.')[-1])

    # Calculate the file size
    file_size = len(audio.raw_data)

    # Calculate the number of parts the audio file should be split into
    n = math.ceil(file_size / 25000000)

    # Calculate the duration of each part in milliseconds
    duration = len(audio) // n

    # Extract the file extension from the input file name
    file_extension = os.path.splitext(uploaded_file.name)[1]

    # Split the audio file into n equal parts
    for i in range(n):
        start_time = i * duration
        end_time = (i + 1) * duration

        # If this is the last part, set the end time to the end of the audio file
        if i == n - 1:
            end_time = len(audio)

        part_audio = audio[start_time:end_time]

        # Create a temporary file for the output audio with the same file extension as the input file
        with tempfile.NamedTemporaryFile(suffix=file_extension) as temp_file:
            # Save the output audio to the temporary file
            part_audio.export(temp_file.name, format=file_extension[1:])

            # Open the temporary file and transcribe the audio
            with open(temp_file.name, 'rb') as f:
                response = openai.Audio.transcribe("whisper-1", f, language='id')
                result += " "
                result += response['text']

    return result
