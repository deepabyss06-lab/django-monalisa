from django.shortcuts import render

# Create your views here.
def dj_view(request):
    student={'name':'mona','roll no':12345,'gender':'female'}
    return render(request,'courseapp/dj.html',{'dic':student})