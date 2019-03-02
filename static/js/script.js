
$(document).ready(function () {
    console.log("jQuery ready!");
});

Vue.use(VueResource)

var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        products: [],
        photos: [],
        baskets: [],
        loading: false,
        message: 'HELLO VUE',
        currentProduct: {},
        newProduct: {
            'product_name': null,
            'product_description': null,
        },
        // http: {
        //     root: '/root',
        //     headers: {
        //       Authorization: 'Basic YXBpOnBhc3N3b3Jk'
        //     }
        //   }
    },
    mounted: function () {
        this.getProducts();
    },
    methods: {
        getProducts: function () {
            this.loading = true;
            this.$http.get('/api/products/')
                .then( response => {
                    this.products = response.body;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getProduct: function() {
            this.loading = true;
            this.$http.get('api/products/${id}')
            .then( response => {
                this.currentProduct = response.body;
                this.loading = false;
            })
            .catch( err => {
                this.loading = false;
                console.log(err);
            })
        }
    }
});