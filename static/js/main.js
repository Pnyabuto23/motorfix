// static/js/main.js

// Example: Show a message when the page loads
document.addEventListener("DOMContentLoaded", function () {
    console.log("MotorFix site loaded 🚗🔧");

    // Example: simple form validation
    let bookingForm = document.querySelector("#bookingForm");
    if (bookingForm) {
        bookingForm.addEventListener("submit", function (event) {
            let name = document.querySelector("#id_customer_name").value;
            let email = document.querySelector("#id_email").value;

            if (!name || !email) {
                alert("Please fill in all required fields before submitting!");
                event.preventDefault(); // stop form from submitting
            }
        });
    }
});
