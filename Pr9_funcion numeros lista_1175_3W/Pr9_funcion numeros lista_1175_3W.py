print(" ")
print("Alvaro Campechano 3W")
print(" ")
def sum(numbers):
    """
    Suma todos los números en una lista.

    Parameters:
    numbers (list): Una lista de números (int o float).

    Returns:
    int or float: La suma de todos los números en la lista.
    
    Example:
    >>> sum([1, 2, 3, 4])
    10
    """
    total = 0
    for number in numbers:
        total += number
    return total

def multip(numbers):
    """
    Multiplica todos los números en una lista.

    Parameters:
    numbers (list): Una lista de números (int o float).

    Returns:
    int or float: El producto de todos los números en la lista.
    
    Example:
    >>> multip([1, 2, 3, 4])
    24
    """
    product = 1
    for number in numbers:
        product *= number
    return product

# Ejemplo de uso
if __name__ == "__main__":
    print(sum([1, 2, 3, 4]))  # Debería imprimir 10
    print(multip([1, 2, 3, 4]))  # Debería imprimir 24
