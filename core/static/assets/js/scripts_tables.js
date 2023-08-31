window.addEventListener('DOMContentLoaded', event => {
    
    $(document).ready(function(){
        $('table.display').DataTable({
            dom: 'Bftrip',
            buttons: [],
            order: [[0, 'asc']],
            pageLength: 50
        });

    });
//działa odświeżanie, nie działa zamykanie modalu
    function refreshTable() {
        const tableRows = document.querySelectorAll('#storesTable tbody tr'); // Znajdź wszystkie wiersze tabeli
        const url = '/get_stores_data/'; // Adres URL do pobrania najnowszych danych
    
        // Wysłanie żądania AJAX do pobrania danych
        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Iteruj przez wiersze tabeli i aktualizuj komórki
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
const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu

editButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        const storeId = button.getAttribute('data-value'); // Tu używamy data-value
        console.log(storeId)
        globalStoreId = storeId
        const url = `/edit_store/${storeId}/`; // Tworzymy URL
        console.log(url)
        // Wysłanie żądania AJAX do Django
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Received data from Django:', data);
                
                // Wypełnij pola formularza
                //const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu
                form.store_name.value = data.form_data.store_name;
                form.phone.value = data.form_data.phone;
                form.email.value = data.form_data.email;
                form.street.value = data.form_data.street;
                form.city.value = data.form_data.city;
                form.state.value = data.form_data.state;
                form.zip_code.value = data.form_data.zip_code;

                // Wyświetl modal
                //const modal = new bootstrap.Modal(document.getElementById('editStore'));
                //modal.show();
            })
            .catch(error => {
                console.error('Error fetching data from Django:', error);
            });
    });
});

const submitButton = document.querySelector('#SubmitEdit');

console.log(submitButton)
submitButton.addEventListener('click', function (event) {
    console.log(submitButton)
    event.preventDefault();
    console.log('in')
    //const storeId = submitButton.getAttribute('data-value'); // Pobierz store_id z przycisku
    storeId = globalStoreId
    console.log(storeId)

    const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu

    const formData = new FormData(form);
    const updateUrl = `http://127.0.0.1:8000/edit_store/${storeId}/`;

    fetch(updateUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Record updated successfully');
            // Tutaj możesz obsłużyć sukces, np. zamknąć modal lub wyświetlić komunikat
            //const form = document.querySelector('#editStoreForm'); // Znajdź formularz w modalu
            refreshTable()
            //const modal = new bootstrap.Modal(document.getElementById('editStore'));
            //modal.hide();
            //modal.remove();
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
