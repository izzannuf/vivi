from django.http import JsonResponse
from django.shortcuts import render
import openai
from django.http import HttpResponse


openai.api_key = "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"

# Create your views here.
def index(request):

    try:

        text = request.POST.get('text')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "user", "content": "Lengkapi kalimat ini: {} - Tema dari teks ini adalah ___".format(text)}
                ]
        )

        theme = response["choices"][0]["message"]["content"]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "user", "content": "Buatlah rangkuman dari teks ini: {}".format(text)}
                ]
        )

        summary = response["choices"][0]["message"]["content"]

        context = {'theme' : theme, 'summary' : summary}
        return render(request, 'summarize.html', context)

    except Exception as e:
        return render(request, 'summarize_error.html')
