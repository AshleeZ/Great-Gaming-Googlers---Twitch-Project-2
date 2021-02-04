d3.json('http://localhost:5000/test').then(function(data) {
    
    var streamers = [];
    var avg_viewers = [];
    Object.entries(data).forEach(([channel,metric]) => {
        streamers.push(channel)
        var target_metric = metric['avg_viewers']
        avg_viewers.push(target_metric)
    });

    console.log(streamers)
    console.log(avg_viewers)

    var trace = {
        x: avg_viewers,
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
