/**
 *
 * John E. Boon, Jr.
 *
 * Copyright (c) 2010 John E. Boon, Jr. (Work in Progress)
 *
 * Project: Matrix-Chain-Order(p) and Matrix-Chain-Multiply(A,s,i,j) Algorithms
 *          solves problem 14.2-1, 14.2-2, or use data in text Fig. 14.5
 *
 * Students are granted unlimited rights to this file.
 *
 */
import java.io.*;
public class OptMatrixParen extends Object {
  
    private static void MatrixChainOrder(int p[], double s[][], double m[][]) {
    	// Programming note - pseudocode in text uses index variable letter l
    	// for readability and to prevent accidental programming errors, 
    	// variable c will be used instead in my program
         int n,i,j,k,c;
         double q;
         n = p.length-1;
         //System.out.println("n="+n);
         for (i=1; i<=n; i++) m[i][i]=0;
         
         for (c=2; c<=n; c++) {
            for (i=1; i<=(n-c+1); i++) {
            	j=i+c-1;
            	m[i][j]=999999;
            	for (k=i; k<=(j-1); k++) {
            		//System.out.println(c+ " "+i+" "+j+" " +k);
            		q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j];
            		if (q < m[i][j]) {
            			m[i][j]=q;
            			s[i][j]=k;
            		}
            	}
            }
         }
    }

   private static void MatrixChainMult(double s[][],int i, int j) {
   	int x,y;
   	//Prints solution in algebraic order
      if (j > i) {
      	System.out.println("( ");
      	MatrixChainMult(s,i,(int)s[i][j]);
      	MatrixChainMult(s,(int)s[i][j]+1,j);
      	System.out.println(")");
      }
      else System.out.println("i="+i);
   }

   public static void main(String[] args) {
   	int i,j;
   	// In the text, the p array starts at Zero
   	// see book page 375 "The procedure assumes that matrix A(i) has
   	// dimensions p(i-1) by p(i) for i=1,2,...,n. Its input is a sequence
   	// p = <p(0), p(1),...,p(n)> where p.length = n+1."
   	//int [] p = new int [] {30,35,15,5,10,20,25}; //Fig 5.5 Data
   	int [] p = new int [] {5,10,3,12,5,50,6};      //Ex 5.2-1 Data
   	int DataDim = p.length+1;                      //account for unused 0th
	  double [][] m = new double [DataDim][DataDim];
	  double [][] s = new double [DataDim][DataDim];
	  
    MatrixChainOrder(p,s,m);
    int NumArrays = DataDim-2; 
    
     System.out.println("Optimal Solution");
     MatrixChainMult(s,1,NumArrays);
     
     System.out.println();
     System.out.println("Array m");     
     for (i=1; i<=NumArrays; i++) {
     	for (j=1; j<=NumArrays; j++) {
     		System.out.print(m[i][j] + " ");
          }
          System.out.println();
     }
     System.out.println();
     System.out.println("Array s");
     for (i=1; i<=NumArrays; i++) {
     	for (j=1; j<=NumArrays; j++) {
     		System.out.print(s[i][j] + " ");
          }
          System.out.println();
     }

   }

}
