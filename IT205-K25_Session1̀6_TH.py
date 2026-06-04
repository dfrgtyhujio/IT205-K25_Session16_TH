blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def get_blood_code(record):
    parts = record.split("-")
    return parts[0]


def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print("--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("-" * 65)

    total_volume = 0

    for item in inventory:
        parts = item.split("-")

        blood_code = parts[0]
        donor_name = parts[1]

        if parts[3].isdigit():
            blood_group = parts[2]
            volume = parts[3]
            expiry_date = parts[4]
        else:
            blood_group = parts[2] + "-" + parts[3]
            volume = parts[4]
            expiry_date = parts[5]

        total_volume += int(volume)

        print(f"{blood_code} | {donor_name} | {blood_group} | {volume} ml | {expiry_date}")

    print("-" * 65)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_code = input("Nhập mã túi máu mới: ").strip().upper()

    if blood_code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    for item in inventory:
        if get_blood_code(item) == blood_code:
            print(f"Lỗi: Mã túi máu {blood_code} đã tồn tại! Vui lòng nhập mã khác.")
            return

    donor_name = " ".join(input("Nhập tên người hiến: ").strip().split()).title()

    if donor_name == "":
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit() or int(volume) <= 0:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry_date = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_record = "-".join([
        blood_code,
        donor_name,
        blood_group,
        volume,
        expiry_date
    ])

    inventory.append(new_record)

    print(f"\nThành công: Đã nhập túi máu {blood_code} vào kho!")


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_code = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if blood_code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):
        parts = inventory[index].split("-")

        if parts[0] == blood_code:
            new_expiry = input("Nhập ngày hết hạn mới: ").strip()

            parts[-1] = new_expiry

            inventory[index] = "-".join(parts)

            print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {blood_code}!")
            return

    print(f"Lỗi: Không tìm thấy túi máu {blood_code} trong kho!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_code = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if blood_code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    for index in range(len(inventory)):
        parts = inventory[index].split("-")

        if parts[0] == blood_code:
            inventory.pop(index)

            print(f"\nThành công: Đã xuất túi máu {blood_code} khỏi kho!")
            return

    print(f"Lỗi: Không tìm thấy túi máu {blood_code} trong kho!")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)

        elif choice == "2":
            add_blood_bag(blood_inventory)

        elif choice == "3":
            update_expiry(blood_inventory)

        elif choice == "4":
            remove_blood_bag(blood_inventory)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()