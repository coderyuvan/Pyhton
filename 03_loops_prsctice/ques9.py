items=["apple", "banana", "cherry", "date", "elderberry","apple"]

unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate item found: {item}")
        break
    unique_items.add(item)

    