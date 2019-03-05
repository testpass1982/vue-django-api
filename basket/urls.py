from django.urls import path

# import basket.views as basket
# from basket.views import ProductList
from django.views.generic import TemplateView

app_name = 'basket'

urlpatterns = [
    # path('', ProductList.as_view()),
    path('', TemplateView.as_view(template_name='basket/index.html')),
    # path('details/<slug:pk>', basket.details, name='details'),
    # path('new/', basket.create, name='create'),
    # path('update/<slug:pk>', basket.update, name='update'),
    # path('delete/<slug:pk>', basket.delete, name='delete'),
]