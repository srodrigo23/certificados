const currentUrl = window.location.href;
var pathname = new URL(currentUrl).pathname;
const route = pathname.substring(1, pathname.length-1)

const routes = ['courses', 'certificates', 'users']
for (let i = 0; i < routes.length; i++) {
    if (routes[i]=== route){
        $(`#${routes[i]}`).toggleClass("active", true)    
    }else{
        $(`#${routes[i]}`).toggleClass("active", false)    
    }
}


function message(){
    console.log('this is a message')
}