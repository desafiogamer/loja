const slider = document.querySelectorAll('.slider');
const btnPrev = document.getElementById('prev-button');
const btnNext = document.getElementById('next-button');

let currentSlide = 0;

function hideSlider() {
    slider.forEach(item => item.classList.remove('on'))
}

function showSlider() {
    slider[currentSlide].classList.add('on')
}

function nextSlider() {
    hideSlider()
    if (currentSlide === slider.length - 1) {
        currentSlide = 0
    } else {
        currentSlide++
    }
    showSlider()
}

function prevSlider() {
    hideSlider()
    if (currentSlide === 0) {
        currentSlide = slider.length - 1
    } else {
        currentSlide--
    }
    showSlider()
}

btnNext.addEventListener('click', nextSlider)
btnPrev.addEventListener('click', prevSlider)



//slider mustang

const slider1 = document.querySelectorAll('.slider1');
const btnPrev1 = document.getElementById('prev-buttonn');
const btnNext1 = document.getElementById('next-buttonn');


let currentSlides = 0;

function hideSliderr() {
    slider1.forEach(item => item.classList.remove('on'))
}

function showSliderr() {
    slider1[currentSlides].classList.add('on')
}

function nextSliderr() {
    hideSliderr()
    if (currentSlides === slider1.length - 1) {
        currentSlides = 0
    } else {
        currentSlides++
    }
    showSliderr()
}

function prevSliderr() {
    hideSliderr()
    if (currentSlides === 0) {
        currentSlides = slider1.length - 1
    } else {
        currentSlides--
    }
    showSliderr()
}

btnNext1.addEventListener('click', nextSliderr)
btnPrev1.addEventListener('click', prevSliderr)




//SLIDER tesla
const sliderTesla = document.querySelectorAll('.sliderTesla');
const btnPrevTesla = document.getElementById('prev-buttonTesla');
const btnNextTesla = document.getElementById('next-buttonTesla');


let currentSlidesTesla = 0;

function hideSliderTesla() {
    sliderTesla.forEach(item => item.classList.remove('on'))
}

function showSliderTesla() {
    sliderTesla[currentSlidesTesla].classList.add('on')
}

function nextSliderTesla() {
    hideSliderTesla()
    if (currentSlidesTesla === sliderTesla.length - 1) {
        currentSlidesTesla = 0
    } else {
        currentSlidesTesla++
    }
    showSliderTesla()
}

function prevSliderTesla() {
    hideSliderTesla()
    if (currentSlidesTesla === 0) {
        currentSlidesTesla = sliderTesla.length - 1
    } else {
        currentSlidesTesla--
    }
    showSliderTesla()
}

btnNextTesla.addEventListener('click', nextSliderTesla)
btnPrevTesla.addEventListener('click', prevSliderTesla)



//SLIDER PORSHE
const sliderPorsche = document.querySelectorAll('.sliderPorsche');
const btnPrevPorsche = document.getElementById('prev-buttonPorsche');
const btnNextPorsche = document.getElementById('next-buttonPorsche');


let currentSlidesPorsche = 0;

function hideSliderPorsche() {
    sliderPorsche.forEach(item => item.classList.remove('on'))
}

function showSliderPorsche() {
    sliderPorsche[currentSlidesPorsche].classList.add('on')
}

function nextSliderPorsche() {
    hideSliderPorsche()
    if (currentSlidesPorsche === sliderPorsche.length - 1) {
        currentSlidesPorsche = 0
    } else {
        currentSlidesPorsche++
    }
    showSliderPorsche()
}

function prevSliderPorsche() {
    hideSliderPorsche()
    if (currentSlidesPorsche === 0) {
        currentSlidesPorsche = sliderPorsche.length - 1
    } else {
        currentSlidesPorsche--
    }
    showSliderPorsche()
}

btnNextPorsche.addEventListener('click', nextSliderPorsche)
btnPrevPorsche.addEventListener('click', prevSliderPorsche)



//slider Chevrolet
const sliderChevrolet = document.querySelectorAll('.sliderChevrolet');
const btnPrevChevrolet = document.getElementById('prev-buttonChevrolet');
const btnNextChevrolet = document.getElementById('next-buttonChevrolet');


let currentSlidesChevrolet = 0;

function hideSliderChevrolet() {
    sliderChevrolet.forEach(item => item.classList.remove('on'))
}

function showSliderChevrolet() {
    sliderChevrolet[currentSlidesChevrolet].classList.add('on')
}

