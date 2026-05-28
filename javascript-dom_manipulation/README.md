# Holberton School - JavaScript DOM manipulation

## Description

This project focuses on mastering DOM (Document Object Model) manipulation and handling asynchronous network requests using JavaScript. It covers selecting and modifying HTML elements, managing classes, handling user events, and fetching data from external APIs asynchronously without reloading the web page.

## Environment & Technical Requirements

* **Language:** JavaScript (ES6+)
* **Runtime Environment:** Google Chrome (Version 57.0 or later)
* **Code Style:** `semistandard` compliant
* **Variables:** Strict usage of `let` and `const` (usage of `var` is prohibited)
* **Behavior:** Dynamic UI updates and asynchronous data fetching without HTML page reloads.

---

## Project Structure & Task Breakdown

Each JavaScript file corresponds to a specific DOM manipulation or API task:

| File | Task | Description |
| :--- | :--- | :--- |
| `0-script.js` | 0. Color Me | Updates the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector`. |
| `1-script.js` | 1. Click and turn red | Changes the `<header>` text color to red when the user clicks on the `#red_header` element. |
| `2-script.js` | 2. Add `.red` class | Adds the CSS class `.red` to the `<header>` element upon clicking `#red_header`. |
| `3-script.js` | 3. Toggle classes | Toggles `.red` and `.green` classes on the `<header>` element when `#toggle_header` is clicked. |
| `4-script.js` | 4. List of elements | Adds a new `<li>Item` element to `ul.my_list` whenever `#add_item` is clicked. |
| `5-script.js` | 5. Change the text | Updates the text of the `<header>` to "New Header!!!" when `#update_header` is clicked. |
| `6-script.js` | 6. Star Wars Character | Fetches and displays the character name from the SWAPI API in the `#character` element. |
| `7-script.js` | 7. Star Wars Movies | Fetches all Star Wars movie titles from the SWAPI API and lists them in the `#list_movies` element. |
| `8-script.js` | 8. Say Hello! | Fetches a translation of "hello" from an API and displays it in the `#hello` element. |
| `9-script.js` | 9. List, Add, Remove `(Advanced)` | Manages a dynamic list (adds, removes, and clears elements) based on distinct user click events. |
| `10-script.js` | 10. Say Hello to Everybody! `(Advanced)` | Fetches "hello" translations in multiple languages and populates them into the `#list_hello` element. |

---

## Installation & Usage

### **1. Clone the Repository:**
```bash
git clone https://github.com/mammadovs/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/javascript-dom_manipulation
```

### **2. Running the Code**
Since this project runs entirely in the browser, you can execute it without any backend server:
* Open the corresponding HTML file (e.g., 0-main.html, 1-main.html, etc.) directly in Google Chrome by double-clicking it.
* Alternatively, use the Live Server extension in VS Code for a local development server experience.

### **3. Debugging**
To ensure everything works correctly and scripts load properly:
* Open Google Chrome.
* Press F12 or Right-Click -> Inspect to open Developer Tools.
* Navigate to the Console tab to check for any linting errors or failed network requests.

## Author

*   **Saddam Mammadov** - Student at [Holberton School Azerbaijan](https://www.holbertonschool.az/).

