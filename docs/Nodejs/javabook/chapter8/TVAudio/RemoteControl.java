package javabook.chapter8.TVAudio;

public interface RemoteControl {
    //상수 필드 : 런타임 시 데이터를 저장할 수 있는 필드를 선언할 수 없다.
    //그러나 상수 필드는 선언이 가능하다 상수는 인터페이스에 고정된 갑으로 런타임 시에 데이터를 바꿀 수없다
    //static final int 형태
    int MAX_VOLUME =10;
    int MIN_VOLUME=0;

    //추상 메소드 : 객체가 가지고 있는 메소드 설명 호출시 필요한 매개값 리턴타입만 공지 실제 실행부는 객체가 가지고 있다
    void turnOn();
    void turnOff();
    void setVolume(int volume);

    //디폴트 메소드 : 인터페이스에 선언되지만 사실 객체가 가지고 있는 인스턴스 메소드
    default void setMute(boolean mute){
        if(mute){
            System.out.println("무음 처리합니다.");
        }else{
            System.out.println("무음 해제합니다.");
        }
    }

    //정적 메소드 : 객체가 없어도 인터페이스만으로 호출가능
    static void changeBettey(){
        System.out.println("건전지를 교환합니다.");
    }
}
