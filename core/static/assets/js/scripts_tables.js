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

        const editStoreButtons = document.querySelectorAll('#editStoreButt');
        let globalStoreId = 0
        const form = document.querySelector('#editStoreForm');

        editStoreButtons.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const storeId = button.getAttribute('data-value');
                console.log(storeId)
                globalStoreId = storeId
                console.log(globalStoreId)
                const url = `/edit_store/${storeId}/`; // url creating
                console.log(url)
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        console.log('Received data from Django:', data);
                        
                        // fill the form fields
                        form.store_name.value = data.form_data.store_name;
                        form.phone.value = data.form_data.phone;
                        form.email.value = data.form_data.email;
                        form.street.value = data.form_data.street;
                        form.city.value = data.form_data.city;
                        form.state.value = data.form_data.state;
                        form.zip_code.value = data.form_data.zip_code;
                    })
                    .catch(error => {
                        console.error('Error fetching data from Django:', error);
                    });
            });
        });

    if (window.location.pathname === 'http://127.0.0.1:8000/stores_table/') {
        var submitStoreEdit = document.querySelector('#submitStoreEdit');

        submitStoreEdit.addEventListener('click', function (event) {
            event.preventDefault();
            storeId = globalStoreId
            console.log(storeId)

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
    
    
        //taking record id from dropdownlink
        const global = document.querySelectorAll('#dropdownLink');
        let globalId = 0
        global.forEach(button => {
            button.addEventListener('click', function (event) {
                event.preventDefault();
                const storeId = button.getAttribute('data-value');
                globalId = storeId
                console.log(globalId)
            });
        })

        const submitDelete = document.querySelector('#submitDelete');
        submitDelete.addEventListener('click', function (event) {
            //event.preventDefault();
            storeId = globalId
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
//=======================Staffs===================================

    const editStaffButtons = document.querySelectorAll('#editStaffButt');
    let globalStaffId = 0
    const Staffform = document.querySelector('#editStaffForm');
    editStaffButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const staffId = button.getAttribute('data-value');
            console.log(staffId)
            globalStaffId = staffId
            console.log(globalStaffId)
            const url = `/edit_staff/${staffId}/`; // url creating
            console.log(url)
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log('Received data from Django:', data);
                    
                    // fill the form fields
                    Staffform.first_name.value = data.form_data.first_name;
                    Staffform.last_name.value = data.form_data.last_name;
                    Staffform.email.value = data.form_data.email;
                    Staffform.phone.value = data.form_data.phone;
                    Staffform.active.value = data.form_data.active;
                    Staffform.store.value = data.form_data.store;
                    Staffform.manager.value = data.form_data.manager;
                })
                .catch(error => {
                    console.error('Error fetching data from Django:', error);
                });
        }); 
    });

    //if (window.location.pathname === 'http://127.0.0.1:8000/staffs_table/') {
        var SubmitStaffEdit = document.querySelector('#SubmitStaffEdit');

        SubmitStaffEdit.addEventListener('click', function (event) {
            event.preventDefault();
            staffId = globalStaffId
            console.log(staffId)

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
                    const form = document.querySelector('#editStaffForm'); // find form on page
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
    //}





























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
