
function DrawFedDotPlot(url) {

  var margin = {top: 20, right: 20, bottom: 30, left: 40},
      width = 960 - margin.left - margin.right,
      height = 760 - margin.top - margin.bottom;

  var x = d3.scale.ordinal().rangeRoundBands([0, width], 1.2);

  var x2 = d3.scale.ordinal().rangeRoundBands([0, width], .8);

  var y = d3.scale.linear().range([height, 0]);

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  var svg = d3.select("#chart").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  d3.json(url, function(error, data) {
    console.log(data);
    x.domain(data.map(function(d) { return d.year; }));
    y.domain(d3.extent(data, function(d) { return d.rate; })).nice();

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
      .append("text")
        .attr("class", "label")
        .attr("x", width)
        .attr("y", -6)
        .style("text-anchor", "end");

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("class", "label")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end");

    svg.selectAll(".dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "dot")
        .attr("r", function(d) { return d.count*3 } )
        .attr("cx", function(d) { return x(d.year) })
        .attr("cy", function(d) { return y(d.rate); })
        .attr("fill", "#00DC3C");
  });

}
