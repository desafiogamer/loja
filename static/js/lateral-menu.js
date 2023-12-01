var btn = document.querySelector('#menu-hamburger');
var Menu_lateral = document.querySelector('#MenuMobile');
var ul = document.querySelector('#lista-nao-ordenada');
var pesquisa = document.querySelector('.pesquisa');
var btn_filtro = document.querySelector('.menu-hamburger2');


btn.addEventListener('click', function(){
    Menu_lateral.classList.toggle('ativo');
});

btn_filtro.addEventListener('click', function(){
    pesquisa.classList.toggle('ativo');
});

ul.addEventListener('click', function(){
    Menu_lateral.classList.remove('ativo');
    pesquisa.classList.remove('ativo');
});

