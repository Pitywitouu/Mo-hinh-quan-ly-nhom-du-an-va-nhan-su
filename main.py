"""
Mã sinh viên: 202418985
Họ tên: Nguyễn Phú Thái
"""
"""
Chương trình kiểm thử mô hình Quản lý Nhóm dự án và Nhân sự bằng Python.
"""
import sys
import io

# Đảm bảo in tiếng Việt Unicode trên Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from python.employee import Employee
from python.software_engineer import SoftwareEngineer
from python.project_team import ProjectTeam

def print_step(step_num: int, title: str):
    print("\n" + "-" * 85)
    print(f">>> [KỊCH BẢN KIỂM THỬ - BƯỚC {step_num}]: {title}")
    print("-" * 85)

def main():
    print("=" * 85)
    print("      CHƯƠNG TRÌNH KIỂM THỬ MÔ HÌNH QUẢN LÝ NHÓM DỰ ÁN VÀ NHÂN SỰ      ")
    print("=" * 85)

    # -------------------------------------------------------------------------
    # Bước 1: Tạo hai Employee bằng hai constructor khác nhau
    # -------------------------------------------------------------------------
    print_step(1, "Tạo 2 Employee bằng 2 constructor khác nhau")
    emp1 = Employee(id="EMP01", full_name="Trần Thụy An")  # Constructor 2 tham số (lương mặc định 0)
    emp1.base_salary = 12_000_000                           # Thiết lập lương cơ bản hợp lệ

    emp2 = Employee(id="EMP02", full_name="Nguyễn Thị Bích Ngọc", base_salary=15_000_000) # Constructor 3 tham số

    print("Kết quả khởi tạo Employee:")
    emp1.display_info()
    emp2.display_info()

    # -------------------------------------------------------------------------
    # Bước 2: Tạo hai SoftwareEngineer bằng hai constructor khác nhau
    # -------------------------------------------------------------------------
    print_step(2, "Tạo 2 SoftwareEngineer bằng 2 constructor khác nhau")
    se1 = SoftwareEngineer(id="SE01", full_name="Lê Văn Cường", primary_language="C++") # Constructor 3 tham số
    se1.base_salary = 18_000_000
    se1.technical_allowance = 4_000_000

    se2 = SoftwareEngineer(id="SE02", full_name="Phạm Minh Đức", primary_language="Python",
                           base_salary=22_000_000, technical_allowance=5_000_000) # Constructor 5 tham số

    print("Kết quả khởi tạo SoftwareEngineer:")
    se1.display_info()
    se2.display_info()

    # -------------------------------------------------------------------------
    # Bước 3: Tăng lương một nhân sự bằng số tiền cố định
    # -------------------------------------------------------------------------
    print_step(3, "Tăng lương một nhân sự (emp1) bằng số tiền cố định (+2,000,000 VND)")
    print("Trước khi tăng: ", end="")
    emp1.display_info()
    emp1.increase_salary(2_000_000)
    print("Sau khi tăng  : ", end="")
    emp1.display_info()

    # -------------------------------------------------------------------------
    # Bước 4: Tăng lương một nhân sự khác theo phần trăm
    # -------------------------------------------------------------------------
    print_step(4, "Tăng lương một nhân sự khác (se2) theo phần trăm (+10%)")
    print("Trước khi tăng: ", end="")
    se2.display_info()
    se2.increase_salary(10.0, by_percentage=True)
    print("Sau khi tăng  : ", end="")
    se2.display_info()

    # -------------------------------------------------------------------------
    # Bước 5: Tạo nhóm dự án không có trưởng nhóm
    # -------------------------------------------------------------------------
    print_step(5, "Tạo nhóm dự án không có trưởng nhóm")
    team_alpha = ProjectTeam(project_code="PRJ_ALPHA", project_name="Hệ Thống Ngân Hàng Số")

    # -------------------------------------------------------------------------
    # Bước 6: Thêm một nhân sự vào nhóm bằng add_member(employee)
    # -------------------------------------------------------------------------
    print_step(6, "Thêm một nhân sự (emp1) vào nhóm bằng add_member(employee)")
    team_alpha.add_member(emp1)

    # -------------------------------------------------------------------------
    # Bước 7: Thêm một kỹ sư bằng add_member(employee, True) để đặt làm trưởng nhóm
    # -------------------------------------------------------------------------
    print_step(7, "Thêm kỹ sư (se2) bằng add_member(employee, True) để đặt làm trưởng nhóm")
    team_alpha.add_member(se2, make_leader=True)

    # Thêm thành viên khác vào nhóm
    team_alpha.add_member(se1)

    # -------------------------------------------------------------------------
    # Bước 8: Thử thêm lại một thành viên đã tồn tại
    # -------------------------------------------------------------------------
    print_step(8, "Thử thêm lại một thành viên đã tồn tại trong nhóm (emp1)")
    add_duplicate_res = team_alpha.add_member(emp1)
    print(f"Kết quả thêm trùng: {'Thành công' if add_duplicate_res else 'Bị từ chối (Đúng quy tắc bất biến)'}")

    # -------------------------------------------------------------------------
    # Bước 9: Hiển thị danh sách bằng lời gọi đa hình
    # -------------------------------------------------------------------------
    print_step(9, "Hiển thị danh sách bằng lời gọi đa hình (display_team -> display_info)")
    team_alpha.display_team()

    # -------------------------------------------------------------------------
    # Bước 10: Tính tổng chi phí nhân sự hằng tháng
    # -------------------------------------------------------------------------
    print_step(10, "Tính tổng chi phí nhân sự hằng tháng (Đa hình calculate_monthly_cost)")
    total_cost = team_alpha.calculate_total_monthly_cost()
    print(f"Tổng chi phí nhân sự hàng tháng của Team Alpha: {total_cost:,.0f} VND")

    # -------------------------------------------------------------------------
    # Bước 11: Thử xóa trưởng nhóm hiện tại và kiểm tra thao tác bị từ chối
    # -------------------------------------------------------------------------
    print_step(11, "Thử xóa trưởng nhóm hiện tại (se2 - SE02) và kiểm tra thao tác bị từ chối")
    remove_leader_res = team_alpha.remove_member(se2.id)
    print(f"Kết quả xóa trưởng nhóm khi chưa có người thay thế: "
          f"{'Xóa thành công (Lỗi quy tắc!)' if remove_leader_res else 'Bị từ chối (Đúng ràng buộc)'}")

    # -------------------------------------------------------------------------
    # Bước 12: Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm
    # -------------------------------------------------------------------------
    print_step(12, "Đổi trưởng nhóm sang se1 (SE01) rồi xóa người từng là trưởng nhóm (se2)")
    print("1. Đổi trưởng nhóm sang se1:")
    team_alpha.change_leader(se1)

    print("\n2. Thực hiện xóa se2 (SE02) - hiện tại đã không còn là trưởng nhóm:")
    remove_old_leader_res = team_alpha.remove_member(se2.id)
    print(f"Kết quả xóa người từng là trưởng nhóm: {'Thành công' if remove_old_leader_res else 'Thất bại'}")

    print("\nDanh sách nhóm Alpha sau khi đổi trưởng nhóm và xóa se2:")
    team_alpha.display_team()

    # -------------------------------------------------------------------------
    # Bước 13: Tạo một nhóm thứ hai và thêm một nhân sự đã có ở nhóm thứ nhất
    #          (Chứng minh quan hệ kết tập nhiều nhóm)
    # -------------------------------------------------------------------------
    print_step(13, "Tạo nhóm thứ hai và thêm emp1 (đã có ở Alpha) để chứng minh kết tập nhiều nhóm")
    def create_and_destroy_temporary_team():
        # ---------------------------------------------------------------------
        # Bước 14: Hủy nhóm thứ hai bằng cách kết thúc một khối hàm/lệnh cục bộ
        # ---------------------------------------------------------------------
        print_step(14, "Khởi tạo Team Beta trong hàm cục bộ và thêm emp1, emp2")
        team_beta = ProjectTeam(project_code="PRJ_BETA", project_name="Ứng Dụng E-Commerce", leader=emp2)
        team_beta.add_member(emp1) # emp1 tham gia đồng thời cả Alpha và Beta

        print("Thông tin Team Beta trong phạm vi hàm cục bộ:")
        team_beta.display_team()
        print("-> Kết thúc hàm cục bộ, team_beta ra khỏi scope...")
        # Khi kết thúc hàm cục bộ, team_beta được giải phóng

    create_and_destroy_temporary_team()

    # -------------------------------------------------------------------------
    # Bước 15: Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại sau khi nhóm bị hủy
    # -------------------------------------------------------------------------
    print_step(15, "Chứng minh nhân sự của nhóm thứ hai (emp1, emp2) vẫn tồn tại sau khi Beta bị hủy")
    print("Nhân sự emp1: ", end="")
    emp1.display_info()
    print("Nhân sự emp2: ", end="")
    emp2.display_info()

    print("\nNhóm Alpha vẫn hoạt động nguyên vẹn với nhân sự emp1:")
    team_alpha.display_team()

    # -------------------------------------------------------------------------
    # Kiểm tra các trường hợp biên (Edge Cases)
    # -------------------------------------------------------------------------
    print_step(16, "Kiểm tra các trường hợp biên (Edge Cases & Invariants)")
    print("a. Thử tăng lương với giá trị <= 0:")
    emp1.increase_salary(-500_000)
    emp1.increase_salary(0, by_percentage=True)

    print("\nb. Thử xóa nhân sự không tồn tại trong nhóm:")
    team_alpha.remove_member("NON_EXISTENT_ID")

    print("\nc. Đổi trưởng nhóm sang một nhân sự chưa có trong nhóm (emp2):")
    team_alpha.change_leader(emp2)
    team_alpha.display_team()

    print("\n" + "=" * 85)
    print("                      KẾT THÚC CHƯƠNG TRÌNH KIỂM THỬ                         ")
    print("=" * 85)

if __name__ == "__main__":
    main()
