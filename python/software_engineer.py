import sys
from .employee import Employee

class SoftwareEngineer(Employee):
    """
    Lớp biểu diễn Kỹ sư phần mềm kế thừa từ Employee, bổ sung ngôn ngữ chính và phụ cấp.
    """
    def __init__(self, id: str, full_name: str, primary_language: str, 
                 base_salary: float = 0.0, technical_allowance: float = 0.0):
        super().__init__(id=id, full_name=full_name, base_salary=base_salary)

        if not primary_language:
            print("[Cảnh báo] Ngôn ngữ lập trình chính không được để trống!", file=sys.stderr)
        if technical_allowance < 0:
            print("[Cảnh báo] Phụ cấp kỹ thuật không được âm! Tự động đặt về 0.", file=sys.stderr)
            technical_allowance = 0.0

        self._primary_language = primary_language
        self._technical_allowance = float(technical_allowance)

    def __del__(self):
        """Quan sát vòng đời đối tượng SoftwareEngineer."""
        print(f"  -> [Destructor SoftwareEngineer] Kỹ sư: {self._full_name} "
              f"(Mã: {self._id}, NN: {self._primary_language}) đã được giải phóng.")
        super().__del__()

    @property
    def primary_language(self) -> str:
        return self._primary_language

    @primary_language.setter
    def primary_language(self, value: str):
        if value and value.strip():
            self._primary_language = value.strip()
        else:
            print("[Lỗi] Ngôn ngữ lập trình chính không được để trống!", file=sys.stderr)

    @property
    def technical_allowance(self) -> float:
        return self._technical_allowance

    @technical_allowance.setter
    def technical_allowance(self, value: float):
        if value >= 0:
            self._technical_allowance = float(value)
        else:
            print("[Lỗi] Phụ cấp kỹ thuật không được âm!", file=sys.stderr)

    def calculate_monthly_cost(self) -> float:
        """Ghi đè: Tính tổng chi phí = Lương cơ bản + Phụ cấp kỹ thuật."""
        return self._base_salary + self._technical_allowance

    def display_info(self) -> None:
        """Ghi đè: Hiển thị đầy đủ thông tin kỹ sư phần mềm."""
        print(f"  [Kỹ sư PM ] Mã: {self._id:<8} | Họ tên: {self._full_name:<20} "
              f"| Lương CB: {self._base_salary:>10,.0f} VND | NN: {self._primary_language:<8} "
              f"| Phụ cấp: {self._technical_allowance:>9,.0f} VND | Chi phí tháng: {self.calculate_monthly_cost():>10,.0f} VND")
