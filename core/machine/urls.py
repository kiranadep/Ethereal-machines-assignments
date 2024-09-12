from django.urls import path
from .views import MachineListCreateView, MachineDetailView, MachineHistoricalDataView

urlpatterns = [
    path('', MachineListCreateView.as_view(), name='machine-list-create'), 
    path('<int:pk>/', MachineDetailView.as_view(), name='machine-detail'), 
    path('historical/', MachineHistoricalDataView.as_view(), name='machine-historical-data'), 
]
