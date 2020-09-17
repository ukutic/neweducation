from django.shortcuts import render
from ..wings from models

# Create your views here.
class Saiten(View):
    def get(self, request, *args, **kwargs):
        answer = request
        if answer == seikai :
            message = "正解!!"
        else:
            message = "不正解"
        context = {
            'message': message,
            'answer':answer,
            'seikai':question.seikai,
            'kaisetu': question.kaisetu,
        }
        return render(request, 'answer.html', context)

    def post(self, request, *args, **kwargs):
        answer = request
        if answer == seikai :
            message = "正解!!"
        else:
            message = "不正解"
        context = {
            'message': message,
            'answer':answer,
            'seikai':question.seikai,
            'kaisetu': question.kaisetu,
        }
        return render(request, 'answer.html', context)

saiten = Saiten.as_view()
