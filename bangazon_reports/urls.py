from django.urls import path
from .views import ExpensiveProductList

urlpatterns = [
    path('reports/expensiveproducts', ExpensiveProductList.as_view()),
]
