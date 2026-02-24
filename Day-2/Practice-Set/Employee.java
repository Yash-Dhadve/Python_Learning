// Create an Employee class with name and salary using constructor.

public class Employee {
    String name;
    int salary;

    Employee(){
        name = "Unknown";
        salary = 0;
    }

    public static void main(String[] args) {
        Employee e0 = new Employee();

        System.out.println("Name: " + e0.name);
        System.out.println("Salary: " + e0.salary);
    }
}
