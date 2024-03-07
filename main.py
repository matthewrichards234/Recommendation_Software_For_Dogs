from classNode import *
from classLinkedList import *
from Data import *

def main():
    # Create linked lists for dog breeds and stats
    breeds_list = LinkedList()
    stats_list = LinkedList()

    # Populate the linked lists with dog breeds and stats
    for breed_data in dog_breed_data:
        breed_name = breed_data[0]
        breed_stats = ", ".join(str(stat) for stat in breed_data[1:])
        breeds_list.insert_beginning(breed_name)
        stats_list.insert_beginning(breed_stats)

    while True:
        # Ask the user for the dog breed they want to search for
        breed = input("Enter the dog breed you want to search for: ")

        # Find the index of the breed in the breeds_list
        current_node = breeds_list.get_head_node()
        index = 0
        while current_node:
            if current_node.get_value() == breed:
                break
            current_node = current_node.get_next_node()
            index += 1

        # If the breed is found, print its stats
        if current_node:
            stats_node = stats_list.get_head_node()
            for _ in range(index):
                stats_node = stats_node.get_next_node()
            print(f"Stats for {breed}: {stats_node.get_value()}")
        else:
            print(f"Dog breed '{breed}' not found.")

        # Ask the user if they want to try again
        try_again = input("Do you want to try again? (yes/no): ")
        if try_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
