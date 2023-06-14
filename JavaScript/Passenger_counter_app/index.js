// document.getElementById("count-el").innerText = 5  --> Comment

// Storing count --> Variable
// let count = 0

// console.log(count)

// variable --> myAge & log to the console.
// let myAge = 35
// console.log(myAge)

// Arithmetic Operators
// let firstBatch = 5
// let secondBatch = 7

// let count = firstBatch + secondBatch

// console.log(count)

// humanDogRatio --> 1 human year == 7 dog years
// let myAge = 26
// let humanDogRatio = 7

// let myDogAge = myAge * humanDogRatio

// console.log(myDogAge)

// REASSIGNING & INCREMENTING
// let count = 5

// count + 1 --> Incrementing by 1
// count = count + 1

// console.log(count)

// Create bonusPoints --> Initialize it at 50
// let bonusPoints = 50
// Increase to 100
// bonusPoints = bonusPoints + 50
// Decrease to 25
// bonusPoints = bonusPoints - 75
// Increase to 70
// bonusPoints = bonusPoints + 45

// console.log(bonusPoints)

// INCREMENT BUTTON FUNCTIONALITY
// - Initialize the count as 0
// - Listen for clicks on the increment button
// - Increment the count variable when the button is clicked.
// - Change the count-el in the HTML to reflect the new count

// FUNCTIONS
// function increment() {
//     console.log("The button was clicked!")
// }

// RACE CAR GAME
// - Setting up the race

// function countdown() {
//     console.log(5)
//     console.log(4)
//     console.log(3)
//     console.log(2)
//     console.log(1)
// }

// countdown()  // --> Invoking or calling the function

// GO!

// Laps  --> Global Scope
// let lap1 = 34
// let lap2 = 33
// let lap3 = 36
// Create a function that logs out the sum of all the lap times
// function sumLapTime() {
//     let totalSum = lap1 + lap2 + lap3
//     console.log(totalSum)
// }

// sumLapTime()
// Players are running the race
// Race is finished!

// Get ready for a new race...
// countdown()



// Assignment
// Create a function that logs out the number 42 to the console
// function fourtyTwo() {
//     console.log(42)
// }
// Call/Invoke the function
// fourtyTwo()

// let lapsCompleted = 0

// Create a function that increments the lapsCompleted variable with one
// Run it three times

// function lapCount() {
//     lapsCompleted += 1
//     console.log(lapsCompleted)
// }

// lapCount()
// lapCount()
// lapCount()

// INCREMENT ON CLICKS
// - Initialize the count as 0
// - Listen for clicks on the increment button
// - Increment the count vaiable when the button is clicked (log it out)
// - Change the count-el in the HTML to reflect the new count

// Display the count
let countEl = document.getElementById("count-el")

console.log(countEl)

let count = 0

function increment() {
    // console.log("clicked")
    count += 1
    countEl.innerText = count
    console.log(count)
}
