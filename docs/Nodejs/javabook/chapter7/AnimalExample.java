package javabook.chapter7;

public class AnimalExample {
    public static void main(String[] args) {
        dog dog = new dog();
        cat cat = new cat();
        dog.sound();
        cat.sound();
        System.out.println("-------");
        Animal animal = null;
        animal = new dog();
        animal.sound();
        animal=new cat();
        animal.sound();
        System.out.println("-------");

        animalSound(new dog());
        animalSound(new cat());
    }
    public static void animalSound(Animal animal){
        animal.sound();
    }
}
