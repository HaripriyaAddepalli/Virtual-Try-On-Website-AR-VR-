const productData = {
    men: {
        tops: {
            'T-Shirts': ['Men\'s T-Shirt 1', 'Men\'s T-Shirt 2'],
            'Dress Shirts': ['Men\'s Dress Shirt 1', 'Men\'s Dress Shirt 2'],
            'Polo Shirts': ['Men\'s Polo Shirt 1', 'Men\'s Polo Shirt 2'],
            'Hoodies': ['Men\'s Hoodie 1', 'Men\'s Hoodie 2'],
            'Sweatshirts': ['Men\'s Sweatshirt 1', 'Men\'s Sweatshirt 2']
        },
        // Other subcategories for men...
    },
    women: {
        tops: {
            'Blouses': ['Women\'s Blouse 1', 'Women\'s Blouse 2'],
            'Tank Tops': ['Women\'s Tank Top 1', 'Women\'s Tank Top 2'],
            'T-Shirts': ['Women\'s T-Shirt 1', 'Women\'s T-Shirt 2'],
            'Sweaters': ['Women\'s Sweater 1', 'Women\'s Sweater 2']
        },
        // Other subcategories for women...
    },
    kids: {
        tops: {
            'T-Shirts': ['Kids\' T-Shirt 1', 'Kids\' T-Shirt 2'],
            'Long Sleeve Shirts': ['Kids\' Long Sleeve Shirt 1', 'Kids\' Long Sleeve Shirt 2'],
            'Sweaters': ['Kids\' Sweater 1', 'Kids\' Sweater 2'],
            'Hoodies': ['Kids\' Hoodie 1', 'Kids\' Hoodie 2']
        },
        // Other subcategories for kids...
    }
};

// Upload image and start camera functions
const uploadImageBtn = document.getElementById('upload-image');
const startCameraBtn = document.getElementById('start-camera');
const fileInput = document.getElementById('file-input');
const cameraFeed = document.getElementById('camera-feed');
const uploadedImage = document.getElementById('uploaded-image');
const categoriesSection = document.getElementById('categories-section');
const subcategoriesContainer = document.getElementById('subcategories');
const productCatalogSection = document.getElementById('product-catalog');
const productGrid = document.getElementById('product-grid');

// Handle file upload
uploadImageBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            cameraFeed.style.display = 'none';  // Hide camera feed if it was active
            categoriesSection.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

// Start camera
startCameraBtn.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraFeed.srcObject = stream;
        cameraFeed.style.display = 'block';
        uploadedImage.style.display = 'none';  // Hide uploaded image if it was active
        categoriesSection.style.display = 'block';
    } catch (err) {
        console.error('Error accessing the camera: ', err);
    }
});

// Show subcategories when category is selected
document.querySelectorAll('.category-btn').forEach(button => {
    button.addEventListener('click', () => {
        const category = button.dataset.category;
        loadSubcategories(category);
    });
});

// Load subcategories based on selected category
function loadSubcategories(category) {
    subcategoriesContainer.innerHTML = '';  // Clear any existing subcategories

    const subcategoryGroups = Object.keys(productData[category]);
    subcategoryGroups.forEach(group => {
        const subcategoryTitle = document.createElement('h3');
        subcategoryTitle.textContent = group.charAt(0).toUpperCase() + group.slice(1); // Capitalize first letter
        subcategoriesContainer.appendChild(subcategoryTitle);

        const subcategories = Object.keys(productData[category][group]);
        subcategories.forEach(subcategory => {
            const subcategoryButton = document.createElement('button');
            subcategoryButton.classList.add('category-btn');
            subcategoryButton.textContent = subcategory;
            subcategoryButton.addEventListener('click', () => {
                loadProducts(category, group, subcategory);
            });
            subcategoriesContainer.appendChild(subcategoryButton);
        });
    });

    subcategoriesContainer.style.display = 'block';  // Show subcategories section
    productCatalogSection.style.display = 'none';  // Hide product catalog section
}

// Load products based on selected subcategory
function loadProducts(category, group, subcategory) {
    productGrid.innerHTML = '';  // Clear any existing products

    const products = productData[category][group][subcategory];
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `<p>${product}</p>`;
        productGrid.appendChild(productDiv);
    });

    productCatalogSection.style.display = 'block';  // Show product catalog section
}
