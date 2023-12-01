from django.urls import path
from . import views
from .views import CarroCreate ,MotoCreate, CarroList, MotoList, AnuncioUpdate, CarroUpdate,teste, CarroDelete, MotoDelete, MeusCarros, MinhasMotos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CarroList.as_view(), name='index'),
    path('motos/', MotoList.as_view(), name='motos'),
    path('teste/', views.teste, name='teste'),
    path('carro-create/', CarroCreate.as_view(), name='carro-create'),
    path('moto-create/', MotoCreate.as_view(), name='moto-create'),
    path('editar/veiculo/<int:pk>/', AnuncioUpdate.as_view(), name='editar-veiculo'),
    path('editar/carro/<int:pk>/', CarroUpdate.as_view(), name='editar-carro'),
    path('excluir/carro/<int:pk>/', CarroDelete.as_view(), name='excluir-carro'),
    path('excluir/moto/<int:pk>/', MotoDelete.as_view(), name='excluir-moto'),
    path('lista/carros/', MeusCarros.as_view(), name='anuncio-carro'),
    path('lista/motos/', MinhasMotos.as_view(), name='anuncio-moto'),
    path('<int:id>', views.detail_page, name='detail'),
    path('moto/<int:id>', views.detail_page_moto, name='detail_moto'),

    path('Peugeot/', views.Peugeot, name='Peugeot'),
    path('Ford/', views.Ford, name='Ford'),
    path('Tesla/', views.Tesla, name='Tesla'),
    path('chevrolet/', views.chevrolet, name='chevrolet'),
    path('porsche/', views.porsche, name='porsche'),
    path('camaro/', views.camaro, name='camaro'),
    path('Lamborghini/', views.Lamborghini, name='Lamborghini'),
    path('Panamera/', views.Panamera, name='Panamera'),
    path('Volkswagen/', views.Volkswagen, name='Volkswagen'),
    path('Ferrari/', views.Ferrari, name='Ferrari'),
    path('Gol/', views.Gol, name='Gol'),
    path('Model/', views.Model, name='Model'),


    path('Dafra/', views.Dafra, name='Dafra'),
    path('BMW/', views.BMW, name='BMW'),
    path('GS/', views.GS, name='GS'),
    path('Kawasaki/', views.Kawasaki, name='Kawasaki'),
    path('Z400/', views.Z400, name='Z400'),
    path('Suzuki/', views.Suzuki, name='Suzuki'),
    path('Honda/', views.Honda, name='Honda'),
    path('Yamaha/', views.Yamaha, name='Yamaha'),
    path('Factor/', views.Factor, name='Factor'),
    path('Ducati/', views.Ducati, name='Ducati'),
    path('Bimota/', views.Bimota, name='Bimota'),
    path('POP/', views.POP, name='POP'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)