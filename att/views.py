from django.http import JsonResponse
from django.shortcuts import render
import openai

openai.api_key = "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"

# Create your views here.
def index(request):
    return render(request, 'att.html')

def transcribe(request):
    if request.method == 'POST' and request.FILES['audio-file']:
        # handle audio file
        audio_file = request.FILES['audio-file']

        if audio_file.size > 25 * 1024 * 1024:
            return JsonResponse({"text" : "The file size is too big. Please upload a file not exceeding 25MBs."})

        else:
            # perform speech to text conversion and get the result
            transcript = openai.Audio.transcribe("whisper-1", audio_file, language="id")
            # return JSON response
            return JsonResponse(transcript)
        
    return render(request, 'audio_to_text.html')