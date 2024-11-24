def add_to_cart(request, product_id, name, price):
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {'name': name, 'price': price, 'quantity': 1}

    request.session['cart'] = cart


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart


def update_cart(request, product_id, quantity):
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] = quantity
        request.session['cart'] = cart


def get_cart_items(request):
    return request.session.get('cart', {}).values()
