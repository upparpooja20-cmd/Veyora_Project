from django.shortcuts import render, redirect


# =========================
# HOME
# =========================

def home(request):
    return render(request, 'store/home.html')


# =========================
# PRODUCT DATA
# =========================

PRODUCTS = {
    "classic-shirt": {
        "name": "Classic Everyday Shirt",
        "price": 799,
        "old_price": 1199,
        "rating": 4.5,
        "category": "Fashion",
        "images": [
            "store/images/classic-shirt-1.jpg",
            "store/images/classic-shirt-2.jpg",
            "store/images/classic-shirt-3.jpg",
        ],
    },

    "t-shirt": {
        "name": "Premium Cotton T-Shirt",
        "price": 599,
        "old_price": 899,
        "rating": 4.4,
        "category": "Fashion",
        "images": [
            "store/images/t-shirt-1.jpg",
            "store/images/t-shirt-2.jpg",
            "store/images/t-shirt-3.jpg",
        ],
    },

    "dress": {
        "name": "Elegant Casual Dress",
        "price": 1299,
        "old_price": 1899,
        "rating": 4.6,
        "category": "Fashion",
        "images": [
            "store/images/dress-1.jpg",
            "store/images/dress-2.jpg",
            "store/images/dress-3.jpg",
        ],
    },

    "jeans": {
        "name": "Comfort Fit Jeans",
        "price": 999,
        "old_price": 1499,
        "rating": 4.3,
        "category": "Fashion",
        "images": [
            "store/images/jeans-1.jpg",
            "store/images/jeans-2.jpg",
            "store/images/jeans-3.jpg",
        ],
    },

    "top": {
        "name": "Stylish Everyday Top",
        "price": 699,
        "old_price": 999,
        "rating": 4.5,
        "category": "Fashion",
        "images": [
            "store/images/top-1.jpg",
            "store/images/top-2.jpg",
            "store/images/top-3.jpg",
        ],
    },

    "jacket": {
        "name": "Urban Casual Jacket",
        "price": 1599,
        "old_price": 2299,
        "rating": 4.7,
        "category": "Fashion",
        "images": [
            "store/images/jacket-1.jpg",
            "store/images/jacket-2.jpg",
            "store/images/jacket-3.jpg",
        ],
    },

    "sneakers": {
        "name": "Classic Street Sneakers",
        "price": 1499,
        "old_price": 2199,
        "rating": 4.6,
        "category": "Footwear",
        "images": [
            "store/images/sneakers-1.jpg",
            "store/images/sneakers-2.jpg",
            "store/images/sneakers-3.jpg",
        ],
    },

    "casual-shoes": {
        "name": "Everyday Casual Shoes",
        "price": 1299,
        "old_price": 1899,
        "rating": 4.4,
        "category": "Footwear",
        "images": [
            "store/images/casual-shoes-1.jpg",
            "store/images/casual-shoes-2.jpg",
            "store/images/casual-shoes-3.jpg",
        ],
    },

    "sandals": {
        "name": "Comfort Walk Sandals",
        "price": 699,
        "old_price": 999,
        "rating": 4.3,
        "category": "Footwear",
        "images": [
            "store/images/sandals-1.jpg",
            "store/images/sandals-2.jpg",
            "store/images/sandals-3.jpg",
        ],
    },

    "sports-shoes": {
        "name": "Active Sports Shoes",
        "price": 1799,
        "old_price": 2499,
        "rating": 4.7,
        "category": "Footwear",
        "images": [
            "store/images/sports-shoes-1.jpg",
            "store/images/sports-shoes-2.jpg",
            "store/images/sports-shoes-3.jpg",
        ],
    },

    "audio-buds": {
        "name": "Wireless Audio Buds",
        "price": 999,
        "old_price": 1599,
        "rating": 4.4,
        "category": "Electronics",
        "images": [
            "store/images/audio-buds-1.jpg",
            "store/images/audio-buds-2.jpg",
            "store/images/audio-buds-3.jpg",
        ],
    },

    "headphones": {
        "name": "Premium Wireless Headphones",
        "price": 1999,
        "old_price": 2999,
        "rating": 4.6,
        "category": "Electronics",
        "images": [
            "store/images/headphones-1.jpg",
            "store/images/headphones-2.jpg",
            "store/images/headphones-3.jpg",
        ],
    },

    "smartwatch": {
        "name": "Smart Fitness Watch",
        "price": 2499,
        "old_price": 3499,
        "rating": 4.5,
        "category": "Electronics",
        "images": [
            "store/images/smartwatch-1.jpg",
            "store/images/smartwatch-2.jpg",
            "store/images/smartwatch-3.jpg",
        ],
    },

    "speaker": {
        "name": "Portable Bluetooth Speaker",
        "price": 1299,
        "old_price": 1899,
        "rating": 4.5,
        "category": "Electronics",
        "images": [
            "store/images/speaker-1.jpg",
            "store/images/speaker-2.jpg",
            "store/images/speaker-3.jpg",
        ],
    },

    "bag": {
        "name": "Everyday Carry Bag",
        "price": 899,
        "old_price": 1299,
        "rating": 4.4,
        "category": "Accessories",
        "images": [
            "store/images/bag-1.jpg",
            "store/images/bag-2.jpg",
            "store/images/bag-3.jpg",
        ],
    },

    "wallet": {
        "name": "Classic Leather Wallet",
        "price": 599,
        "old_price": 899,
        "rating": 4.5,
        "category": "Accessories",
        "images": [
            "store/images/wallet-1.jpg",
            "store/images/wallet-2.jpg",
            "store/images/wallet-3.jpg",
        ],
    },

    "watch": {
        "name": "Minimal Classic Watch",
        "price": 1499,
        "old_price": 2199,
        "rating": 4.6,
        "category": "Accessories",
        "images": [
            "store/images/watch-1.jpg",
            "store/images/watch-2.jpg",
            "store/images/watch-3.jpg",
        ],
    },

    "sunglasses": {
        "name": "Modern UV Sunglasses",
        "price": 799,
        "old_price": 1199,
        "rating": 4.3,
        "category": "Accessories",
        "images": [
            "store/images/sunglasses-1.jpg",
            "store/images/sunglasses-2.jpg",
            "store/images/sunglasses-3.jpg",
        ],
    },
}


