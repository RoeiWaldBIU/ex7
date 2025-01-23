import csv

# Global BST root
ownerRoot = None

########################
# 0) Read from CSV -> HOENN_DATA
########################


def read_hoenn_csv(filename):
    """
    Reads 'hoenn_pokedex.csv' and returns a list of dicts:
      [ { "ID": int, "Name": str, "Type": str, "HP": int,
          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },
        ... ]
    """
    data_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter
        first_row = True
        for row in reader:
            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it
            if first_row:
                first_row = False
                continue

            # row => [ID, Name, Type, HP, Attack, Can Evolve]
            if not row or not row[0].strip():
                break  # Empty or invalid row => stop
            d = {
                "ID": int(row[0]),
                "Name": str(row[1]),
                "Type": str(row[2]),
                "HP": int(row[3]),
                "Attack": int(row[4]),
                "Can Evolve": str(row[5]).upper()
            }
            data_list.append(d)
    return data_list


HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")

########################
# 1) Helper Functions
########################

def read_int_safe(prompt):
    """
    Prompt the user for an integer, re-prompting on invalid input.
    """
    pass

def get_poke_dict_by_id(poke_id):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by ID, or None if not found.
    """
    pass

def get_poke_dict_by_name(name):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by name, or None if not found.
    """
    pass

def display_pokemon_list(poke_list):
    """
    Display a list of Pokemon dicts, or a message if empty.
    """
    pass


########################
# 2) BST (By Owner Name)
########################
def new_pokedex():
    global ownerRoot
    name = input("Owner name: ")
    if find_owner_bst(ownerRoot, name) is not None:
        print(F"Owner '{name}' already exists. No new Pokedex created.")
        return
    print("Choose your starter Pokemon:")
    print("1) Treecko")
    print("2) Torchic")
    print("3) Mudkip")
    first_pokemon = int(input("Your choice: "))
    first_pokemon = (first_pokemon - 1)*3
    new_owner = create_owner_node(name, first_pokemon)
    if ownerRoot is None:
        ownerRoot = new_owner
    else:
        insert_owner_bst(ownerRoot, new_owner)
    print(f"New Pokedex created for {name} with starter {HOENN_DATA[first_pokemon]['Name']}.")
    return

def create_owner_node(owner_name, first_pokemon):
    owner = {'owner': owner_name,
             'pokedex':[],
             'left': None,
             'right': None }
    owner['pokedex'].append(HOENN_DATA[first_pokemon])
    return owner

def insert_owner_bst(root, new_node):
    if root is None:
        root = new_node
        return root
    elif new_node['owner'] < root['owner']:
        root['left'] = insert_owner_bst(root['left'], new_node)
    else:
        root['right'] = insert_owner_bst(root['right'], new_node)
# return None means
def find_owner_bst(root, owner_name):
    if root is None:
        return None
    elif root['owner'].lower() == owner_name.lower():
        return root
    elif root['owner'] < owner_name:
        return find_owner_bst(root['right'], owner_name)
    else:
        return find_owner_bst(root['left'], owner_name)

def min_node(node):
    """
    Return the leftmost node in a BST subtree.
    """
    pass

def delete_owner_bst(root, owner_name):
    """
    Remove a node from the BST by owner_name. Return updated root.
    """
    pass


########################
# 3) BST Traversals
########################

def bfs_traversal(root):
    """
    BFS level-order traversal. Print each owner's name and # of pokemons.
    """
    pass

def pre_order(root):
    """
    Pre-order traversal (root -> left -> right). Print data for each node.
    """
    pass

def in_order(root):
    """
    In-order traversal (left -> root -> right). Print data for each node.
    """
    pass

def post_order(root):
    """
    Post-order traversal (left -> right -> root). Print data for each node.
    """
    pass


########################
# 4) Pokedex Operations
########################

def add_pokemon_to_owner(owner_node):
    choice = int(input("Enter Pokemon ID to add: "))
    while choice < 1 or choice > 135:
        print ("Invalid input")
        choice = int(input("Enter Pokemon ID to add: "))
    if HOENN_DATA[choice-1] in owner_node['pokedex']:
        print("Pokemon already in the list. No changes made.")
        return
    owner_node['pokedex'].append(HOENN_DATA[choice - 1])
    print(f"Pokemon {HOENN_DATA[choice - 1]['Name']} (ID {HOENN_DATA[choice - 1]['ID']}) added to {owner_node['owner']}'s Pokedex.")

    """
    Prompt user for a Pokemon ID, find the data, and add to this owner's pokedex if not duplicate.
    """

