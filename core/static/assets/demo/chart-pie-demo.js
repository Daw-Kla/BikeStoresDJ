// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var chartData = JSON.parse(document.getElementById("myBarChart").getAttribute('data-chart-data'));
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: chartData.brands,
    datasets: [{
      data: chartData.total_brands_sales,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#6610f2', '#ff6c23', '#6f42c1', '#fd7e14', '#17a2b8', '#e83e8c'],
    }],
  },
});
