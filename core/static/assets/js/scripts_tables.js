window.addEventListener('DOMContentLoaded', event => {
    
    $(document).ready(function(){
        $('table.display').DataTable({
            dom: 'Bftrip',
            buttons: [],
            order: [[0, 'asc']],
            pageLength: 50
        });

    });


    const editButtons = document.querySelectorAll('#editButt');

editButtons.forEach(button => {

    button.addEventListener('click', function (event) {
        event.preventDefault();

        const storeId = button.getAttribute('data-value'); // Tu używamy data-value
        const url = `/edit_store/${storeId}/`; // Tworzymy URL

        // Wysłanie żądania AJAX do Django
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Received data from Django:', data);
                
                // Wypełnij pola formularza
                const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu
                form.store_name.value = data.form_data.store_name;
                form.phone.value = data.form_data.phone;
                form.email.value = data.form_data.email;
                form.street.value = data.form_data.street;
                form.city.value = data.form_data.city;
                form.state.value = data.form_data.state;
                form.zip_code.value = data.form_data.zip_code;

                // Wyświetl modal
                const modal = new bootstrap.Modal(document.getElementById('editStore'));
                modal.show();
            })
            .catch(error => {
                console.error('Error fetching data from Django:', error);
            });
    });
});
const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const button = document.querySelectorAll('#editButt');
    const formData = new FormData(form);
    const storeId = button.getAttribute('data-value'); // Tu używamy data-value
    const updateUrl = `/edit_store/${storeId}/`;

    fetch(updateUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Record updated successfully');
            // Tutaj możesz obsłużyć sukces, np. zamknąć modal lub wyświetlić komunikat
        } else {
            console.error('Error updating record:', data.errors);
            // Tutaj możesz obsłużyć błędy, np. wyświetlić komunikat z błędami
        }
    })
    .catch(error => {
        console.error('Error updating record:', error);
    });
});

    /*$(document).ready(function() {
        let dataTable = $('#ordersTable').DataTable({
            dom: 'Bftrip',
            buttons: [],
            order: [[0, 'asc']],
            pageLength: 50
        });

        ordersTable.on('page.dt', function () {
            const currentPage = ordersTable.page.info().page;
            // Wysyłasz zapytanie AJAX, aby pobrać dane dla danej strony
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
