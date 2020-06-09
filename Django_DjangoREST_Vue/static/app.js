new Vue ({
    el: '#orders_app',
    data: {
        orders: []
    },
    created: function() {
        const VM = this;
        axios.get('/api/orders/')
            .then(function(response){
                VM.orders = response.data
            })
    }
}
)