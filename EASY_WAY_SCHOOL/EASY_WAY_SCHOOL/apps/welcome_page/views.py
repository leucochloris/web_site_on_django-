from django.http import HttpResponse


def welcome(request):
    return HttpResponse('EASY WAY приветствует Вас!!!')


def about(request):
    return HttpResponse('We are - school of education English language "EASY WAY" 📚📖📕\n\n'
                        'Our company is young startup with a potential of billion of dollars! 🤑💵💰\n'
        '\nWe have schools and representative offices in 5 cities. Other 10 cities are in the plans ✈✈✈\n\n')
