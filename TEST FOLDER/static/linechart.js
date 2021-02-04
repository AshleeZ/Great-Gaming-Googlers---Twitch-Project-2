d3.json('http://localhost:5000/game').then(function(data) {
    
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
        type: 'bar',
        orientation: 'v'
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
