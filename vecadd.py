
def dot_product(vec1, vec2):
    """Compute the dot product of two equal-length vectors."""
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be the same length.")
    return sum(a * b for a, b in zip(vec1, vec2))

if __name__ == "__main__":
    # Input two vectors from the user
    vec1 = list(map(float, input("Enter elements of first vector separated by spaces: ").split()))
    vec2 = list(map(float, input("Enter elements of second vector separated by spaces: ").split()))

    result = dot_product(vec1, vec2)
    print("Dot product:", result)

