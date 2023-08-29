/*!
    * Start Bootstrap - SB Admin v7.0.0 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2021 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    /*const editButtons = document.querySelectorAll('.edit-button');
    const modal = new bootstrap.Modal(document.getElementById('editStore'));

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const row = button.closest('tr');
            const storeId = row.getAttribute('data-store-id');

            // Wysłanie żądania AJAX, aby pobrać dane rekordu
            fetch(`/get_store_data/${storeId}/`)
                .then(response => response.json())
                .then(data => {
                    // Wypełnianie pól formularza danymi zwróconymi przez żądanie
                    document.querySelector('#store_id').value = data.id;
                    document.querySelector('#store_name').value = data.store_name;
                    document.querySelector('#phone').value = data.phone;
                    document.querySelector('#email').value = data.email;
                    document.querySelector('#street').value = data.street;
                    document.querySelector('#city').value = data.city;
                    document.querySelector('#state').value = data.state;
                    document.querySelector('#zip_code').value = data.zip_code;

                    // Otwarcie modala przy użyciu Bootstrap
                    //modal.show();
                })
                .catch(error => {
                    console.error('Error fetching store data:', error);
                });
        });
    });*/

});
