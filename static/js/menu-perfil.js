var menu_perfil = document.querySelector('.hamburger');
var perfil = document.querySelector('.perfil-lateral');
var perfil_ususario = document.querySelector('.perfil-usuario');
var Menu_lateral = document.querySelector('#MenuMobile');

menu_perfil.addEventListener('click', function () {
    perfil.classList.toggle('ativo');
});

perfil_ususario.addEventListener('click', function () {
    perfil.classList.remove('ativo');
    Menu_lateral.classList.remove('ativo');
});
