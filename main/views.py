from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496100',
        'name': 'Emilio Junino Rizanvidri Pao',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
