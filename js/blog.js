document.addEventListener("DOMContentLoaded",function(event){

    console.log("this is blog.js")
    let sc=document.createElement('script')
    sc.setAttribute('src','https://cdn.tiny.cloud/1/48ff710z3czitop1rjs27yj79oc3992d6uswqiicmcql0l94/tinymce/7/tinymce.min.js'),
    document.head.appendChild(sc);
sc.onload=()=>{

    tinymce.init({
        selector:'#id_content'
    });
}
})