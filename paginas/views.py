from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CarroForms, MotoForms
from .models import Anuncio, AnuncioMoto
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create views.

def teste(request):
    return render(request, 'teste.html')

class CarroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CarroForms
    template_name = 'anuciar-carro.html'
    success_url = reverse_lazy ('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url
    
class MotoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = MotoForms
    template_name = 'anuciar-moto.html'
    success_url = reverse_lazy ('motos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url


#update views

class AnuncioUpdate(UpdateView):
    model =  AnuncioMoto
    fields = ['moto', 'modelo', 'descricao', 'preco', 'data', 'km', "cidade", "troca", "Refrigeracao", "Partida", "cor", "ipva", "Cilindrada", "marchas"]
    template_name = 'updateViews/UpdateMotos.html'
    success_url = reverse_lazy('anuncio-moto')

    def get_object(self, queryset=None):
        self.object = AnuncioMoto.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CarroUpdate(UpdateView):
    model =  Anuncio
    fields = ['carro', 'modelo', 'descricao', 'preco', 'data', 'km', "cidade", "troca", "combustivel", "cambio", "cor", "ipva"]
    template_name = 'updateViews/UpdateVeiculos.html'
    success_url = reverse_lazy('anuncio-carro')

    def get_object(self, queryset=None):
        self.object = Anuncio.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

# list views

class CarroList(ListView):
    model = Anuncio
    template_name = 'index.html'

        
    
class MeusCarros(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Anuncio
    template_name = 'meus_anuncios/meus_anuncio_carro.html'

    def get_queryset(self):
        self.object_list = Anuncio.objects.filter(usuario=self.request.user)
        return self.object_list
    

class MinhasMotos(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = AnuncioMoto
    template_name = 'meus_anuncios/meus_anuncios_motos.html'

    def get_queryset(self):
        self.object_list = AnuncioMoto.objects.filter(usuario=self.request.user)
        return self.object_list
    
def detail_page(request, id):
    obj= get_object_or_404(Anuncio,pk=id)
    return render(request, 'detail-carro.html', {'obj':obj})


def detail_page_moto(request, id):
    obj= get_object_or_404(AnuncioMoto,pk=id)
    return render(request, 'detail-moto.html', {'obj':obj})
    
 
#anuncios moto
    
class MotoList(ListView):
    login_url = reverse_lazy('login')
    model = AnuncioMoto
    template_name = 'motos.html'

    def get_queryset(self):
        self.object_list = AnuncioMoto.objects.filter(usuario=self.request.user)
        return self.object_list
    
    def get_queryset(self):

        txt_numero = self.request.GET.get('numero')

        if txt_numero:
            atividade = AnuncioMoto.objects.filter(numero__icontains=txt_numero)
        else:
            atividade = AnuncioMoto.objects.all()

        return atividade


# delete views

class CarroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Anuncio
    template_name = 'DeleteViews/veiculo-excluir.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = Anuncio.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    

class MotoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = AnuncioMoto
    template_name = 'DeleteViews/veiculo-excluir.html'
    success_url = reverse_lazy('motos')

    def get_object(self, queryset=None):
        self.object = AnuncioMoto.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


#Carro individual

def Peugeot(request):
    return render(request, 'veiculos/Peugeot.html')

def Ford(request):
    return render(request, 'veiculos/Ford.html')

def Tesla(request):
    return render(request, 'veiculos/Tesla.html')

def chevrolet(request):
    return render(request, 'Chevrolet.html')

def porsche(request):
    return render(request, 'veiculos/Porsche.html')

def camaro(request):
    return render(request, 'veiculos/camaro.html')

def Lamborghini(request):
    return render(request, 'veiculos/Lamborghini.html')

def Panamera(request):
    return render(request, 'veiculos/Panamera.html')

def Volkswagen(request):
    return render(request, 'veiculos/Volkswagen.html')


def Ferrari(request):
    return render(request, 'veiculos/Ferrari.html')

def Gol(request):
    return render(request, 'veiculos/Gol.html')

def Model(request):
    return render(request, 'veiculos/Model.html')

#listas de Motos

def Dafra(request):
    return render(request, 'veiculos/motos/Dafra.html')

def BMW(request):
    return render(request, 'veiculos/motos/BMW.html')

def GS(request):
    return render(request, 'veiculos/motos/GS.html')

def Kawasaki(request):
    return render(request, 'veiculos/motos/Kawasaki.html')

def Z400(request):
    return render(request, 'veiculos/motos/Z400.html')

def Suzuki(request):
    return render(request, 'veiculos/motos/Suzuki.html')

def Honda(request):
    return render(request, 'veiculos/motos/Honda.html')


def Yamaha(request):
    return render(request, 'veiculos/motos/Yamaha.html')

def Factor(request):
    return render(request, 'veiculos/motos/Factor.html')

def Ducati(request):
    return render(request, 'veiculos/motos/Ducati.html')

def Bimota(request):
    return render(request, 'veiculos/motos/Bimota.html')

def POP(request):
    return render(request, 'veiculos/motos/POP.html')