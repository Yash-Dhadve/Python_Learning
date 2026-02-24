// Create a Car class with brand and price.
// Create 2 objects with different data.

public class Car {
    String brand;
    int price;

    Car(){
        brand = "Unkown";
        price = 0;
    }

    public static void main(String[] args) {
        Car c1 = new Car();
        Car c2 = new Car();

        c1.brand = "BMW";
        c1.price = 5000000;

        c2.brand = "Toyota";
        c2.price = 40000000;

        System.out.println("Brand: " + c1.brand);
        System.out.println("Price: " + c1.price + "\n");
        
        System.out.println("Brand: " + c2.brand);
        System.out.println("Price: " + c2.price);
    }
}
