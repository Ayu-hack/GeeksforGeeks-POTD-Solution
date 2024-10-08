const quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Get busy living or get busy dying. – Stephen King",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "In the end, we only regret the chances we didn't take. – Lewis Carroll"
];

const quoteContainer = document.getElementById('quote');
const newQuoteButton = document.getElementById('new-quote');

// Single event listener for the button click
newQuoteButton.addEventListener('click', () => {
    console.log("Button clicked!"); // This will show in the console when clicked
    const randomIndex = Math.floor(Math.random() * quotes.length);
    quoteContainer.textContent = quotes[randomIndex];
});