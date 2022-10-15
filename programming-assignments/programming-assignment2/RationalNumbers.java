//********************************************************************
//  RationalNumbers.java       Author: Lewis and Loftus
//  Boon modifications June 2020
//  Driver to exercise the use of multiple Rational objects.
//********************************************************************

public class RationalNumbers
{
   //-----------------------------------------------------------------
   //  Creates some rational number objects and performs various
   //  operations on them.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {
      Rational r1 = new Rational (6, 8);
      Rational r2 = new Rational (1, 3);
	  Rational e1 = new Rational (4, 1);

      System.out.println ("First rational number : " + r1);
      System.out.println ("Second rational number: " + r2);

      if (r1.equals(r2))
         System.out.println ("r1 and r2 are equal.");
      else
         System.out.println ("r1 and r2 are NOT equal.");

      Rational j3 = r1.add(r2);
      Rational j4 = r1.subtract(r2);
      Rational j5 = r1.multiply(r2);
      Rational j6 = r1.divide(r2);
	  Rational j7 = r1.expon(e1);


      System.out.println ("r1 + r2: " + j3);
      System.out.println ("r1 - r2: " + j4);
      System.out.println ("r1 * r2: " + j5);
      System.out.println ("r1 / r2: " + j6);
      System.out.println ("r1 ^ r2: " + j7);
	  
      
      // *************************************
      // Student question testing area by Boon
      // *************************************
      Rational m = new Rational(1,1);
      Rational b = new Rational(2,1);
      
      System.out.println ("First rational number m : " + m);
      System.out.println ("Second rational number b: " + b);
      Rational r7 = m.divide(b);
      System.out.println ("m / b: " + r7);
      System.out.println ("(m/b): " + m.divide(b));
       
      
   }
}