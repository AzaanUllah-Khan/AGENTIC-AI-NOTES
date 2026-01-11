`Topics`

* HTML
* HTML Tags
* CSS
* JavaScript
* React JS

---

### Topic 01: HTML

`Hyper Text Markup Language`

HTML defines the **structure and content** of a website. It tells the browser what each element means (heading, image, form, link, etc.).

### Key Characteristics

* Markup language (not programming)
* Uses **tags + attributes**
* Works with CSS (design) and JS (logic)
* Browser renders HTML into visible UI

### Basic HTML Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
    <meta charset="UTF-8" />
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

### Common HTML Tags

#### Text Tags

* `<h1> – <h6>` → Headings
* `<p>` → Paragraph
* `<span>` → Inline container
* `<strong>` → Bold importance
* `<em>` → Emphasis

#### Media Tags

* `<img>` → Images
* `<video>` → Video
* `<audio>` → Audio

#### Layout Tags

* `<div>` → Block container
* `<section>` → Section block
* `<article>` → Independent content
* `<header>` → Header area
* `<footer>` → Footer area
* `<nav>` → Navigation

#### Lists

* `<ul>` → Unordered list
* `<ol>` → Ordered list
* `<li>` → List item
* `<dl>` → Description list
* `<dt>` → Term
* `<dd>` → Definition

#### Tables

* `<table>`
* `<tr>` → Row
* `<th>` → Header cell
* `<td>` → Data cell

#### Forms

* `<form>`
* `<input>`
* `<textarea>`
* `<select>`
* `<button>`
* `<label>`

### Attributes Examples

* `src`, `href`, `alt`, `id`, `class`, `type`, `placeholder`

### Semantic HTML Benefits

* Better SEO
* Better accessibility
* Cleaner code

> View Full Detail: [Class 14](https://github.com/AzaanUllah-Khan/AGENTIC-AI-NOTES/blob/main/Class%2014/Class%2014.md)

---

### Topic 02: CSS

`Cascading Style Sheets`

CSS is used to control the **design, layout, colors, spacing, animations and responsiveness** of websites.

### Ways to Apply CSS

1. Inline CSS
2. Internal CSS
3. External CSS (recommended)

### CSS Syntax

```css
selector {
  property: value;
}
```

### Core CSS Properties

#### Design

* `color`
* `background-color`
* `font-size`
* `font-family`
* `text-align`
* `opacity`

#### Box Model

* `margin`
* `padding`
* `border`
* `width`
* `height`

#### Layout

* `display`
* `position`
* `flex`
* `grid`
* `float`

#### Animations

* `transition`
* `transform`
* `animation`

#### Responsive

* `media queries`
* `max-width`
* `min-width`

### Selectors

* Element selector → `p {}`
* Class selector → `.box {}`
* ID selector → `#main {}`
* Attribute selector → `input[type="text"]`

### Modern Layout Systems

#### Flexbox

* Used for 1D layouts
* Properties: `justify-content`, `align-items`, `gap`

#### Grid

* Used for 2D layouts
* Properties: `grid-template-columns`, `grid-gap`

---

### Topic 03: JavaScript

JavaScript adds **logic, interaction, and dynamic behavior** to websites.

### What JS Can Do

* Handle user actions (click, input)
* Change HTML content dynamically
* Fetch data from APIs
* Validate forms
* Build web apps

### Core Concepts

* Variables (`let`, `const`)
* Data types (string, number, boolean, array, object)
* Functions
* Conditions (`if`, `switch`)
* Loops (`for`, `while`)
* Events

### Example

```javascript
const btn = document.querySelector("button");

btn.addEventListener("click", () => {
  alert("Hello World");
});
```

### DOM Manipulation

* `document.querySelector()`
* `innerHTML`
* `classList`
* `style`

### ES6 Features

* Arrow functions
* Destructuring
* Spread operator
* Modules

---

### Topic 05: React JS

React is a **JavaScript library** for building fast, scalable UI applications.

### Why React?

* Component-based architecture
* Virtual DOM (performance)
* Reusable UI components
* Strong ecosystem

### Prerequisites

* HTML
* CSS
* JavaScript (ES6)
* Node.js installed

### Install Node

Download from: [https://nodejs.org](https://nodejs.org)

Verify:

```
node -v
npm -v
```

### Create React App

```
npx create-react-app my-app
cd my-app
npm start
```

### Recommended File Structure

```
src/
 ├── components/
 ├── pages/
 ├── assets/
 ├── App.js
 └── main.jsx
```

### Core Concepts

* Components
* JSX
* Props
* State
* Hooks (`useState`, `useEffect`)
* Events

### Sample Component

```jsx
function Button() {
  return <button>Click Me</button>;
}
```

### In-Depth Learning Path

1. JSX Fundamentals
2. Component Reusability
3. Props & State
4. Hooks
5. API Integration
6. Routing
7. Performance Optimization

---

###  Bonus: Best Practices

* Write semantic HTML
* Use mobile-first CSS
* Keep JS modular
* Use Git version control
* Optimize images
* Follow accessibility rules
