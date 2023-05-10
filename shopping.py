shop = [
    {
        'name': 'apple',
        'price': 10,
        'qty': 100
    },
    {
        'name': 'banana',
        'price': 5,
        'qty': 200
    },
    {
        'name': 'papaya',
        'price': 20,
        'qty': 20
    },
    {
        'name': 'mango',
        'price': 30,
        'qty': 50
    },

]

def buy_somethings(money, items_list):
    for item in items_list:
        for shop_item in shop:
            if item['name'] == shop_item['name']:
                pass