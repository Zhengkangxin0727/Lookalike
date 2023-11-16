from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('g/', views.g),
    path('get_keywords/', views.get_keywords),
    path('upload/',views.upload_account_ids),
    path('index1/', views.index1, name='index1'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('get_suggestions/', views.get_suggestions, name='get_suggestions'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('fn2/', views.fn2_view, name='fn2'),
    path('index3/', views.index3, name='index3'),
    # path('indextest/',views.indextest,name = 'indextest'),
    path('submit/', views.submit_form, name='submit_form'),
   
]
