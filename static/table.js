d3.json('http://localhost:5000/test').then(function(data) {
    
    var tbody = d3.select('tbody');
    Object.entries(data).forEach(([key,value]) => {
        var row = tbody.append('tr')
        var cell = row.append('td')
        cell.text(value['avg_viewers'])
        var cell = row.append('td')
        cell.text(key)
    })
    
})

