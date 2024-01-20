from django.urls import path
from . import views
urlpatterns = [
    
    path('about/',views.about,name = 'aboutpage'),
    path('form/',views.submit,name = 'submit'),
    # path('django_form/',views.DjangoForm,name = 'django_form'),
    path('django_form/',views.DjangoForm,name = 'django_form'),

]