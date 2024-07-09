document.addEventListener('DOMContentLoaded', function(){
    const kpiElement = document.querySelector('.kpi-container');
    kpiElement.addEventListener('click', function(){
        kpiElement.style.backgroundColor = '#e74c3c';
        kpiElement.style.color = '#ffffff';
    });
});