function nextSliderChevrolet() {
    hideSliderChevrolet()
    if (currentSlidesChevrolet === sliderChevrolet.length - 1) {
        currentSlidesChevrolet = 0
    } else {
        currentSlidesChevrolet++
    }
    showSliderChevrolet()
}

function prevSliderChevrolet() {
    hideSliderChevrolet()
    if (currentSlidesChevrolet === 0) {
        currentSlidesChevrolet = sliderChevrolet.length - 1
    } else {
        currentSlidesChevrolet--
    }
    showSliderChevrolet()
}

btnNextChevrolet.addEventListener('click', nextSliderChevrolet)
btnPrevChevrolet.addEventListener('click', prevSliderChevrolet)



//slider Lamborguini
const sliderLamborguini = document.querySelectorAll('.sliderLamborguini');
const btnPrevLamborguini = document.getElementById('prev-buttonLamborguini');
const btnNextLamborguini = document.getElementById('next-buttonLamborguini');


let currentSlidesLamborguini = 0;

function hideSliderLamborguini() {
    sliderLamborguini.forEach(item => item.classList.remove('on'))
}

function showSliderLamborguini() {
    sliderLamborguini[currentSlidesLamborguini].classList.add('on')
}

function nextSliderLamborguini() {
    hideSliderLamborguini()
    if (currentSlidesLamborguini === sliderLamborguini.length - 1) {
        currentSlidesLamborguini = 0
    } else {
        currentSlidesLamborguini++
    }
    showSliderLamborguini()
}

function prevSliderLamborguini() {
    hideSliderLamborguini()
    if (currentSlidesLamborguini === 0) {
        currentSlidesLamborguini = sliderLamborguini.length - 1
    } else {
        currentSlidesLamborguini--
    }
    showSliderLamborguini()
}

btnNextLamborguini.addEventListener('click', nextSliderLamborguini)
btnPrevLamborguini.addEventListener('click', prevSliderLamborguini)



//slider Amarok
const sliderAmarok = document.querySelectorAll('.sliderAmarok');
const btnPrevAmarok = document.getElementById('prev-buttonAmarok');
const btnNextAmarok = document.getElementById('next-buttonAmarok');


let currentSlidesAmarok = 0;

function hideSliderAmarok() {
    sliderAmarok.forEach(item => item.classList.remove('on'))
}

function showSliderAmarok() {
    sliderAmarok[currentSlidesAmarok].classList.add('on')
}

function nextSliderAmarok() {
    hideSliderAmarok()
    if (currentSlidesAmarok === sliderAmarok.length - 1) {
        currentSlidesAmarok = 0
    } else {
        currentSlidesAmarok++
    }
    showSliderAmarok()
}

function prevSliderAmarok() {
    hideSliderAmarok()
    if (currentSlidesAmarok === 0) {
        currentSlidesAmarok = sliderAmarok.length - 1
    } else {
        currentSlidesAmarok--
    }
    showSliderAmarok()
}

btnNextAmarok.addEventListener('click', nextSliderAmarok)
btnPrevAmarok.addEventListener('click', prevSliderAmarok)



//slider Ferrari
const sliderFerrari = document.querySelectorAll('.sliderFerrari');
const btnPrevFerrari = document.getElementById('prev-buttonFerrari');
const btnNextFerrari = document.getElementById('next-buttonFerrari');


let currentSlidesFerrari = 0;

function hideSliderFerrari() {
    sliderFerrari.forEach(item => item.classList.remove('on'))
}

function showSliderFerrari() {
    sliderFerrari[currentSlidesFerrari].classList.add('on')
}

function nextSliderFerrari() {
    hideSliderFerrari()
    if (currentSlidesFerrari === sliderFerrari.length - 1) {
        currentSlidesFerrari = 0
    } else {
        currentSlidesFerrari++
    }
    showSliderFerrari()
}

function prevSliderFerrari() {
    hideSliderFerrari()
    if (currentSlidesFerrari === 0) {
        currentSlidesFerrari = sliderFerrari.length - 1
    } else {
        currentSlidesFerrari--
    }
    showSliderFerrari()
}

btnNextFerrari.addEventListener('click', nextSliderFerrari)
btnPrevFerrari.addEventListener('click', prevSliderFerrari)

//slider panamera

const sliderPanamera = document.querySelectorAll('.sliderPanamera');
const btnPrevPanamera = document.getElementById('prev-buttonPanamera');
const btnNextPanamera = document.getElementById('next-buttonPanamera');


let currentSlidesPanamera = 0;

