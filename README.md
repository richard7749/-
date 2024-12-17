import json
import os

# 儲存顧客資料的檔案
CUSTOMER_FILE = "customers.json"
# 儲存原物料資料的檔案
MATERIAL_FILE = "materials.json"

# 讀取顧客資料
def load_customers():
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# 儲存顧客資料
def save_customers(customers):
    with open(CUSTOMER_FILE, "w") as file:
        json.dump(customers, file, indent=4)

# 讀取原物料資料
def load_materials():
    if os.path.exists(MATERIAL_FILE):
        with open(MATERIAL_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# 儲存原物料資料
def save_materials(materials):
    with open(MATERIAL_FILE, "w") as file:
        json.dump(materials, file, indent=4)

# 新增顧客
def add_customer(name, phone, email, address):
    customers = load_customers()
    customer_id = len(customers) + 1
    customers.append({
        "id": customer_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_customers(customers)

# 查詢顧客
def get_customers():
    return load_customers()

# 更新顧客資料
def update_customer(customer_id, name, phone, email, address):
    customers = load_customers()
    for customer in customers:
        if customer["id"] == customer_id:
            customer["name"] = name
            customer["phone"] = phone
            customer["email"] = email
            customer["address"] = address
            save_customers(customers)
            return True
    return False

# 刪除顧客
def delete_customer(customer_id):
    customers = load_customers()
    customers = [customer for customer in customers if customer["id"] != customer_id]
    save_customers(customers)

# 新增原物料
def add_material(name, quantity, price):
    materials = load_materials()
    material_id = len(materials) + 1
    materials.append({
        "id": material_id,
        "name": name,
        "quantity": quantity,
        "price": price
    })
    save_materials(materials)

# 查詢原物料
def get_materials():
    return load_materials()

# 更新原物料資料
def update_material(material_id, name, quantity, price):
    materials = load_materials()
    for material in materials:
        if material["id"] == material_id:
            material["name"] = name
            material["quantity"] = quantity
            material["price"] = price
            save_materials(materials)
            return True
    return False

# 刪除原物料
def delete_material(material_id):
    materials = load_materials()
    materials = [material for material in materials if material["id"] != material_id]
    save_materials(materials)

# 顯示顧客資料
def show_customers():
    customers = get_customers()
    print("顧客資料:")
    for customer in customers:
        print(f"ID: {customer['id']}, 姓名: {customer['name']}, 電話: {customer['phone']}, 郵件: {customer['email']}, 地址: {customer['address']}")

# 顯示原物料資料
def show_materials():
    materials = get_materials()
    print("原物料資料:")
    for material in materials:
        print(f"ID: {material['id']}, 名稱: {material['name']}, 數量: {material['quantity']}, 價格: {material['price']}")

# 主程式
def main():
    while True:
        print("\n1. 新增顧客")
        print("2. 顯示顧客資料")
        print("3. 更新顧客資料")
        print("4. 刪除顧客")
        print("5. 新增原物料")
        print("6. 顯示原物料資料")
        print("7. 更新原物料資料")
        print("8. 刪除原物料")
        print("9. 離開")
        
        choice = input("選擇操作: ")

        if choice == '1':
            name = input("顧客姓名: ")
            phone = input("顧客電話: ")
            email = input("顧客郵件: ")
            address = input("顧客地址: ")
            add_customer(name, phone, email, address)
        
        elif choice == '2':
            show_customers()
        
        elif choice == '3':
            customer_id = int(input("輸入顧客ID: "))
            name = input("新姓名: ")
            phone = input("新電話: ")
            email = input("新郵件: ")
            address = input("新地址: ")
            if not update_customer(customer_id, name, phone, email, address):
                print("顧客ID不存在！")
        
        elif choice == '4':
            customer_id = int(input("輸入顧客ID: "))
            delete_customer(customer_id)
        
        elif choice == '5':
            name = input("原物料名稱: ")
            quantity = int(input("原物料數量: "))
            price = float(input("原物料價格: "))
            add_material(name, quantity, price)
        
        elif choice == '6':
            show_materials()
        
        elif choice == '7':
            material_id = int(input("輸入原物料ID: "))
            name = input("新名稱: ")
            quantity = int(input("新數量: "))
            price = float(input("新價格: "))
            if not update_material(material_id, name, quantity, price):
                print("原物料ID不存在！")
        
        elif choice == '8':
            material_id = int(input("輸入原物料ID: "))
            delete_material(material_id)
        
        elif choice == '9':
            print("感謝使用！")
            break

if __name__ == '__main__':
    main()
