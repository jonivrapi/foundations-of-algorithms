/**
 *
 * John E. Boon, Jr.
 *
 * Copyright (c) 2000 John E. Boon, Jr. (Work in Progress)
 *
 * Project: Recursion Eq. 14.7 page 377 CLRS 4Ed computation
 *
 * Students are granted unlimited rights to this file.
 *
 */
import java.io.*;
public class Eq14_7 extends Object {
  
    private static void recurrence(int P[], int MAX_ELEM) {
         int n,k;

         P[1] = 1;
         for (n=2; n<=MAX_ELEM; n++) {
            P[n] = 0;
            for (k=1; k<=n-1; k++) {
               P[n] = P[k]*P[n-k] + P[n];
            }
            System.out.println(n + "," + P[n]);
         }
    }

 

   public static void main(String[] args) {
   	int MAX_ELEM = 20;

	   int[] P = new int [MAX_ELEM+1];
      recurrence(P,MAX_ELEM);
   }
     
}
