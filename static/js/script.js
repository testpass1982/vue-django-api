
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
        basket: {},
        loading: false,
        message: 'HELLO VUE',
        currentProduct: {},
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
        getProduct: function(id) {
            this.loading = true;
            this.$http.get(`api/products/${id}`)
            .then( response => {
                this.currentProduct = response.body;
                this.loading = false;
            })
            .catch( err => {
                this.loading = false;
                console.log(err);
            })
        },
        addToBasket: function(product) {
            this.loading = true;
            if (this.basket.basket_id) {
                product.basket_id = this.basket.basket_id;
            } else {
                this.$http.post('/api/baskets/')
                .then( response => {
                    this.basket = response.body;
                    this.loading = false;
                    product.basket_id = this.basket.basket_id;
                })
                .catch( err => {
                    this.loading = false;
                    console.log(err);
            })
            }
        }
    }
});