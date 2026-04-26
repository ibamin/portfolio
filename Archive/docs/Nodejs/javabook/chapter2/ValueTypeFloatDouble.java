package javabook.chapter2;

public class ValueTypeFloatDouble {
    public static void main(String[] args) {
        double var1=3.14;
        float var2 =3.14f;

        double var3 = 0.123456789123456789;
        float var4 =0.123456789123456789f;

        System.out.println("var1: "+var1);
        System.out.println("var2: "+var2);
        System.out.println("var3: "+var3);
        System.out.println("var4: "+var4);

        int var5=3000000;
        double var6=3e6;
        float var7=3e6f;
        double var8=2e-3;
        System.out.println("var5: "+var5);
        System.out.println("var6: "+var6);
        System.out.println("var7: "+var7);
        System.out.println("var8: "+var8);
    }
}
