package org.velezreyes.quiz.question6;

public class Drink {
  private String name;
  private boolean fizzy = true;
  private int getPrice;

  
  public Drink(String name, boolean fizzy) {
    this.name = name;
    this.fizzy = fizzy;
  }

  public Drink(String name, boolean fizzy, int getPrice) {
    this.name = name;
    this.fizzy = fizzy;
    this.getPrice = getPrice;
  }


  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public boolean isFizzy() {
    return fizzy;
  }


  public void setFizzy(boolean fizzy) {
    this.fizzy = fizzy;
  }


  public int getGetPrice() {
    return getPrice;
  }


  public void setGetPrice(int getPrice) {
    this.getPrice = getPrice;
  }
  
}