var CHROMA_TERRITORIES_URL = 'http://faceless-games.com/chromabot/report.json';

var width = 800,
    height = 540;

var colors = ['rgb(148, 148, 255)', // PW = #9494ff FERT FERT FERT FERT FERT FERT FERT FERT FERT FERT FERT
              'rgb(32, 32, 32)',
              'rgb(255, 69, 0)']; // OR = #ff4500

var force = d3.layout.force()
    .charge(-350) // repulsion
    .linkDistance(60) // spring
    .friction(0.95)
    .size([width, height]);

var svg = d3.select('div#map').append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('align', 'center');

function bothLoaded(request1, request2, callback) {
    return request1.done(function(data1){
        return request2.done(function(data2){
            return callback(data1, data2);
        });
    });
}

function startD3(chromaConfig, territoryStates) {
    force.nodes(territoryData.territories)
         .links(connectionConfig.connections)
         .start();
    
    var connections = svg.selectAll('.connection')
        .data(connections)
        .enter().append('line')
        .attr('class', 'connection');
    
    var territories = svg.selectAll('.territory')
        .attr('width', 'inherit')
        .data(territories)
        .enter()
        .append('circle')
        .attr('class', 'territory')
        .attr('r', 8)
        .style('fill', function(d) { return colors[d.affiliation]; })
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
}

function byAffiliation() {
    svg.selectAll('.territory')
       .style('fill', function(d) { return colors[d.affiliation]; });
}

function byContinent() {
    svg.selectAll('.territory')
       .style('fill', function(d) { return colors[d.continent]; });
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

$.ajax({
    url: CHROMA_TERRITORIES_URL
}).done(startD3);
