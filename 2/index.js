document.querySelectorAll('div').forEach((div, index) => {
    const status = div.getAttribute('data-status');

    if (status === 'inactive') {
        div.remove(); // حذف المان‌های غیرفعال
        return; // ادامه حلقه برای المان بعدی
    }

    // دریافت مقدار اولیه score و تبدیل به عدد
    let score = parseInt(div.getAttribute('data-score'), 10);

    // دو برابر کردن score
    score *= 2;

    // به‌روزرسانی attribute
    div.setAttribute('data-score', score);

    // تغییر متن داخلی با فرمت خواسته شده
    div.textContent = `Item ${index + 1} - Score: ${score} - Status: ${status}`;
});
