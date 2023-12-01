const filtro = document.querySelector('.filter')
const backFiltro = document.querySelector('.filtro')
const filtro2 = document.querySelector('.filtro div')
const fecharMenu1 = document.querySelector('.list1');
const fecharMenu2 = document.querySelector('.list2');
const fecharMenu3 = document.querySelector('.list3');
const fecharMenu4 = document.querySelector('.list4');
const fecharMenu5 = document.querySelector('.list5');
const fecharMenu6 = document.querySelector('.list6');
const fecharMenu7 = document.querySelector('.list7');
const fecharMenu8 = document.querySelector('.list8');
const fecharMenu9 = document.querySelector('.list9');
const body = document.querySelector('.carro-container');


filtro.addEventListener('click', function(){
    backFiltro.classList.add('ativo')
})

filtro2.addEventListener('click', function(){
    backFiltro.classList.remove('ativo')
})

fecharMenu1.addEventListener('click', function(){
    backFiltro.classList.remove('ativo')
})

fecharMenu2.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu3.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu4.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu5.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu6.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu7.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu8.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})

fecharMenu9.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})


body.addEventListener('click', function () {
    backFiltro.classList.remove('ativo')
})
