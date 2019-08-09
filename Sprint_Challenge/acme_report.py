from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        products.append(
            Product(name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0],
                    price = randint(5, 100),
                    weight = randint(5, 100),
                    flammability = uniform(0, 2.5)))
    return products

def inventory_report(products):
    product_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    for product in products:
        product_names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT', '\n',
          'Unique product names: ', len(set(product_names)), '\n',
          'Average price: ', total_price/len(products), '\n',
          'Average weight: ', total_weight/len(products), '\n',
          'Average flammability: ', total_flammability/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())