def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    pass

def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    pass


########################
# 5) Sorting Owners by # of Pokemon
########################

def gather_all_owners(root, arr):
    """
    Collect all BST nodes into a list (arr).
    """
    pass

def sort_owners_by_num_pokemon():
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    pass


########################
# 6) Print All
########################

def print_all_owners():
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """
    pass

def pre_order_print(node):
    """
    Helper to print data in pre-order.
    """
    pass

def in_order_print(node):
    """
    Helper to print data in in-order.
    """
    pass

def post_order_print(node):
    """
    Helper to print data in post-order.
    """
    pass


########################
# 7) The Display Filter Sub-Menu
########################

def display_filter_sub_menu(owner_node):
    while True:
        print("-- Display Filter Menu --")
        print("1. Only a certain Type")
        print("2. Only Evolvable")
        print("3. Only Attack above __")
        print("4. Only HP above __")
        print("5. Only names starting with letter(s)")
        print("6. All of them!")
        print("7. Back")
        choice = int(input("Your choice: "))
        while choice < 1 and choice > 7:
            print ("Invalid input")
            choice = int(input("Your choice: "))
        if choice == 1:
            display_certain_type(owner_node)
        if choice == 2:
            display_evolvable(owner_node)
        if choice == 3:
            display_attack(owner_node)
        if choice == 4:
            pass
        if choice == 5:
            pass
        if choice == 6:
            pass
        if choice == 7:
            break




def display_certain_type(owner_node):
    if not owner_node['pokedex']:
        print("There are no Pokemons in this Pokedex that match the criteria.")
        return
    type = str(input("Which Type? (e.g. GRASS, WATER): ")).capitalize()
    for pokemon in owner_node['pokedex']:
        if pokemon['Type'] == type:
            print(pokemon)

def display_evolvable(owner_node):
    if not owner_node['pokedex']:
        print("There are no Pokemons in this Pokedex that match the criteria.")
        return
    for pokemon in owner_node['pokedex']:
        if pokemon['Can Evolve'] == "TRUE":
            print(pokemon)

def display_attack(owner_node):
    if not owner_node['pokedex']:
        print("There are no Pokemons in this Pokedex that match the criteria.")
        return
    attack = int(input("Enter Attack threshold: "))
    for pokemon in owner_node['pokedex']:
        if pokemon['Attack'] >= attack:
            print(pokemon)

def display_HP(owner_node):
    if not owner_node['pokedex']:
        print("There are no Pokemons in this Pokedex that match the criteria.")
        return
    HP = int(input("Enter HP threshold: "))
########################
# 8) Sub-menu & Main menu
########################

def existing_pokedex():
    global ownerRoot
    name = input("Owner name: ")
    owner_node = find_owner_bst(ownerRoot, name)
    if owner_node is None:
        print(f"Owner '{name}' not found.")
        return
    while True:
        print(f"-- {name}'s Pokedex Menu --")
        print("1. Add Pokemon")
        print("2. Display Pokedex")
        print("3. Release Pokemon")
        print("4. Evolve Pokemon")
        print("5. Back to Main")
        chice = int(input("Your choice: "))
        while chice < 1 or chice > 5:
            print ("Invalid input")
            chice = int(input("Your choice: "))
        if chice == 1:
            add_pokemon_to_owner(owner_node)
        if chice == 2:
            display_filter_sub_menu(owner_node)
def main_menu():
    while True:
        print("===Main Menu ===")
        print("1. New Pokedex")
        print("2. Existing Pokedex")
        print("3. Delete a Pokedex")
        print("4. Display owners by number of Pokemon")
        print("5. Print all")
        print("6. Exit")
        choice = int(input("Your choice: "))
        while choice < 1 or choice > 6:
            print ("Invalid input")
            choice = int(input("Your choice: "))
        if choice == 1:
            new_pokedex()
        elif choice == 2:
            existing_pokedex()



        elif choice == 6:
            print("Goodbye!")
            exit(0)

    """
    Main menu for:
    1) New Pokedex
    2) Existing Pokedex
    3) Delete a Pokedex
    4) Sort owners
    5) Print all
    6) Exit
    """
    pass

def main():
    print(HOENN_DATA)
    main_menu()
    """
    Entry point: calls main_menu().
    """
    pass

if __name__ == "__main__":
    main()
