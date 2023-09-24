# CSS (Cascading Style Sheets)

CSS is a language used to add style and presentation to an [HTML](/wiki/HTML) page. It allows you to control the layout, design, and visual presentation of web content. CSS is an essential technology for creating visually appealing and responsive web applications.

## Key Concepts

### Selectors

Selectors are patterns used to select and style HTML elements. CSS rules are applied to elements that match a given selector. Here are some common types of selectors:

- **Element Selector**: Selects HTML elements by their tag name (e.g., `p` selects all paragraphs).

- **Class Selector**: Selects elements with a specific class attribute (e.g., `.my-class` selects all elements with `class="my-class"`).

- **ID Selector**: Selects a single element with a specific ID attribute (e.g., `#my-id` selects the element with `id="my-id"`).

### Properties and Values

CSS rules consist of one or more declarations, each containing a property and a value. Properties define the aspect of an element to be styled, and values specify how the property should be styled. Here are some examples:

- **Color**: `color: blue;` sets the text color to blue.

- **Font Size**: `font-size: 16px;` sets the font size to 16 pixels.

- **Background Color**: `background-color: #f0f0f0;` sets the background color to a light gray.

### Cascading and Specificity

CSS stands for "Cascading Style Sheets" because styles can cascade or flow from one rule to another. The cascade is determined by the specificity of the selectors and their order in the stylesheet.

## Example Code Snippets

```css
/* Change text color and font size */
p {
    color: blue;
    font-size: 16px;
}
```