package javabook.chapter6;

public class shopservice {
    static shopservice spsvc = new shopservice();

    static shopservice getInstance(){
        return spsvc;
    }
}
