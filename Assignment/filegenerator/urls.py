from django.urls import path

from filegenerator import views


app_name="filegenerator"

urlpatterns = [
    path("generate-file/", views.generate_file)
]