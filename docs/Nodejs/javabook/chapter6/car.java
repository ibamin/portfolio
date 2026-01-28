package javabook.chapter6;

public class car {
    String company = "현대자동차";
    String model = "그랜져";
    String color = "검정";
    int maxspeed = 350;
    int speed;

    car(){}
    car(String model){
        this(model,"은색",250);
    }
    car(String model,String color){
        this.color=color;
    }
    car(String model,String color,int maxspeed){
        this.model=model;
        this.color=color;
        this.maxspeed=maxspeed;
    }
    void setSpeed(int speed){
        this.speed=speed;
    }

    void run(){
        for(int i=10;i<=50;i+=10){
            this.setSpeed(i);
            System.out.println(this.model+"가 달립니다.(시속:"+this.speed+"km/h)");
        }
    }
    public static void main(String[] args) {
        car mycar =new car();
        mycar.speed=60;
        mycar.run();
    }
}
