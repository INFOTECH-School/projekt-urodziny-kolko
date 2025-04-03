from django.urls import path
from .views import niespodzianka, Czas
urlpatterns = [
    path('chebanyjarnuch/<int:id>/', niespodzianka),

    path('aktualna_godzina/<int:strefa_czasowa>/', Czas.as_view(), name='godzina' ),
]