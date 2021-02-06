d3.json('http://localhost:5000/test').then(function(data) {
    
    var streamers = [];
    var followers = [];
    Object.entries(data).forEach(([channel,metric]) => {
        streamers.push(channel)
        var target_metric = metric['total_followers']
        followers.push(target_metric)
    });

    console.log(streamers)
    console.log(followers)

   
    var trace = {
        x: followers,
        y: streamers,
        text: streamers,
        marker: {color: '#6441A4'},
        type: 'bar',
        orientation: 'h'
    };

    var data = [trace];
    var layout = {
        title: {
            text: 'Total Followers by Top Streamers',
            font: {
                family: 'sans serif', 
                size: 24,
                color: '#6441A4'
            },
        },
        xaxis: {
            title: {
                text: 'Number of Followers',
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
    var chart = d3.selectAll('#followers_bar').node();
    Plotly.newPlot(chart, data, layout);
})