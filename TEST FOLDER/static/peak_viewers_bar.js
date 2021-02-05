d3.json('http://localhost:5000/test').then(function(data) {
    
    var streamers = [];
    var peak_viewers = [];
    Object.entries(data).forEach(([channel,metric]) => {
        streamers.push(channel)
        var target_metric = metric['all_time_peak_viewers']
        peak_viewers.push(target_metric)
    });

    console.log(streamers)
    console.log(peak_viewers)

   
    var trace = {
        x: peak_viewers,
        y: streamers,
        text: streamers,
        marker: {color: '#6441A4'},
        type: 'bar',
        orientation: 'h'
    };

    var data = [trace];
    var layout = {
        title: {
            text: 'All-Time Peak Viewers of Top Streamers',
            font: {
                family: 'sans serif', 
                size: 24,
                color: '#6441A4'
            },
        },
        xaxis: {
            title: {
                text: 'All-Time hours peaked',
                font: {
                    family: 'sans serif',
                    size: 18,
                    color: '#6441A4'
                }
            },
        },
        yaxis: {
            title: {
                text: 'Top Streamers',
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
    var chart = d3.selectAll('#peak_viewers_bar').node();
    Plotly.newPlot(chart, data, layout);
})

