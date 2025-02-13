from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.
def Home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context) 

class RecipesViewList(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

class RecipeDetailList(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    # Checks if user is author of recipe or if user is a super user (admin of site) 
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_superuser


def About(request):
    return render(request, "recipes/about.html", {'title': 'About us'})