# Enhanced Click Counter

This project is a simple web page that displays a click counter, a reset button, a color change button, and a goal indicator.

## Purpose

The purpose of this page is to demonstrate the use of HTML, CSS, and JavaScript to create an interactive web page. The click counter allows users to click a button and see the number of clicks increase. The reset button resets the counter to zero. The color change button changes the background color of the page to a random color. The goal indicator shows a message when the goal of 10 clicks is reached or exceeded.

## Elements

### Click Button

The click button is an HTML button element with the id "clickButton". When clicked, it increments the click counter and updates the counter display.

```html
<button id="clickButton">Click Me!</button>
```

### Reset Button

The reset button is an HTML button element with the id "resetButton". When clicked, it resets the click counter to zero, clears the notification message, and sets the background color of the page to the default color.

```html
<button id="resetButton">Reset</button>
```

### Color Change Button

The color change button is an HTML button element with the id "colorButton". When clicked, it generates a random color and sets the background color of the page to that color.

```html
<button id="colorButton">Change Color</button>
```

### Counter Display

The counter display is an HTML div element with the id "counter". It displays the current number of clicks.

```html
<div id="counter">Clicks: 0</div>
```

### Goal Indicator

The goal indicator is an HTML div element with the id "goal". It displays the goal of 10 clicks.

```html
<div id="goal">Goal: 10 clicks</div>
```

### Notification Display

The notification display is an HTML div element with the id "notification". It displays a message when the goal of 10 clicks is reached or exceeded.

```html
<div id="notification"></div>
```

## JavaScript Code

The JavaScript code for this project is contained within the `<script>` tags of the HTML document. It defines variables for the click counter, the goal, and the HTML elements for the buttons, counter display, and notification message. It also defines event listeners for the buttons, and functions for updating the counter display, checking the goal, and generating random colors.

```javascript
let count = 0;
const goal = 10;
const button = document.getElementById('clickButton');
const resetButton = document.getElementById('resetButton');
const colorButton = document.getElementById('colorButton');
const counterDisplay = document.getElementById('counter');
const notificationDisplay = document.getElementById('notification');

button.addEventListener('click', () => {
    count++;
    updateCounter();
    checkGoal();
});

resetButton.addEventListener('click', () => {
    count = 0;
    updateCounter();
    notificationDisplay.textContent = '';
    document.body.style.backgroundColor = '#f0f0f0';
});

colorButton.addEventListener('click', () => {
    const randomColor = Math.floor(Math.random()*16777215).toString(16);
    document.body.style.backgroundColor = "#" + randomColor;
});

function updateCounter() {
    counterDisplay.textContent = `Clicks: ${count}`;
}

function checkGoal() {
    if (count === goal) {
        notificationDisplay.textContent = 'Goal reached!';
    } else if (count > goal) {
        notificationDisplay.textContent = 'Wow! You exceeded the goal!';
    }
}
```

This JavaScript code uses event listeners to respond to user interactions with the buttons, and functions to update the counter display and check the goal. It also generates random colors for the background of the page.