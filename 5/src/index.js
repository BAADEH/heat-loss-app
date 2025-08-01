const box = document.getElementById('moving-box');
const button = document.getElementById('toggle-animation');

let intervalId = null;
let position = 0;
let direction = 1; // 1 برای جلو، -1 برای عقب

function startAnimation() {
    const duration = 2000; // 2 ثانیه برای رفت یا برگشت
    const distance = 300;  // پیکسل
    const frameRate = 10;  // هر 10ms یک فریم
    const step = (distance / (duration / frameRate)); // مقدار حرکت در هر فریم

    intervalId = setInterval(() => {
        position += step * direction;
        box.style.left = `${position}px`;

        if (position >= distance || position <= 0) {
            direction *= -1; // تغییر جهت
        }
    }, frameRate);
}

function stopAnimation() {
    clearInterval(intervalId);
    intervalId = null;
}

button.addEventListener('click', () => {
    if (intervalId === null) {
        startAnimation();
        button.textContent = 'Pause Animation';
    } else {
        stopAnimation();
        button.textContent = 'Start Animation';
    }
});
