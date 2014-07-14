var width = 800,
    height = 540;

// PW = #ccccff FERT FERT FERT FERT FERT FERT FERT FERT FERT FERT FERT
// OR = #ff4500
var color = ['rgb(148, 148, 255)',
             'rgb(32, 32, 32)',
             'rgb(255, 69, 0)'];

var force = d3.layout.force()
    .charge(-350) // repulsion
    .linkDistance(60) // spring
    .friction(0.95)
    .size([width, height]);

var svg = d3.select('div#map').append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('align', 'center');

d3.json('/static/maps/connector.json', function(error, chroma) {
    force.nodes(chroma.territories)
         .links(chroma.connections)
         .start();

    var connections = svg.selectAll('.connection')
        .data(chroma.connections)
        .enter().append('line')
        .attr('class', 'connection');

    var territories = svg.selectAll('.territory')
        .attr('width', 'inherit')
        .data(chroma.territories)
        .enter()
        .append('circle')
        .attr('class', 'territory')
        .attr('r', 8)
        .style('fill', function(d) { return color[d.affiliation]; })
        .call(force.drag);

    territories.append('title').text(function(d) { return d.name; });
    force.on('tick', function() {
        connections.attr('x1', function(d) { return d.source.x; })
                   .attr('y1', function(d) { return d.source.y; })
                   .attr('x2', function(d) { return d.target.x; })
                   .attr('y2', function(d) { return d.target.y; });

        territories.attr('cx', function(d) { return d.x; })
                   .attr('cy', function(d) { return d.y; });
    });
});

function byAffiliation() {
    svg.selectAll('.territory')
       .style('fill', function(d) { return color[d.affiliation]; });
}

function byContinent() {
    svg.selectAll('.territory')
       .style('fill', function(d) { return color[d.continent]; });
}

function logPositions() {
    positions = [];
    svg.selectAll('.territory').each(function(d) {
        positions.push(
            {
                name: d.name,
                url: d.url,
                continent: d.continent,
                affiliation: d.affiliation,
                x: Math.round(d.x),
                y: Math.round(d.y)
            }
        );
    });
    console.log(JSON.stringify(positions, null, 4));
}
