/**
*   somGrid             draws SOM grid 
*                     
*   @param id           div id tag starting with #
*   @param width        width of the grid in pixels
*   @param height       height of the grid in pixels
*   @param square       true/false if you want the height to 
*                           match the (calculated first) width
*/
function somGrid(id, width, height, square)
{
    var somNodes = generateNodes(width, height, square);
    console.log(somNodes);
    var grid = d3.select(id).append("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .attr("class", "chart");

    var row = grid.selectAll(".row")
                  .data(somNodes)
                .enter().append("svg:g")
                  .attr("class", "row");

    var col = row.selectAll(".cell")
                 .data(function (d) { return d; })
                .enter().append("svg:rect")
                 .attr("class", "cell")
                 .attr("x", function(d) { return d.x; })
                 .attr("y", function(d) { return d.y; })
                 .attr("width", function(d) { return d.width; })
                 .attr("height", function(d) { return d.height; })
                 .on('mouseover', function() {
                    d3.select(this)
                        .transition()
                        .duration(10)
                        .style('fill-opacity', 0.5);
                 })
                 .on('mouseout', function() {
                    d3.select(this)
                        .transition()
                        .duration(1000)
                        .style('fill-opacity', 1);
                 })
                 .on('click', function() {
                    console.log(d3.select(this));
                 })
                 .style("fill", "teal")
                 .style("stroke", '#FFF');
}

////////////////////////////////////////////////////////////////////////

/**
*   generateNodes()   generates array with positions and nodes' dimensions       
*/

function generateNodes(gridWidth, gridHeight, square)
{
    var data = new Array();
    var gridItemWidth = gridWidth / 17;
    var gridItemHeight = (square) ? gridItemWidth : gridHeight / 20;
    var startX = gridItemWidth / 2;
    var startY = gridItemHeight / 2;
    var stepX = gridItemWidth;
    var stepY = gridItemHeight;
    var xpos = startX;
    var ypos = startY;
    var newValue = 0;
    var count = 0;

    for (var index_a = 0; index_a < 10; index_a++)
    {
        data.push(new Array());
        for (var index_b = 0; index_b < 10; index_b++)
        {
            data[index_a].push({ 
                                width: gridItemWidth,
                                height: gridItemHeight,
                                x: xpos,
                                y: ypos,
                                count: count
                            });
            xpos += stepX;
            count += 1;
        }
        xpos = startX;
        ypos += stepY;
    }
    return data;
}