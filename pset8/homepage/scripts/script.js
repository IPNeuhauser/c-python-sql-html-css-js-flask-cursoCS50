function menu() {
    let menu = document.querySelector('ul#menu');

    if(menu.style.display == 'none'){
        menu.style.display = 'block';
    } else {
        menu.style.display = 'none';
    }
}