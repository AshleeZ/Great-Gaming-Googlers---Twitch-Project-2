function populate_categories() {

    var categories = ['Choose a Category','MOBA','RPG','Shooting','Strategy'];
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
        case 'RPG':
            var games = ['Zelda','Pokemon','Final Fantasy'];
            break;
        case 'Shooting':
            var games = ['Fortnite','Call of Duty','Halo'];
            break;
        case 'Strategy':
            var games = ['Chess','Among Us', 'BloonsTD6'];
            break;
        default:
            var games = []
    }

    var games_list = d3.select("#games");
    games_list.html("");
    games.forEach(game => {
        var item = games_list.append('li').append('a').attr('href', 'games/'+game).text(game)
    })
}

d3.select("#select_category").on("change", populate_games);