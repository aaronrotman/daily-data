// The date the countdown ends
var countDownDate = new Date("Nov 11, 2020 18:00:00").getTime();

// Update the time every 1 second
setInterval(() => {

    // Store the current time
    var currentTime = new Date().getTime();

    // Calculate the time until the countdown ends
    var timeLeft = countDownDate - currentTime;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
        
    // Display the time remaining in the countdown row
    document.getElementById("countDown").innerHTML = `Shadow Draw Countdown: ${days}D ${hours}H ${minutes}M ${seconds}S`;

    // Display a message if the countdown is complete 
    if (timeLeft < 0) {
        clearInterval();
        document.getElementById("countDown").innerHTML = "The shadow draw has ended!";
    }  

}, 1000);