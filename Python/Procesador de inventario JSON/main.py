import os
import json

def load_json(PATH_NAME):
    """Carga el archivo JSON. Si el archivo no existe entonces devuelve una libreria vacia"""
    if os.path.exists(PATH_NAME):
        try:
            with open(PATH_NAME, 'r', encoding='utf-8') as f:
                inventory = json.load(f)
                return inventory
        except json.JSONDecodeError as e:
            print(f"Error: Archivo JSON malformado. \nDetalle: {e}")
            return
        except Exception as e:
            print(f"Error: El JSON no se pudo cargar correctamente. \nDetalle: {e}")
            return
    else:
        return { }

def add_json(PATH_NAME, inventory):
    """Para agregar nuevos items al inventario al archivo JSON"""
    item = input("Agrega un item: ").strip()

    if not item:
        print("Error Agrega un item, no puedes continuar sin ninguno")
        return
    
    try:
        quantity = int(input("Agrega la cantidad del Item: "))
        if quantity < 0:
            print("La cantidad no puede ser negativa")
            return
        state = input("Ahora agrega la disponibilidad: ").strip()

        if state.lower() in ["disponible", "available", "in stock", "stock"]:
            state = True
            print(state)
        elif state.lower() in ["agotado", "no disponible", "out", "out of stock"]:
            state = False
            print(state)
        else:
            print("Por favor ingresa un valor valido. El valor debe ser: disponible o agotado, no puede ser ni numero, ni otra cosa")
            return
    except AttributeError as e:
        print("Por favor ingresa un numero")
        return
    except Exception as e:
        print(f"❌ Oopss. Ha ocurrido un error.\nDetalles: {e}")
        return
    
    if item in inventory:
        print(f"Estas editando un item ya existente: {item}")
        inventory[item]['cantidad'] = quantity
        inventory[item]['disponibilidad'] = state
    else:
        print(f"Estas en un nuevo item: {item}")
        inventory[item] = {'cantidad': quantity, 'disponibilidad': state}
    
    save_json(PATH_NAME, inventory)

def save_json(PATH_NAME, inventory):
    """Crea el archivo JSON para guardar la informacion"""
    try:
        with open(PATH_NAME, 'w') as f:
            json.dump(inventory, f, indent=4)
    except Exception as e:
        print(f"❌ Oopss. Ha ocurrido un error.\nDetalles: {e}")

def view_json(inventory):
    """Muestra el inventario actual."""
    if not inventory:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario Actual ---")
    for item, details in inventory.items():
        print(f"Artículo: {item}")
        print(f"  Cantidad: {details.get('cantidad', 'N/A')}")
        print(f"  Estado: {details.get('estado', 'N/A')}")
        print("-" * 20)
    print("-------------------------\n")
    

def main():
    PATH_NAME = input("Selecciona el nombre de tu inventario: ").strip() #You need to add .json
    inventory = load_json(PATH_NAME)
    while True:
        os.system("cls")
        print("-" * 50 + "\n\t\t\tWelcome\n" + "-" * 50)
        print("--- Menu Inventario---")
        print("1. Agrega/Crea un nuevo inventario")
        print("2. Ver inventario")
        print("3. Exit")
            
        userInput = input("Tu: ").strip()
        if userInput == "1":
            add_json(PATH_NAME, inventory)
        if userInput == "2":
            view_json(inventory)
            input()
        if userInput.lower() in ["3", "exit", "bye", "quit", "stop", "salir", "parar"]:
            break

if __name__ == "__main__":
    main()