import sys

class Employee:
    """
    Lớp biểu diễn Nhân sự thông thường trong hệ thống.
    """
    def __init__(self, id: str = "UNKNOWN", full_name: str = "Unnamed employee", base_salary: float = 0.0):
        # Kiểm tra ràng buộc
        if not id:
            print("[Cảnh báo] Mã nhân sự không được để trống!", file=sys.stderr)
        if not full_name:
            print("[Cảnh báo] Họ tên nhân sự không được để trống!", file=sys.stderr)
        if base_salary < 0:
            print("[Cảnh báo] Lương cơ bản không được âm! Tự động đặt về 0.", file=sys.stderr)
            base_salary = 0.0

        self._id = id
        self._full_name = full_name
        self._base_salary = float(base_salary)

    def __del__(self):
        """Quan sát vòng đời đối tượng Employee."""
        print(f"  -> [Destructor Employee] Nhân sự: {self._full_name} (Mã: {self._id}) đã được giải phóng.")

    # Getters & Setters
    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        if value and value.strip():
            self._id = value.strip()
        else:
            print("[Lỗi] Mã nhân sự không được để trống!", file=sys.stderr)

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str):
        if value and value.strip():
            self._full_name = value.strip()
        else:
            print("[Lỗi] Họ tên không được để trống!", file=sys.stderr)

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value >= 0:
            self._base_salary = float(value)
        else:
            print("[Lỗi] Lương cơ bản không được âm!", file=sys.stderr)

    def increase_salary(self, value: float, by_percentage: bool = False) -> None:
        """
        Nạp chồng tính năng tăng lương:
        - Nếu by_percentage == False: Tăng một số tiền cố định (value > 0).
        - Nếu by_percentage == True: Tăng theo tỷ lệ phần trăm (value > 0).
        """
        if value <= 0:
            print(f"[Lỗi] Giá trị tăng lương ({value}) phải là số dương (> 0)!", file=sys.stderr)
            return

        if by_percentage:
            increase_amount = self._base_salary * (value / 100.0)
            self._base_salary += increase_amount
            print(f"[Thành công] Tăng lương {value}% (+{increase_amount:,.0f} VND) cho {self._full_name}. "
                  f"Lương mới: {self._base_salary:,.0f} VND")
        else:
            self._base_salary += value
            print(f"[Thành công] Tăng lương cố định +{value:,.0f} VND cho {self._full_name}. "
                  f"Lương mới: {self._base_salary:,.0f} VND")

    def calculate_monthly_cost(self) -> float:
        """Phương thức đa hình tính chi phí hàng tháng (mặc định bằng lương cơ bản)."""
        return self._base_salary

    def display_info(self) -> None:
        """Phương thức đa hình hiển thị thông tin nhân sự."""
        print(f"  [Nhân viên] Mã: {self._id:<8} | Họ tên: {self._full_name:<20} "
              f"| Lương CB: {self._base_salary:>12,.0f} VND | Chi phí tháng: {self.calculate_monthly_cost():>12,.0f} VND")
