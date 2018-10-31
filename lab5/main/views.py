from django.shortcuts import render


# Create your views here.
def test(request):
    return render(request, 'main/test.html', {'x': ['Emir', 2, 3, 4, 5]})


def detail(request, id):
    return render(request, 'main/detail.html', {'id': id})
