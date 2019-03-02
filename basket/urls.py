from django.urls import path

import basket.views as basket

app_name = 'vacancies'
urlpatterns = [
    path('', basket.index, name='index'),
    # path('details/<slug:pk>', basket.details, name='details'),
    # path('new/', basket.create, name='create'),
    # path('update/<slug:pk>', basket.update, name='update'),
    # path('delete/<slug:pk>', basket.delete, name='delete'),
]