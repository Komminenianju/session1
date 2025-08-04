interface Animal {
    void makeSound();
}
 class Cat implements Animal {
    public void makeSound() {
        System.out.println("Cat runs");
    }
    public static void main(String[] args) {
        Cat c =new Cat();
        c.makeSound();
    }
}