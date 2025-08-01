const colors = [
    'hsl(0, 70%, 85%)',
    'hsl(120, 70%, 85%)',
    'hsl(240, 70%, 85%)',
    'hsl(60, 70%, 85%)',
    'hsl(180, 70%, 85%)',
    'hsl(300, 70%, 85%)',
];


let index = 0;

setInterval(() => {
    document.body.style.backgroundColor = colors[index];
    index = (index + 1) % colors.length; 
}, 2000);