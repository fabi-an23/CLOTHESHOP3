

let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")


menu.addEventListener("click", function() {
    
    if(header.style.height == "80px" || header.offsetHeight == 80){
        header.style.height = 80 + nav.offsetHeight + "px"
    } else {
        header.style.height = "80px"
    }
    
})

window.addEventListener("resize", function(){
    let ancho = this.document.documentElement.clientWidth

    if(ancho > 480) {
        header.style = ""
    }

})