function hideSliderPanamera() {
    sliderPanamera.forEach(item => item.classList.remove('on'))
}

function showSliderPanamera() {
    sliderPanamera[currentSlidesPanamera].classList.add('on')
}

function nextSliderPanamera() {
    hideSliderPanamera()
    if (currentSlidesPanamera === sliderPanamera.length - 1) {
        currentSlidesPanamera = 0
    } else {
        currentSlidesPanamera++
    }
    showSliderPanamera()
}

function prevSliderPanamera() {
    hideSliderPanamera()
    if (currentSlidesPanamera === 0) {
        currentSlidesPanamera = sliderPanamera.length - 1
    } else {
        currentSlidesPanamera--
    }
    showSliderPanamera()
}

btnNextPanamera.addEventListener('click', nextSliderPanamera)
btnPrevPanamera.addEventListener('click', prevSliderPanamera)



//slider Volkswagen
const sliderVolkswagen = document.querySelectorAll('.sliderVolkswagen');
const btnPrevVolkswagen = document.getElementById('prev-buttonVolkswagen');
const btnNextVolkswagen = document.getElementById('next-buttonVolkswagen');


let currentSlidesVolkswagen = 0;

function hideSliderVolkswagen() {
    sliderVolkswagen.forEach(item => item.classList.remove('on'))
}

function showSliderVolkswagen() {
    sliderVolkswagen[currentSlidesVolkswagen].classList.add('on')
}

function nextSliderVolkswagen() {
    hideSliderVolkswagen()
    if (currentSlidesVolkswagen === sliderVolkswagen.length - 1) {
        currentSlidesVolkswagen = 0
    } else {
        currentSlidesVolkswagen++
    }
    showSliderVolkswagen()
}

function prevSliderVolkswagen() {
    hideSliderVolkswagen()
    if (currentSlidesVolkswagen === 0) {
        currentSlidesVolkswagen = sliderVolkswagen.length - 1
    } else {
        currentSlidesVolkswagen--
    }
    showSliderVolkswagen()
}

btnNextVolkswagen.addEventListener('click', nextSliderVolkswagen)
btnPrevVolkswagen.addEventListener('click', prevSliderVolkswagen)



//slider Chevrolet
const sliderChevrolett = document.querySelectorAll('.sliderChevrolett');
const btnPrevChevrolett = document.getElementById('prev-buttonChevrolett');
const btnNextChevrolett = document.getElementById('next-buttonChevrolett');


let currentSlidesChevrolett = 0;

function hideSliderChevrolett() {
    sliderChevrolett.forEach(item => item.classList.remove('on'))
}

function showSliderChevrolett() {
    sliderChevrolett[currentSlidesChevrolett].classList.add('on')
}

function nextSliderChevrolett() {
    hideSliderChevrolett()
    if (currentSlidesChevrolett === sliderChevrolett.length - 1) {
        currentSlidesChevrolett = 0
    } else {
        currentSlidesChevrolett++
    }
    showSliderChevrolett()
}

function prevSliderChevrolett() {
    hideSliderChevrolett()
    if (currentSlidesChevrolett === 0) {
        currentSlidesChevrolett = sliderChevrolett.length - 1
    } else {
        currentSlidesChevrolett--
    }
    showSliderChevrolett()
}

btnNextChevrolett.addEventListener('click', nextSliderChevrolett)
btnPrevChevrolett.addEventListener('click', prevSliderChevrolett)



//slider tesla1
const slidertesla1 = document.querySelectorAll('.slidertesla1');
const btnPrevtesla1 = document.getElementById('prev-buttontesla1');
const btnNexttesla1 = document.getElementById('next-buttontesla1');


let currentSlidestesla1 = 0;

function hideSlidertesla1() {
    slidertesla1.forEach(item => item.classList.remove('on'))
}

function showSlidertesla1() {
    slidertesla1[currentSlidestesla1].classList.add('on')
}

function nextSlidertesla1() {
    hideSlidertesla1()
    if (currentSlidestesla1 === slidertesla1.length - 1) {
        currentSlidestesla1 = 0
    } else {
        currentSlidestesla1++
    }
    showSlidertesla1()
}

function prevSlidertesla1() {
    hideSlidertesla1()
    if (currentSlidestesla1 === 0) {
        currentSlidestesla1 = slidertesla1.length - 1
    } else {
        currentSlidestesla1--
    }
    showSlidertesla1()
}

btnNexttesla1.addEventListener('click', nextSlidertesla1)
btnPrevtesla1.addEventListener('click', prevSlidertesla1)
