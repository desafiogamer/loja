from django.shortcuts import render, get_object_or_404
from .forms import Usuarioforms
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect

def teste(request):
    return render(request, 'socialaccount/provider_list.html')

class UsuarioCreate(CreateView):
    form_class = Usuarioforms
    template_name = 'registrarUsuarios.html'
    success_url = reverse_lazy ('login')

    def form_valid(self, form):
        url = super().form_valid(form)
        Profile.objects.create(usuario=self.object)
        return url
    
    
class ProfileCreate(CreateView):
    model = Profile
    fields = ['dataa', 'cep', 'estado', 'cidade', 'cpf', 'nome', 'telefone', 'imagemPerfil']
    template_name = 'profileCreate.html' 
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['nome',  'cep','dataa' ,'estado' ,'cpf' ,'cidade' , 'telefone', 'imagemPerfil']
    template_name = 'perfil-usuario.html'
    success_url = reverse_lazy('profile-update')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus dados pessoais'
        context['botao'] = 'Atualizar'

        return context
    
class MyPasswordReset(PasswordResetView):
    template_name = 'password_reset_form.html'


class MyPasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'redefinir_senha.html', {'form_senha': form_senha})