document.addEventListener("DOMContentLoaded", function () {
    const lessonButtons = document.querySelectorAll(".lesson-button");
    const lessonBox = document.querySelector(".lesson-box");
    const lessonTitle = document.querySelector(".lesson-title");
    
    lessonButtons.forEach(button => {
        button.addEventListener("click", function () {
            let lessonId = this.getAttribute("data-lesson");
            
            if (!lessonId || lessonId === "null") {
                lessonId = this.getAttribute("data-practice");
            }

            if (!lessonId) {
                console.error("Ошибка: lessonId и practiceId не заданы.");
                return;
            }

            fetch(`/lesson/${lessonId}/`)
                .then(response => response.text())
                .then(data => {
                    lessonTitle.textContent = this.textContent;
                    lessonBox.innerHTML = data;
                })
                .catch(error => console.error("Ошибка загрузки урока:", error));
        });
    });
});
