def sweep_max(items: list) -> list:
    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos], items[0]
    return items


if __name__ == "__main__":
    print(sweep_max([10, 9, 4, 32, 4]))
