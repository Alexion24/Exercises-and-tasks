def same_parity_filter(items):
    return list(
        filter(
            lambda x: x % 2 == 0 if items[0] % 2 == 0 else x % 2 != 0, items
        )
    )


print(same_parity_filter([2, 0, 1, -3, 10, -2]))
