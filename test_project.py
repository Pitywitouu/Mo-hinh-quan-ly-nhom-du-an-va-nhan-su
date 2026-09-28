"""
Bộ Unit Test tự động kiểm tra toàn bộ các nghiệp vụ và bất biến của mô hình.
"""
import sys
import io

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import unittest
from python.employee import Employee
from python.software_engineer import SoftwareEngineer
from python.project_team import ProjectTeam

class TestEmployee(unittest.TestCase):
    def test_default_constructor(self):
        emp = Employee()
        self.assertEqual(emp.id, "UNKNOWN")
        self.assertEqual(emp.full_name, "Unnamed employee")
        self.assertEqual(emp.base_salary, 0.0)
        self.assertEqual(emp.calculate_monthly_cost(), 0.0)

    def test_parameterized_constructor(self):
        emp = Employee("E01", "Nguyen Van A", 10000000)
        self.assertEqual(emp.id, "E01")
        self.assertEqual(emp.full_name, "Nguyen Van A")
        self.assertEqual(emp.base_salary, 10000000)
        self.assertEqual(emp.calculate_monthly_cost(), 10000000)

    def test_increase_salary_fixed(self):
        emp = Employee("E01", "Nguyen Van A", 10000000)
        emp.increase_salary(2000000)
        self.assertEqual(emp.base_salary, 12000000)

    def test_increase_salary_percentage(self):
        emp = Employee("E01", "Nguyen Van A", 10000000)
        emp.increase_salary(10, by_percentage=True)
        self.assertEqual(emp.base_salary, 11000000)

    def test_increase_salary_invalid_value(self):
        emp = Employee("E01", "Nguyen Van A", 10000000)
        emp.increase_salary(-500000)
        self.assertEqual(emp.base_salary, 10000000) # Lương không đổi


class TestSoftwareEngineer(unittest.TestCase):
    def test_software_engineer_cost(self):
        se = SoftwareEngineer("SE01", "Le Van C", "Python", base_salary=20000000, technical_allowance=5000000)
        self.assertEqual(se.primary_language, "Python")
        self.assertEqual(se.technical_allowance, 5000000)
        # Kiểm tra đa hình: Chi phí tháng = Lương CB + Phụ cấp
        self.assertEqual(se.calculate_monthly_cost(), 25000000)


class TestProjectTeam(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("E01", "Nguyen Van A", 10000000)
        self.emp2 = Employee("E02", "Tran Thi B", 12000000)
        self.se1 = SoftwareEngineer("SE01", "Le Van C", "C++", base_salary=20000000, technical_allowance=4000000)

    def test_team_creation_without_leader(self):
        team = ProjectTeam("PRJ01", "Project Alpha")
        self.assertIsNone(team.leader)
        self.assertEqual(len(team.members), 0)

    def test_team_creation_with_leader(self):
        team = ProjectTeam("PRJ01", "Project Alpha", leader=self.emp1)
        self.assertEqual(team.leader, self.emp1)
        self.assertEqual(len(team.members), 1)
        self.assertTrue(team.contains("E01"))

    def test_prevent_duplicate_members(self):
        team = ProjectTeam("PRJ01", "Project Alpha")
        self.assertTrue(team.add_member(self.emp1))
        self.assertFalse(team.add_member(self.emp1)) # Không được trùng
        self.assertEqual(len(team.members), 1)

    def test_add_member_make_leader(self):
        team = ProjectTeam("PRJ01", "Project Alpha")
        team.add_member(self.emp1)
        team.add_member(self.se1, make_leader=True)
        self.assertEqual(team.leader, self.se1)
        self.assertEqual(len(team.members), 2)

    def test_cannot_remove_leader_directly(self):
        team = ProjectTeam("PRJ01", "Project Alpha", leader=self.emp1)
        # Ràng buộc: Không thể xóa trưởng nhóm khi chưa chọn trưởng nhóm thay thế
        self.assertFalse(team.remove_member("E01"))
        self.assertEqual(len(team.members), 1)

    def test_change_leader_and_remove_old_leader(self):
        team = ProjectTeam("PRJ01", "Project Alpha", leader=self.emp1)
        team.add_member(self.emp2)
        # Đổi leader sang emp2
        self.assertTrue(team.change_leader(self.emp2))
        self.assertEqual(team.leader, self.emp2)
        # Giờ đã có thể xóa emp1
        self.assertTrue(team.remove_member("E01"))
        self.assertFalse(team.contains("E01"))
        self.assertEqual(len(team.members), 1)

    def test_polymorphic_total_cost(self):
        team = ProjectTeam("PRJ01", "Project Alpha")
        team.add_member(self.emp1) # Cost = 10,000,000
        team.add_member(self.se1)  # Cost = 24,000,000 (20M + 4M)
        self.assertEqual(team.calculate_total_monthly_cost(), 34000000)

    def test_aggregation_member_in_multiple_teams(self):
        team1 = ProjectTeam("PRJ01", "Project Alpha")
        team2 = ProjectTeam("PRJ02", "Project Beta")
        team1.add_member(self.emp1)
        team2.add_member(self.emp1)
        self.assertTrue(team1.contains("E01"))
        self.assertTrue(team2.contains("E01"))

if __name__ == "__main__":
    unittest.main()
