package javabook.chapter7;

public class DmbCellPhone extends cellphone{
    int channel;
    DmbCellPhone(String model,String color,int channel){
        this.model=model;
        this.color=color;
        this.channel=channel;
    }

    void turnOnDum(){
        System.out.println("채널 "+channel+"번 DMB 방송 수신을 시작합니다.");
    }
    void changeChannelDmb(int channel){
        this.channel=channel;
        System.out.println("채널 "+channel+"번으로 바꿉니다");
    }
    void turnoffDmb(){
        System.out.println("DMB방송 수신을 멈춥니다");
    }
}
