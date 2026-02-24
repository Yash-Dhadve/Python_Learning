// Create a BankAccount class with accountHolder and balance.
// Print details.

public class BankAccount {
    String accountHolder;
    int balance;

    BankAccount(){
        accountHolder = "Unkown";
        balance = 0;
    }

    public static void main(String[] args) {
        BankAccount c1 = new BankAccount();
        BankAccount c2 = new BankAccount();

        c1.accountHolder = "Yash";
        c1.balance = 50000;

        c2.accountHolder = "Lara";
        c2.balance = 40000;

        System.out.println("Account Holder Name: " + c1.accountHolder);
        System.out.println("Account Balance: " + c1.balance + "\n");
        
        System.out.println("Account Holder Name: " + c2.accountHolder);
        System.out.println("Account Balance: " + c2.balance);
    }
}
