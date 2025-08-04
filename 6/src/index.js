const box = document.getElementById("moving-box");
const button = document.getElementById("toggle-animation");

let isAnimating = false;
let direction = 1; // 1 for right, -1 for left
let position = 0;
let animationId = null;
const maxDistance = 300;
const duration = 2000; // milliseconds
const fps = 60;
const speedPerFrame = (maxDistance / duration) * (1000 / fps); // 2px/frame

function animate() {
    if (!isAnimating) return;

    position += direction * speedPerFrame;

    // Reverse direction at boundaries
    if (position >= maxDistance) {
        position = maxDistance;
        direction = -1;
    } else if (position <= 0) {
        position = 0;
        direction = 1;
    }

    box.style.left = position + "px";
    animationId = requestAnimationFrame(animate);
}

button.addEventListener("click", () => {
    isAnimating = !isAnimating;

    if (isAnimating) {
        button.textContent = "Pause Animation";
        animate();
    } else {
        button.textContent = "Start Animation";
        cancelAnimationFrame(animationId);
    }
});
