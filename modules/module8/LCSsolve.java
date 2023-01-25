/**
 *
 * John E. Boon, Jr.
 *
 * Copyright (c) 2010 John E. Boon, Jr. (Work in Progress)
 *
 * Project: LCS-LENGTH(X,Y) and PRINT-LCS(b,X,i,j) Algorithms
 *          solves problem 14.4-1
 *
 * Students are granted unlimited rights to this file.
 *
 */
import java.io.*;
public class LCSsolve extends Object {
  
    private static void LCSlength(int X[], int Y[], double c[][], String b[][]) {
    	int m,n,i,j;
    	m=X.length-1;
    	n=Y.length-1;
    	for (i=1; i<=m; i++) c[i][0]=0;
    	for (j=0; j<=n; j++) c[0][j]=0;
    	for (i=1; i<=m; i++) {
    		for (j=1; j<=n; j++) {
    			if (X[i]==Y[j]){
    				c[i][j]=c[i-1][j-1]+1;
    				b[i][j]="UL";
    			}
    			else if (c[i-1][j]>=c[i][j-1]) {
    				c[i][j]=c[i-1][j];
    				b[i][j]="UP";
    			}
    			else {
    				c[i][j]=c[i][j-1];
    				b[i][j]="LE";
    			}
    		}
    	}
         
    }

   private static void PrintLCS(String b[][],int X[], int i, int j) {
   	if ((i==0) || (j==0)) return;
   	if (b[i][j]=="UL") {
   	   PrintLCS(b,X,(i-1),(j-1));
   	   System.out.print(X[i]+ " ");
   	}
   	else if (b[i][j]=="UP") PrintLCS(b,X,(i-1),j);
   	else PrintLCS(b,X,i,(j-1));
   }

   public static void main(String[] args) {
   	int i,j,n,m;
   	// Exercise 15.4-1 data
     int [] Y = new int [] {9,1,0,0,1,0,1,0,1};
   	 int [] X = new int [] {9,0,1,0,1,1,0,1,1,0};
   	// Figure 15.8 data
   	// (I was lazy -- mapped characters to integers 
   	// as I didn't have a container class for my X and Y
   	// in this implementation
   	// A=1, B=2, C=3, D=4
    // int [] X = new int [] {9,1,2,3,2,4,1,2};
   	// int [] Y = new int [] {9,1,4,3,1,2,1};   	
   	m=X.length-1;
   	n=Y.length-1;
	double [][] c = new double [m+1][n+1]; //[0..m][0..n]
	String [][] b = new String [m+1][n+1]; //[1..m][1..n]
	for (i=0; i < b.length; i++) {
        for (j=0; j < b[0].length; j++){
        	b[i][j]="0 ";
        }
     }
     LCSlength(X,Y,c,b);
     System.out.print("LCS is:  ");
     PrintLCS(b,X,m,n);
     System.out.println();
     System.out.println("c and b tables computed by LCS-LENGTH:");
     for (j=0; j < c[0].length; j++){
        System.out.print("    j="+j+"    ");
     }
     System.out.println();
     for (i=0; i < c.length; i++) {
        System.out.print("i="+i+" ");
        for (j=0; j < c[0].length; j++){
        	System.out.print("["+c[i][j]+ " | "+ b[i][j]+ "] ");
        }
        System.out.println();
     }

   }

}
