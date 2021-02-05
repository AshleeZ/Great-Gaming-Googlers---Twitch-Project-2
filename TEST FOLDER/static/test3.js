d3.json('http://localhost:5000/test3').then(function(data) {
    
    var streamers = [];
    var total_views = [];
    Object.entries(data).forEach(([channel,metric]) => {
        streamers.push(channel)
        var target_metric = metric['total_views']
        total_views.push(target_metric)
    });

    console.log(streamers)
    console.log(total_views)

    var trace = {
        x: total_views,
        y: streamers,
        text: streamers,
        type: 'bar',
        orientation: 'h'
    };

    var data = [trace];
    var layout = {
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
    var chart = d3.selectAll('#bar').node();
    Plotly.newPlot(chart, data, layout);
})
