function populate_categories() {

    var categories = ['Choose a Category','MOBA','Shooting','Strategy'];
    var select = d3.select("#select_category");
    categories.forEach(category => {
        var option = select.append("option");
        option.text(category);
    });
}

populate_categories();

function populate_games() {

    var menu = d3.select("#select_category");
    var category = menu.node().value;

    switch(category) {
        case 'MOBA':
            var games = ['League of Legends','DOTA2','Smite'];
            break;
        case 'Shooting':
            var games = ['Fortnite','Call of Duty','CSGO'];
            break;
        case 'Strategy':
            var games = ['Chess','Among Us', 'Hearthstone'];
            break;
        default:
            var games = []
    }

    var games_list = d3.select("#games");
    games_list.html("");
    games.forEach(game => {
        var item = games_list.append('li').append('a').attr('href', '/games/'+game).text(game)
    })
}

d3.select("#select_category").on("change", populate_games);

function populate_chart() {

    d3.json('http://localhost:5000/targetgamedata').then(function(data) {
        
        var streamers = [];
        var viewers = [];
        var game_name = d3.select('#game_name').text()

        Object.entries(data).forEach(([channel,metric]) => {
            streamers.push(channel)
            var target_metric = metric['Viewers']
            viewers.push(target_metric)
        });
    
        var trace = {
            x: viewers,
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
                text: 'Top Streamers for ' + game_name,
                font: {
                    size: 24,
                    color: 'rgb(82, 46, 238)'
                },
            },
            xaxis: {
                title: {
                    text: 'Viewers',
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

        var list = d3.select('#streamer_list');
        streamers.forEach(streamer => {
            var item = list.append('li').append('a').attr('href', '/streamer/'+streamer).text(streamer);
        })
    }) 
}

populate_chart();