var leftBtn = document.getElementById('leftBtn');
var forwardBtn = document.getElementById('forwardBtn');
var rightBtn = document.getElementById('rightBtn');
var backwardBtn = document.getElementById('backwardBtn');


document.onkeydown = function (event) {
    switch (event.keyCode) {
        case 37:
            console.log("Left key is pressed.");
            leftBtn.click();
            break;
        case 38:
            console.log("Up key is pressed.");
            forwardBtn.click();
            break;
        case 39:
            console.log("Right key is pressed.");
            rightBtn.click();
            break;
        case 40:
            console.log("Down key is pressed.");
            backwardBtn.click();
            break;
    }
};