
function filter() {
    var input,
        filter,
        filterAcentom,
        ul,
        li,
        a,
        i,
        span,
        txtValue,
        count = 0

    input = document.getElementById('busca-cidade');
    ul = document.getElementById('lista-nao-ordenada');
    filter = input.value.toLocaleLowerCase();
    filterAcentom = filter.normalize('NFD').replace(/[\u0300-\u036f]/g, "");


    li = ul.getElementsByTagName("li");
    const lis = document.querySelector('#locali')

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByClassName("localizacao")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toLocaleLowerCase().indexOf(filterAcentom) > -1) {
            li[i].style.display = "";
            count++
            span = li[i].querySelector("#city");
            if (span) {
                span.innerHTML = txtValue.replace(new RegExp(filterAcentom, "gi"), (match) => {
                    return "<strong>" + match + "</strong>";
                })
            }

        } else {
            li[i].style.display = "none";
        }
    }

    if (count == 0) {
        ul.style.display = "none";
        lis.innerHTML = "Nenhum carro encontrado nessa localização"
    }if(count == 12){
        lis.innerHTML = ""
    }else {
        ul.style.display = "grid";
        lis.innerHTML = count + ' veiculos foram encontrados'
    }
}