from iterable import WordsCollection, MatrixCollection

collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()), end="")

print("\n")

collection2 = MatrixCollection()
collection2.add_item([1, 2, 3, 4, 5, 6])


collection2.show()
for x in collection2:
    print(x)