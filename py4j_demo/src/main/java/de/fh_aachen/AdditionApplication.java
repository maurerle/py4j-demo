package de.fh_aachen;

import java.util.HashMap;

public class AdditionApplication {

  public int addition(int first, int second) {
    return first + second;
  }
  public void sayHello() {
        System.out.println("Hello World!");
  }
  
  public String printDict(HashMap dict) {
        System.out.println(dict.toString());
        return dict.toString();
    }
}