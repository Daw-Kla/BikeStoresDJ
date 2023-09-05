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

    function refreshTable() {
        const tableRows = document.querySelectorAll('#storesTable tbody tr'); // finding all table rows
        const url = '/get_stores_data/'; // url for get actual data
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
     

    const editButtons = document.querySelectorAll('#editButt');
    let globalStoreId = 0
    const form = document.querySelector('#editStoreForm');

    editButtons.forEach(button => {
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

    const submitEdit = document.querySelector('#SubmitEdit');

    submitEdit.addEventListener('click', function (event) {
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
                refreshTable()
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
