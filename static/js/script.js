$( document ).ready(function() {
    console.log( "jQuery ready!" );
});

var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        message: 'HELLO VUE'
    }
}) 