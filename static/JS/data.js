const data = {
    labels: ['WestPineLofts', 'Cambridge Woods', 'Oak Ramble Apartments', 'City of Laclede Lofts', 'The Standard Apartments','Eagles Point Apartments', 'The Henry', 'Lakes of North Dale', 'Woodward Lofts', 'Avalon Heights', 'The Henry', 'Willow Brooke Apartments'],
    datasets: [{
      label: 'Percentage of Students Living in Housing Communities of Tampa',
      data: [75, 60, 45, 80, 70, 55, 40, 65, 50, 30, 20, 10],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 205, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)',
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 205, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 205, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 205, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  };  

  const ctx = document.getElementById('myChart').getContext('2d');

  const chart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          ticks: {
            callback: function(value) {
              return value + "%";
            }
          }
        }
      },
      plugins: {
        legend: {
          display: false
        },
        title: {
          display: true,
          text: 'Percentage of Students Living in Different Housing Communities',
          font: {
            size: 25, // adjust font size as needed
            weight: 'bold' // make the title bold
          }
        },
        datalabels: {
          anchor: 'end',
          align: 'top',
          font: {
            weight: 'bold'
          },
          formatter: function(value, context) {
            return value + '%';
          }
        }
      }
    }
  });
  