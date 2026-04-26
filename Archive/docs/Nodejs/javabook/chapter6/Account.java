package javabook.chapter6;

public class Account {
    int Balance=0;

    void setBalance(int n){
        if(n>=0) 
        this.Balance=n;
    }
    int getBalance(){
        return Balance;
    }
}
