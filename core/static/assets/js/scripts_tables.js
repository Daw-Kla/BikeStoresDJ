window.addEventListener('DOMContentLoaded', event => {
    
    //table handle
    $(document).ready(function(){
        $('table.display').DataTable({
            dom: 'Bftrip',
            buttons: [],
            order: [[0, 'asc']],
            pageLength: 50
        });

    });

    //function for refreshing table after edit
    function refreshTable(table_name, table_url) {
        const tableRows = document.querySelectorAll(table_name + ' tbody tr'); // finding all table rows
        const url = table_url; // url for get actual data
        fetch(url)
            .then(response => response.json())
            .then(data => {
                // iteration throung table rowas and updating cell values
                tableRows.forEach((row, rowIndex) => {
                    const item = data[rowIndex];
                    const cells = row.querySelectorAll('td');
    
                    for (let i = 0; i < cells.length - 1; i++) {
                        cells[i].textContent = item[i];
                    }
                });
            })
            .catch(error => {
                console.error('Error refreshing table:', error);
            });
    }

    //fcn that takes a coockie from a session
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Find cookie with csrf token
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

//=======================Stores page===================================
    //editing a store record
    const editStoreButtons = document.querySelectorAll('#editStoreButt');
    const Storeform = document.querySelector('#editStoreForm');
    let globalStoreId = 0
    if ( editStoreButtons && Storeform){
        editStoreButtons.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const storeId = button.getAttribute('data-value');
                globalStoreId = storeId
                const url = `/edit_store/${storeId}/`; // url creating
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        console.log('Received data from Django:', data);
                        
                        // fill the form fields
                        Storeform.store_name.value = data.form_data.store_name;
                        Storeform.phone.value = data.form_data.phone;
                        Storeform.email.value = data.form_data.email;
                        Storeform.street.value = data.form_data.street;
                        Storeform.city.value = data.form_data.city;
                        Storeform.state.value = data.form_data.state;
                        Storeform.zip_code.value = data.form_data.zip_code;
                    })
                    .catch(error => {
                        console.error('Error fetching data from Django:', error);
                    });
            });
        });
    }

    //submit store edition
    var submitStoreEdit = document.querySelector('#submitStoreEdit');
    if (submitStoreEdit){
        submitStoreEdit.addEventListener('click', function (event) {
            event.preventDefault();
            storeId = globalStoreId

            const form = document.querySelector('#editStoreForm');
            const formData = new FormData(form);
            const updateUrl = `http://127.0.0.1:8000/edit_store/${storeId}/`;

            fetch(updateUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // success handling
                    console.log('Record updated successfully');
                    const form = document.querySelector('#editStoreForm'); // find form on page
                    refreshTable('#storesTable', '/get_stores_data/')
                } else {
                    //errors handling
                    console.error('Error updating record:', data.errors);
                }
            })
            .catch(error => {
                console.error('Error updating record:', error);
            });
        });
    }

    //taking record id from dropdownlink
    const dropdownStore = document.querySelectorAll('#dropdownStore');
    if (dropdownStore){
        dropdownStore.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const storeId = button.getAttribute('data-value');
                globalStoreId = storeId
            });
        })
    }

    //store record delete
    const submitStoreDelete = document.querySelector('#submitStoreDelete');
    if (submitStoreDelete){
        submitStoreDelete.addEventListener('click', function (event) {
            //event.preventDefault();
            storeId = globalStoreId
            const updateUrl = `/delete_store/${storeId}/`;
            const csrftoken = getCookie('csrftoken'); // Download csrf token
            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => {
                if (response.ok) {
                    // refresh whole page
                    location.reload()
                } else {
                    console.error('There was a mistake during deleting a record');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

//=======================Staffs page===================================

    //editing Staffs record
    const editStaffButtons = document.querySelectorAll('#editStaffButt');
    const Stafform = document.querySelector('#editStaffForm');
    if (editStaffButtons && Stafform){
        let globalStaffId = 0
        editStaffButtons.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const staffId = button.getAttribute('data-value');
                globalStaffId = staffId
                const url = `/edit_staff/${staffId}/`; // url creating
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        console.log('Received data from Django:', data);
                        
                        // fill the form fields
                        Stafform.first_name.value = data.form_data.first_name;
                        Stafform.last_name.value = data.form_data.last_name;
                        Stafform.email.value = data.form_data.email;
                        Stafform.phone.value = data.form_data.phone;
                        Stafform.active.value = data.form_data.active;
                        Stafform.store.value = data.form_data.store;
                        Stafform.manager.value = data.form_data.manager;
                    })
                    .catch(error => {
                        console.error('Error fetching data from Django:', error);
                    });
            }); 
        });
    }

    //submit staff edit
    var SubmitStaffEdit = document.querySelector('#SubmitStaffEdit');
    if (SubmitStaffEdit){
        SubmitStaffEdit.addEventListener('click', function (event) {
            event.preventDefault();
            staffId = globalStaffId

            const form = document.querySelector('#editStaffForm');
            const formData = new FormData(form);
            const updateUrl = `http://127.0.0.1:8000/edit_staff/${staffId}/`;

            fetch(updateUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // success handling
                    console.log('Record updated successfully');
                    refreshTable('#staffsTable', '/get_staffs_data/')
                } else {
                    //errors handling
                    console.error('Error updating record:', data.errors);
                }
            })
            .catch(error => {
                console.error('Error updating record:', error);
            });
        });
    }

    const dropdownStaffs = document.querySelectorAll('#dropdownStaffs');
    if (dropdownStaffs){
        dropdownStaffs.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const staffId = button.getAttribute('data-value');
                globalStaffId = staffId
            });
        });
    }

    //delete staff record
    const submitStaffDelete = document.querySelector('#submitStaffDelete');
    if (submitStaffDelete){
        submitStaffDelete.addEventListener('click', function (event) {
            staffId = globalStaffId
            const updateUrl = `/delete_staff/${staffId}/`;
            const csrftoken = getCookie('csrftoken'); // Download csrf token
            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => {
                if (response.ok) {
                    // refresh whole page
                    location.reload()
                } else {
                    console.error('There was a mistake during deleting a record');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

//=======================Customers page===================================

    //editing Customers record
    const editCustomerButtons = document.querySelectorAll('#editCustomerButt');
    const Customerform = document.querySelector('#editCustomerForm');
    if (editCustomerButtons && Customerform){
        let globalCustId = 0
        editCustomerButtons.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const CustomerId = button.getAttribute('data-value');
                globalCustId = CustomerId
                const url = `/edit_customer/${CustomerId}/`; // url creating
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        console.log('Received data from Django:', data);
                        
                        // fill the form fields
                        Customerform.first_name.value = data.form_data.first_name;
                        Customerform.last_name.value = data.form_data.last_name;
                        Customerform.phone.value = data.form_data.phone;
                        Customerform.email.value = data.form_data.email;
                        Customerform.street.value = data.form_data.street;
                        Customerform.city.value = data.form_data.city;
                        Customerform.state.value = data.form_data.state;
                        Customerform.zip_code.value = data.form_data.zip_code;
                    })
                    .catch(error => {
                        console.error('Error fetching data from Django:', error);
                    });
            }); 
        });
    }

    //submit customer edit 
    var submitCustomerEdit = document.querySelector('#submitCustomerEdit');
    if (submitCustomerEdit){
        submitCustomerEdit.addEventListener('click', function (event) {
            event.preventDefault();
            CustomerId = globalCustId

            const form = document.querySelector('#editCustomerForm');
            const formData = new FormData(form);
            const updateUrl = `http://127.0.0.1:8000/edit_customer/${CustomerId}/`;

            fetch(updateUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // success handling - works bad for big table volumes
                    console.log('Record updated successfully');
                    //refreshTable('#customersTable', '/get_customers_data/')\      //works bad for table witch sorted rows by values
                    location.reload()
                } else {
                    //errors handling
                    console.error('Error updating record:', data.errors);
                }
            })
            .catch(error => {
                console.error('Error updating record:', error);
            });
        });
    }

    const dropdownCustomer = document.querySelectorAll('#dropdownCustomer');
    if (dropdownCustomer){
        dropdownCustomer.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const CustomerId = button.getAttribute('data-value');
                globalCustId = CustomerId
            });
        });
    }

    //delete Customer record
    const submitCustomerDelete = document.querySelector('#submitCustomerDelete');
    if (submitCustomerDelete){
        submitCustomerDelete.addEventListener('click', function (event) {
            CustomerId = globalCustId
            const updateUrl = `/delete_customer/${CustomerId}/`;
            const csrftoken = getCookie('csrftoken'); // Download csrf token
            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => {
                if (response.ok) {
                    // refresh whole page
                    location.reload()
                } else {
                    console.error('There was a mistake during deleting a record');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

//=======================Orders page===================================

    //editing order record
    const editOrderButt = document.querySelectorAll('#editOrderButt');
    const Orderform = document.querySelector('#editOrderForm');
    if (editOrderButt && Orderform){
        editOrderButt.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const OrderId = button.getAttribute('data-value');
                globalOrdId = OrderId
                const url = `/edit_order/${OrderId}/`; // url creating
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        console.log('Received data from Django:', data);
                        
                        // fill the form fields -doesnt work for customer, store and staff fields - FK
                        Orderform.customer.value = data.form_data.customer;
                        Orderform.order_status.value = data.form_data.order_status;
                        Orderform.order_date.value = data.form_data.order_date;
                        Orderform.shipped_date.value = data.form_data.shipped_date;
                        Orderform.required_date.value = data.form_data.required_date;
                        Orderform.store.value = data.form_data.store;
                        Orderform.staff.value = data.form_data.staff;
                    })
                    .catch(error => {
                        console.error('Error fetching data from Django:', error);
                    });
            }); 
        });
    }

    //submit order edit 
    var submitOrderEdit = document.querySelector('#submitOrderEdit');
    if (submitOrderEdit){
        submitOrderEdit.addEventListener('click', function (event) {
            event.preventDefault();
            OrderId = globalOrdId

            const form = document.querySelector('#editOrderForm');
            const formData = new FormData(form);
            const updateUrl = `http://127.0.0.1:8000/edit_order/${OrderId}/`;

            fetch(updateUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Record updated successfully');
                    location.reload()
                } else {
                    console.error('Error updating record:', data.errors);
                }
            })
            .catch(error => {
                console.error('Error updating record:', error);
            });
        });
    }

    const dropdownOrder = document.querySelectorAll('#dropdownOrder');
    if (dropdownOrder){
        dropdownOrder.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const OrderId = button.getAttribute('data-value');
                globalOrdId = OrderId
            });
        });
    }

    //delete order record
    const submitOrderDelete = document.querySelector('#submitOrderDelete');
    if (submitOrderDelete){
        submitOrderDelete.addEventListener('click', function (event) {
            OrderId = globalOrdId
            const updateUrl = `/delete_order/${OrderId}/`;
            const csrftoken = getCookie('csrftoken'); // Download csrf token
            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => {
                if (response.ok) {
                    // refresh whole page
                    location.reload()
                } else {
                    console.error('There was a mistake during deleting a record');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }





    //big tables rendering
    /*$(document).ready(function() {
        let dataTable = $('#ordersTable').DataTable({
            dom: 'Bftrip',
            buttons: [],
            order: [[0, 'asc']],
            pageLength: 50
        });

        ordersTable.on('page.dt', function () {
            const currentPage = ordersTable.page.info().page;
            $.ajax({
                url: `/load_page_orders/${currentPage + 1}/`,
                method: 'GET',
                success: function(response) {
                    ordersTable.clear();
                    ordersTable.rows.add(response).draw();
                },
                error: function(error) {
                    console.error('Error loading page:', error);
                }
            });
        });
    });*/


});