# =========================
# CATEGORY PAGE
# =========================

def category(request):
    selected_category = request.GET.get("category", "Fashion")

    category_products = []

    for product_id, product in PRODUCTS.items():
        if product["category"].lower() == selected_category.lower():
            item = product.copy()
            item["id"] = product_id
            category_products.append(item)

    return render(
        request,
        "store/category.html",
        {
            "products": category_products,
            "category": selected_category,
        },
    )


# =========================
# PRODUCT PAGE
# =========================
def product(request):
    # Accept the product parameter used by the website
    product_id = request.GET.get("product") or request.GET.get("id")

    # If no product is selected, show classic shirt
    if not product_id:
        product_id = "classic-shirt"

    # Get the correct product from our complete product list
    product_data = PRODUCTS.get(product_id)

    # If the product doesn't exist, go back to the first product
    if not product_data:
        product_id = "classic-shirt"
        product_data = PRODUCTS["classic-shirt"]

    return render(
        request,
        "store/product.html",
        {
            "product": product_data,
            "product_id": product_id,
        },
    )


# =========================
# ADD TO CART
# =========================

def add_to_cart(request):
    product_id = request.GET.get("product")

    if product_id not in PRODUCTS:
        return redirect("home")

    product_data = PRODUCTS[product_id]

    cart = request.session.get("cart", {})

    if product_id in cart:
        cart[product_id]["quantity"] += 1
    else:
        cart[product_id] = {
            "name": product_data["name"],
            "price": product_data["price"],
            "category": product_data["category"],
            "image": product_data["images"][0],
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# =========================
# CART
# =========================

def cart(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, item in cart.items():

        subtotal = item['price'] * item['quantity']

        cart_items.append({
            'id': product_id,
            'name': item['name'],
            'price': item['price'],
            'category': item['category'],
            'quantity': item['quantity'],
            'subtotal': subtotal
        })

        total += subtotal

    return render(
        request,
        'store/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


# =========================
# CHECKOUT
# =========================

def checkout(request):
    cart_data = request.session.get("cart", {})

    if not cart_data:
        return redirect("cart")

    total = sum(
        item["price"] * item["quantity"]
        for item in cart_data.values()
    )

    if request.method == "POST":
        request.session["cart"] = {}
        request.session.modified = True

        return redirect("order_placed")

    return render(
        request,
        "store/checkout.html",
        {
            "cart": cart_data,
            "total": total,
        },
    )


# =========================
# ORDER PLACED
# =========================

def order_placed(request):
    return render(request, "store/order_placed.html")


# =========================
# WISHLIST
# =========================

def wishlist(request):
    return render(request, "store/wishlist.html")