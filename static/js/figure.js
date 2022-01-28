



//function for dropdown menu and initial graphs 
function init() {
    colType = ['Administrative_Avg', 'Informational_Avg', 'ProductRelated_Avg',
        'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay', 'Month',
        'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType',
        'Weekend', 'Revenue'];
    var menu1 = d3.select("#selDataset1");
    colType.forEach((type) => {
        menu1.append("option").text(type).property("value", type);
    });

    var menu2 = d3.select("#selDataset2");
    colType.forEach((type) => {
        menu2.append("option").text(type).property("value", type);
    });
};


init();

