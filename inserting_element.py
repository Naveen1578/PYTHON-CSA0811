def insert_element(array, element, position):
    """Inserts an element into the specified position in the array"""
    array.insert(position, element)
    return array

def get_input():
    """Gets user input for the array and the element to be inserted"""
    num_elements = int(input("Enter the number of elements: "))
    array = list(map(int, input("Enter the elements: ").split(',')))
    element = int(input("Enter the element to be Inserted: "))
    position = int(input("Position: "))
    return array, element, position

def display_output(array):
    """Displays the modified array"""
    print("Modified array:", array)

def main():
    array, element, position = get_input()
    modified_array = insert_element(array, element, position)
    display_output(modified_array)

if __name__ == "__main__":
    main()
