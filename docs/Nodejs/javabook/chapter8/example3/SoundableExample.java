package javabook.chapter8.example3;

public class SoundableExample {
    private static void printSound(Soundable soundable){
        System.out.println(soundable.sound());
    }

    public static void main(String[] args) {
        printSound(new Dog());
        printSound(new Cat());
    }
}
