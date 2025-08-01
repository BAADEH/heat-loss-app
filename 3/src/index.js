document.getElementById('magicButton').addEventListener('click', () => {
    const target = document.getElementById('targetElement');
    
    // اضافه کردن کلاس highlight
    target.classList.add('highlight');

    // حذف کلاس بعد از ۳ ثانیه (۳۰۰۰ میلی‌ثانیه)
    setTimeout(() => {
        target.classList.remove('highlight');
    }, 3000);
});
