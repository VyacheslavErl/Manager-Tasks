document.addEventListener("DOMContentLoaded", function() {
    const days = document.querySelectorAll('.day');
    days.forEach(day => {
        const dailyTasks = day.querySelector('.daily-tasks');
        if (dailyTasks && dailyTasks.children.length === 0) {
            day.remove();
        }
    });
});