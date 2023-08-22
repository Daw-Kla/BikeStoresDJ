window.addEventListener('DOMContentLoaded', event => {
    const csrftoken = Cookies.get('csrftoken');

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

        var exampleModal = document.getElementById("exampleModal");

        // Nasłuchuj zdarzenia show.bs.modal
        exampleModal.addEventListener("show.bs.modal", function () {
        // Znajdź przycisk "Add"
        var addStoreBtn = exampleModal.querySelector("#addStoreBtn");
        //if (addStoreBtn) {
        
            addStoreBtn.addEventListener('click', function () {
            //var recipient = addButton.getAttribute('data-bs-whatever');
            var storeId = document.querySelector("input[name='store_id']").value;
            var storeName = document.querySelector("input[name='store_name']").value;
            var phone = document.querySelector("input[name='phone']").value;
            var email = document.querySelector("input[name='email']").value;
            var street = document.querySelector("input[name='street']").value;
            var city = document.querySelector("input[name='city']").value;
            var state = document.querySelector("input[name='state']").value;
            var zip_code = document.querySelector("input[name='zip_code']").value;

            var data = {
                'store_id': storeId,
                'store_name': storeName,
                'phone': phone,
                'email': email,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                //"csrfmiddlewaretoken" : csrftoken           //to moze dac do ajaxa
            };
            
            $.ajax({
                type: 'POST',
                url: '/jsonresponse/stores',
                data: data,
                
                
                success: function (response) {
                    // Tutaj możesz obsłużyć odpowiedź z serwera
                    // np. odświeżając tabelę z danymi
                    console.log(data)
                },
                error: function (error) {
                    // Tutaj możesz obsłużyć błąd w przypadku niepowodzenia
                    console.log('not ok')
                }
            })
        }); })
    }
    //}

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
                    { data: 'product__product_name' },
                    { data: 'quantity' },
                    { data: 'list_price' },
                    { data: 'discount' },
                ]
            });
        });
    }

    const ordersTable = document.body.querySelector('#ordersTable');
    if (ordersTable) {
        $(document).ready(function() {
            $('#ordersTable').DataTable({
                ajax: {
                    url: 'jsonresponse/orders',
                    dataSrc: ''
                },
                columns: [
                    { data: 'order_id' },
                    { data: 'customer' },
                    { data: 'order_status' },
                    { data: 'order_date' },
                    { data: 'store__store_name' },
                    {
                        data: null,
                        render: function(data, type, row) {
                            if (row.staff__first_name && row.staff__last_name) {
                                return row.staff__first_name + ' ' + row.staff__last_name;
                            } else {
                                return '';
                            }
                        }
                    },
                ]
            });
        });
    }

    const staffsTable = document.body.querySelector('#staffsTable');
    if (staffsTable) {
        $(document).ready(function() {
            $('#staffsTable').DataTable({
                ajax: {
                    url: 'jsonresponse/staffs',
                    dataSrc: ''
                },
                columns: [
                    { data: 'staff_id' },
                    { data: 'first_name' },
                    { data: 'last_name' },
                    { data: 'email' },
                    { data: 'phone' },
                    { data: 'active' },
                    { data: 'store__store_name' },
                    {
                        data: null,
                        render: function(data, type, row) {
                            if (row.manager__first_name && row.manager__last_name) {
                                return row.manager__first_name + ' ' + row.manager__last_name;
                            } else {
                                return '';
                            }
                        }
                    },
                ]
            });
        });
    }

});
