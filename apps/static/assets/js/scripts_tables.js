window.addEventListener('DOMContentLoaded', event => {

    const customersTable = document.body.querySelector('#customersTable');
    if (customersTable) {
        $(document).ready(function() {
            $('#customersTable').DataTable({
                ajax: {
                    url: 'jsonresponse/customers',
                    dataSrc: ''
                },
                columns: [
                    { data: 'first_name' },
                    { data: 'last_name' },
                    { data: 'phone' },
                    { data: 'email' },
                    { data: 'street' },
                    { data: 'city' },
                    { data: 'state' },
                    { data: 'zip_code' }
                ]
            });
        });
    }

    const storesTable = document.body.querySelector('#storesTable');
    if (storesTable) {
        $(document).ready(function() {
            $('#storesTable').DataTable({
                ajax: {
                    url: 'jsonresponse/stores',
                    dataSrc: ''
                },
                columns: [
                    { data: 'store_id' },
                    { data: 'store_name' },
                    { data: 'phone' },
                    { data: 'email' },
                    { data: 'street' },
                    { data: 'city' },
                    { data: 'state' },
                    { data: 'zip_code' }
                ]
            });
        });
    }

    const orderItemsTable = document.body.querySelector('#orderItemsTable');
    if (orderItemsTable) {
        $(document).ready(function() {
            $('#orderItemsTable').DataTable({
                ajax: {
                    url: 'jsonresponse/order_items',
                    dataSrc: ''
                },
                columns: [
                    { data: 'order' },
                    { data: 'item_id' },
                    { data: 'product' },
                    { data: 'quantity' },
                    { data: 'list_price' },
                    { data: 'discount' },
                ]
            });
        });
    }

});
