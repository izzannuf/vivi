from django.http import JsonResponse
from django.shortcuts import render
import openai
from django.http import HttpResponse


openai.api_key = "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"

# Create your views here.
def index(request):
    text = request.POST.get('text')
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": "Apa tema dari teks ini?: {}".format(text)}
            ]
    )

    theme = response["choices"][0]["message"]["content"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": "Apa intisari dari teks ini?: {}".format(text)}
            ]
    )

    summary = response["choices"][0]["message"]["content"]

    context = {'theme' : theme, 'summary' : summary}
    return render(request, 'summarize.html', context)