document.addEventListener('DOMContentLoaded', () => {
  const cartItems = [];
  const cartSection = document.querySelector('.cart-items');
  const checkoutBtn = document.getElementById('checkout');

  // Loading screen functionality
  window.onload = function() {
    const loadingScreen = document.getElementById('loading-screen');
    const mainContent = document.getElementById('main-content');
    // Hide the loading screen and show the main content
    loadingScreen.style.display = 'none';
    mainContent.style.display = 'block';
  };

  // Add to cart functionality
  document.querySelectorAll('.add-to-cart').forEach((button) => {
    button.addEventListener('click', (event) => {
      const productCard = event.target.closest('.product-card');
      const productId = productCard.dataset.id;
      const productName = productCard.querySelector('h3').textContent;
      const productPrice = parseFloat(productCard.querySelector('.price').textContent.replace('$', ''));

      const product = { id: productId, name: productName, price: productPrice };

      cartItems.push(product);
      updateCart();
    });
  });

  // Update cart section
  function updateCart() {
    if (cartItems.length === 0) {
      cartSection.innerHTML = '<p>Your cart is empty</p>';
    } else {
      cartSection.innerHTML = cartItems.map(item => `
        <div class="cart-item">
          <p>${item.name} - $${item.price}</p>
          <button class="remove-item" data-id="${item.id}">Remove</button>
        </div>
      `).join('');
    }

    // Remove item functionality
    document.querySelectorAll('.remove-item').forEach((button) => {
      button.addEventListener('click', (event) => {
        const itemId = event.target.dataset.id;
        const index = cartItems.findIndex(item => item.id === itemId);
        cartItems.splice(index, 1);
        updateCart();
      });
    });
  }

  // Checkout functionality
  checkoutBtn.addEventListener('click', () => {
    if (cartItems.length > 0) {
      alert(`You've checked out with ${cartItems.length} items!`);
      cartItems.length = 0;
      updateCart();
    } else {
      alert('Your cart is empty!');
    }
  });
});
