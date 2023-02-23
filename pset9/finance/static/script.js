function olhoLogin(){
    visibilidade = document.querySelector("span.material-symbols-outlined");
    texto = visibilidade.innerHTML.trim()

    if (texto == 'visibility'){
        senha = document.querySelector('input.password')
        senha.type = 'password'

        visibilidade.innerHTML = 'visibility_off'
    } else {
        senha = document.querySelector('input.password')
        senha.type = 'text'
        visibilidade.innerHTML = 'visibility'
    }
}

function olhoRegister(){
    visibilidade = document.querySelector("span.material-symbols-outlined");
    texto = visibilidade.innerHTML.trim()

    if (texto == 'visibility'){
        senha = document.querySelector('input.password')
        check = document.querySelector('input.check')
        senha.type = 'password'
        check.type = 'password'

        visibilidade.innerHTML = 'visibility_off'
    } else {
        senha = document.querySelector('input.password')
        check = document.querySelector('input.check')
        senha.type = 'text'
        check.type = 'text'

        visibilidade.innerHTML = 'visibility'
    }
}