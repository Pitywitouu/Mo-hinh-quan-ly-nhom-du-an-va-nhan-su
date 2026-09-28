import sys
from typing import List, Optional
from .employee import Employee

class ProjectTeam:
    """
    Lớp quản lý Nhóm dự án theo quan hệ kết tập (Aggregation) với Employee.
    Duy trì liên kết không sở hữu tới trưởng nhóm và danh sách thành viên.
    """
    def __init__(self, project_code: str, project_name: str, leader: Optional[Employee] = None):
        self._project_code = project_code
        self._project_name = project_name
        self._leader: Optional[Employee] = leader
        self._members: List[Employee] = []

        if leader is not None:
            self._members.append(leader)
            print(f"[ProjectTeam] Khởi tạo dự án [{self._project_code}] '{self._project_name}' "
                  f"với trưởng nhóm: {leader.full_name} ({leader.id}).")
        else:
            print(f"[ProjectTeam] Khởi tạo dự án [{self._project_code}] '{self._project_name}' (Chưa có trưởng nhóm).")

    def __del__(self):
        """Destructor: Chỉ giải phóng liên kết nội bộ, các Employee vẫn được bảo toàn."""
        print(f"  -> [Destructor ProjectTeam] Dự án [{self._project_code}] '{self._project_name}' bị hủy "
              f"(Giải phóng liên kết, các nhân sự độc lập vẫn tồn tại).")
        self._members.clear()
        self._leader = None

    @property
    def project_code(self) -> str:
        return self._project_code

    @property
    def project_name(self) -> str:
        return self._project_name

    @property
    def leader(self) -> Optional[Employee]:
        return self._leader

    @property
    def members(self) -> List[Employee]:
        return self._members

    def contains(self, employee_id: str) -> bool:
        """Kiểm tra sự tồn tại của nhân sự trong nhóm theo mã id."""
        return any(member.id == employee_id for member in self._members)

    def add_member(self, employee: Employee, make_leader: bool = False) -> bool:
        """
        Nạp chồng thêm thành viên:
        - Không thêm trùng nhân sự.
        - Nếu make_leader == True, nhân sự được thêm (nếu chưa có) và trở thành trưởng nhóm.
        - Trưởng nhóm cũ vẫn là thành viên trong nhóm.
        """
        if self.contains(employee.id):
            if not make_leader:
                print(f"[Từ chối] Nhân sự {employee.full_name} ({employee.id}) đã tồn tại trong dự án [{self._project_code}]!", 
                      file=sys.stderr)
                return False
        else:
            self._members.append(employee)
            print(f"[Thành công] Đã thêm nhân sự {employee.full_name} ({employee.id}) vào dự án [{self._project_code}].")

        if make_leader:
            self._leader = employee
            print(f"[Thành công] Đã chỉ định {employee.full_name} ({employee.id}) làm TRƯỞNG NHÓM dự án [{self._project_code}].")

        return True

    def remove_member(self, employee_id: str) -> bool:
        """
        Xóa nhân sự khỏi nhóm theo mã.
        Ràng buộc: Không được xóa trưởng nhóm khi chưa chọn trưởng nhóm thay thế!
        """
        if self._leader is not None and self._leader.id == employee_id:
            print(f"[Từ chối] Không thể xóa {self._leader.full_name} ({employee_id}) vì đang là TRƯỞNG NHÓM! "
                  f"Hãy đổi trưởng nhóm trước khi xóa.", file=sys.stderr)
            return False

        for i, member in enumerate(self._members):
            if member.id == employee_id:
                removed_name = member.full_name
                self._members.pop(i)
                print(f"[Thành công] Đã xóa nhân sự {removed_name} ({employee_id}) khỏi dự án [{self._project_code}].")
                return True

        print(f"[Từ chối] Không tìm thấy nhân sự có mã {employee_id} trong dự án [{self._project_code}] để xóa.", 
              file=sys.stderr)
        return False

    def change_leader(self, employee: Employee) -> bool:
        """
        Thay đổi trưởng nhóm:
        Ràng buộc: Trưởng nhóm mới phải được thêm vào nhóm nếu chưa phải thành viên.
        """
        if not self.contains(employee.id):
            self._members.append(employee)
            print(f"[Thông tin] Trưởng nhóm mới chưa có trong nhóm, đã tự động thêm "
                  f"{employee.full_name} ({employee.id}) vào danh sách thành viên.")

        self._leader = employee
        print(f"[Thành công] Đã đổi trưởng nhóm sang: {employee.full_name} ({employee.id}) "
              f"cho dự án [{self._project_code}].")
        return True

    def calculate_total_monthly_cost(self) -> float:
        """Tính tổng chi phí nhân sự hàng tháng bằng lời gọi đa hình calculate_monthly_cost()."""
        return sum(member.calculate_monthly_cost() for member in self._members)

    def display_team(self) -> None:
        """Hiển thị toàn bộ thông tin dự án, trưởng nhóm và danh sách thành viên."""
        print("\n" + "=" * 95)
        print(f" THÔNG TIN DỰ ÁN: [{self._project_code}] {self._project_name}")
        leader_info = f"{self._leader.full_name} (Mã: {self._leader.id})" if self._leader else "[Chưa có]"
        print(f" Trưởng nhóm: {leader_info}")
        print(f" Số lượng thành viên: {len(self._members)}")
        print("-" * 95)
        print(" DANH SÁCH THÀNH VIÊN TRONG DỰ ÁN (Lời gọi đa hình display_info):")
        for i, member in enumerate(self._members, start=1):
            print(f" {i:<2}.", end="")
            member.display_info()
        print("-" * 95)
        print(f" -> TỔNG CHI PHÍ NHÂN SỰ HÀNG THÁNG: {self.calculate_total_monthly_cost():>15,.0f} VND")
        print("=" * 95 + "\n")
