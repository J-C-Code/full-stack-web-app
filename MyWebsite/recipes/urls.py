
from django.urls import path, include
from . import views


'app-model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path("", views.RecipesViewList.as_view(), name="recipes-home"),
    path("recipe/<int:pk>", views.RecipeDetailList.as_view(), name="recipes-detail"),
    path("recipe/<int:pk>/update", views.RecipeUpdateView.as_view(), name="recipes-update"),
    path("recipe/<int:pk>/delete", views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path("recipe/create", views.RecipeCreateView.as_view(), name="recipes-create"),
    path("about/", views.About, name="recipes-about")
]
