// Create the Shell for the graph
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// SVG Wrapper, append SVG Wrapper to hold chart, 
var svg = d3
    .select(".chart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Apend and SVG grou
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

//Initial Params for GAME DATA 
var chosenXAxis = "Month"
var chosenYAxis = "Hours Watched";

// function to update x-scale variable on click of axis
function XScale(game_complete, chosenXAxis) {
    //create scales
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(game_complete, d => d[chossenXAxis]) * 0.8,
            d3.max(game_complete, d => d[chosenXAxis]) * 1.2
        ])  
        .range(0, width]);
    return xLinearScale;
}

// function to update yscale 