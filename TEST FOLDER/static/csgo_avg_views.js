d3.json('http://localhost:5000/csgo').then(function(data) {
    
    var dates = [];
    var avg_viewers = [];
    Object.entries(data).forEach(([index,metric]) => {
        dates.push(index)
        avg_viewers.push(metric[0])
        console.log(metric)
        console.log(index)
    });

    // console.log(dates)
    // console.log(avg_viewers)

    var trace = {
        x: dates,
        y: avg_viewers,
        marker: {color: '#6441A4'},
        type: 'scatter',
        orientation: 'v'
    };

    var data = [trace];
    var layout = {
        title: {
            text: 'Counter Strike Global Offensive Average Viewers',
            font: {
                family: 'sans serif', 
                size: 24,
                color: '#6441A4'
            },
        },
        xaxis: {
            title: {
                text: 'Date',
                font: {
                    family: 'sans serif',
                    size: 18,
                    color: '#6441A4'
                }
            },
        },
        yaxis: {
            title: {
                text: 'Viewers (k)',
                font: {
                    family: 'sans serif',
                    size: 18,
                    color: '#6441A4'
                }
            },
        },
        autosize: false,
        width: 1000,
        height: 500,
        margin: {
          l: 200,
          r: 50,
          b: 100,
          t: 100,
          pad: 4
        },
    };
    
    var chart = d3.selectAll('#csgo_avg_views').node();
    Plotly.newPlot(chart, data, layout);
})
