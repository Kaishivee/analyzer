import json


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def calculate_stats(data):
    prices = {}  # Словарь для хранения общей суммы продаж по категориям
    categories = {}  # Словарь для хранения общей суммы продаж по категориям

    for item in data:
        category = item['category']  # Получаем категорию предмета
        price = item['price']  # Получаем цену предмета

        if category not in categories:
            prices[category] = 0
            categories[category] = 0

        prices[category] += price
        categories[category] += 1
    return prices, categories


def main(file_path):
    data = load_data(file_path)
    total_price, total_category = calculate_stats(data)
    return total_price, total_category


if __name__ == "__main__":
    file_path = 'f.json'
    total_price, total_category = main(file_path)

    print(total_price)
    print(total_category)
