function populate_categories() {

    var metrics = ['Choose a Metric', 'Average Viewers', 'Time Streamed (hrs)', 'All Time Peak Viewers', 'Hours Watched', 'Overall Rank', 'Followers Gained', 'Total Followers', 'Total Views'];
    var select = d3.select("#select_category");
    metrics.forEach(category => {
        var option = select.append("option");
        option.text(category);
    });
}

populate_categories();

function populate_chart() {

    d3.json('http://localhost:5000/topstreamersdata').then(function(data) {


    var streamers = [];
    var metrics = [];

    Object.entries(data).forEach(([channel,metric]) => {
        streamers.push(channel)
        var target_metric = metric['avg_viewers']
        metrics.push(target_metric)
    });

    var trace = {
        x: metrics,
        y: streamers,
        text: streamers,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: 'rgb(110, 180, 6)'
          }
    };

    var data = [trace];
    var layout = {
        title: {
            text: 'Top Streamers for Game',
            font: {
                size: 24,
                color: 'rgb(82, 46, 238)'
            },
        },
        xaxis: {
            title: {
                text: 'target_metric',
                font: {
                    size: 18,
                    color: 'rgb(82, 46, 238)'
                }
            },
        },
        yaxis: {
            title: {
                text: 'Streamer Name',
                font: {
                    size: 18,
                    color: 'rgb(82, 46, 238)'
                }
            },
        },
        autosize: false,
        width: 1000,
        height: 500,
        margin: {
          l: 150,
          r: 150,
          b: 50,
          t: 50,
          pad: 4
        },
    };
    var chart = d3.selectAll('#chart_group').node();
    Plotly.newPlot(chart, data, layout);

    })
}

populate_chart();

function updatePlotly() {
    
    d3.json('http://localhost:5000/topstreamersdata').then(function(data) {
        var menu = d3.select("#select_category");
        var category = menu.node().value;
        var chart = d3.selectAll('#chart_group').node();
        var target_metric = ''
        switch(category) {
            case 'Average Viewers':
                target_metric = 'avg_viewers';
                break;
            case 'All Time Peak Viewers':
                target_metric = 'all_time_peak_viewers';
                break;
            case 'Hours Watched':
                target_metric = 'hours_watched';
                break;
            case 'Overall Rank':
                target_metric = 'overall_rank';
                break;    
            case 'Followers Gained':
                target_metric = 'followers_gained';
                break;
            case 'Total Followers':
                target_metric = 'total_followers';
                break;
            case 'Total Views':
                target_metric = 'total_views';
                break;
            case 'Time Streamed (hrs)':
                target_metric = 'time_streamed(hrs)';
                break;
            default:
                target_metric = 'avg_viewers';
        }    

        var streamers = [];
        var metrics = [];
    
        Object.entries(data).forEach(([channel,metric]) => {
            streamers.push(channel)
            var target = metric[target_metric]
            metrics.push(target)
        });
    
        Plotly.restyle(chart, "x", [metrics])
        Plotly.restyle(chart, "y", [streamers])        
    })
}

d3.select("#select_category").on("change", updatePlotly);