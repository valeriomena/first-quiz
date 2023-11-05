package org.velezreyes.quiz.question6;

import java.util.HashMap;

import java.util.Map;
 
public class VendingMachineImpl implements VendingMachine {
 
    private int totalMoney;

    private static VendingMachineImpl instance;

    private VendingMachineImpl() {
        this.totalMoney = 0;
    }

    public static VendingMachineImpl getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        instance.totalMoney = 0;
        return instance;
    }

    @Override
    public void insertQuarter() {
        this.totalMoney += 25; 
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        
 switch (name) { 
    case "ScottCola":
      if (this.totalMoney < 75){
            throw new NotEnoughMoneyException("Not enough money inserted.");
        }
        return new Drink(name,true);

    case "KarenTea":
     System.out.println("entro");
     System.out.println(this.totalMoney);
     if (this.totalMoney < 100){
            throw new NotEnoughMoneyException("Not enough money inserted.");
        }
        return new Drink(name,false);
    
    
     
  }
       throw new UnknownDrinkException("unknow drink select"); 


    }
}
