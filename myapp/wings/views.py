from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from .models import Category, Question
from .forms import SearchForm

class Index(View):
    model =  Question
    template_name = 'index'
    def get(self,request,*args,**kwargs):
        searchForm = SearchForm(request.GET)
        if searchForm.is_valid():
            keyword = searchForm.cleaned_data['keyword']
            questions = Question.objects.filter(category__name__icontains=keyword)
        else:
            searchForm = SearchForm()
            questions = Question.objects.all()

        context = {
            'questions':questions,
            'searchForm':searchForm,
        }
        return render(request,'wings/index.html',context)

index_view = Index.as_view()

    #def get_queryset(self):
    #    return Question.objects.filter(category_name

class DetailView(generic.DetailView):
    model = Question