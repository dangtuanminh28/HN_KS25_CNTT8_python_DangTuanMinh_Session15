inventory_stock = 100
total_revenue = 0.0

def calculate_final_price(quantity, price):
    raw_total = quantity * price
    discount = 0.0
    
    if raw_total >= 1000:
        discount = raw_total * 0.10
        
    total_after_discount = raw_total - discount
    tax_vat = total_after_discount * 0.08
    final_total = total_after_discount + tax_vat
    
    return final_total, raw_total, discount, tax_vat



def handle_add_stock():
    """Chức năng 1: Nhập thêm hàng vào kho"""
    global inventory_stock
    print("--- NHẬP HÀNG ---")
    stock_input = input("Nhập số lượng sản phẩm muốn thêm: ").strip()
    
    if stock_input == "":
        print("Dữ liệu nhập vào phải lớn hơn 0")
        return
    if not stock_input.isdigit():
        print("Dữ liệu nhập vào phải lớn hơn 0")
        return
        
    amount = int(stock_input)
    if amount <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0")
        return
        
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def handle_sale():
    """Chức năng 2: Bán hàng"""
    global inventory_stock, total_revenue
    print("--- BÁN HÀNG ---")
    qty_input = input("Nhập số lượng mua: ").strip()
    if qty_input == "" or not qty_input.isdigit():
        print("Dữ liệu nhập vào phải lớn hơn 0!")
        return
        
    quantity = int(qty_input)
    if quantity <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0!")
        return
        
    if quantity > inventory_stock:
        print(f"Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return
        
    price_input = input("Nhập đơn giá ($): ").strip()
    if price_input == "":
        print("Giá đơn không được trống!")
        return
    try:
        price = float(price_input)
        if price <= 0:
            print("Giá đơn phải lớn hơn 0!")
            return
    except ValueError:
        print("Giá đơn phải lớn hơn 0!")
        return
        
    final_total, raw_total, discount, tax_vat = calculate_final_price(quantity, price)
    
    inventory_stock -= quantity
    total_revenue += final_total
    
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price}")
    print(f"Tạm tính: ${raw_total}")
    print(f"Giảm giá (10%): ${discount}")
    print(f"Thuế VAT (8%): ${tax_vat}")
    print(f"Tổng thanh toán: ${final_total}")
    print("Đã bán thành công!")



def handle_report():
    """Chức năng 3: Xem báo cáo tổng quan tình hình kinh doanh."""
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")

while True:
    print("""
==== TECHSTORE MANAGEMENT SYSTEM ====
1. Nhập thêm hàng vào kho
2. Bán hàng (tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
""")
    choice = input("Nhập lựa chọn (1-4): ").strip()
    
    if choice == '1':
        handle_add_stock()
    elif choice == '2':
        handle_sale()
    elif choice == '3':
        handle_report()
    elif choice == '4':
        print("Thoát chương trình")
        break
    else:
        print("Vui lòng nhập lại(1-4)!")