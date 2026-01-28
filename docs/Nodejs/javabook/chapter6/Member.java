package javabook.chapter6;

public class Member {
    String name;
    String id;
    String password="12345";
    int age;

    Member(String name,String id){
        this.name=name; this.id=id;
    }
    boolean login(String id,String password){
        if(this.id==id && this.password==password)
        return true;
        else return false;
    }
}
