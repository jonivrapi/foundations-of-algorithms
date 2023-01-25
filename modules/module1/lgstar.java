/**
 *
 * John E. Boon, Jr.
 *
 * Copyright (c) 2000 John E. Boon, Jr. (Work in Progress)
 *
 * Project: Example program Chapter 2 iterated logarithm function
 *
 * Students are granted unlimited rights to this file.
 *
 */
import java.io.*;
//Note that java.lang.Math is imported by default
/**
 * <p>
 * This class implements the iterated logarithm function; it uses command-line
 * interface.
 * The program prompts the student for a non-negative number, then computes the
 * <i>lg*n</i> for that number.
 * <p>
 * Revision control information for this file follows:
 * <ul>
 * <li><CODE>$Source$</CODE>
 * <li><CODE>$State$</CODE>
 * </ul>
 * <p>
 * Program Description:
 * <ul>
 * <li> Thomas H. Cormen, Lieserson, Charles E., and Rivest, Ronald L., 
 *      <i>Introduction to Algorithms</i>. Cambridge, MA: The MIT Press, 1990.
 *      (page 36) 
 * <li>Program Unit Notebook: There is no separate documentation for this 
 *      program.
 * <li> Program Goals: This program implements the iterated logarithm function.
 * <li>Reusability Keywords : algorithmic growth iterated log
 * <li>Software Metrics
 * <ol>
 * <li>Cyclomatic Complexity: {not yet computed}
 * <li>Program Volume: {not yet computed}
 * </ol>
 * </ul>
 * <p>
 * Runtime Environment
 * <ul>
 * <li>Platform              : Intel PentiumPro/Windows NT 4.0 (Service Pack 6a)
 * <li>Compiler Used         : JDK 1.3.0-C/Forte for Java, Community Edition 
 *                             v. 1.0 (Build 842)
 * <li>Compilation Switches  : no special switches required
 * </ul>
 * <p>
 * <ol>
 * <li>Input Files Needed    : none
 * <li>Temporary Files Needed: none
 * <li>Output Files Needed   : none
 * </ol>
 * <p>
 * Header Version            : BOON-08-03-2000-GNU-CVS
 * <p>
 * @author  John E. Boon, Jr.
 * @version $Revision$
 * @since   1.3
 */

public class lgstar extends Object {
    
    /**
     * Default Constructor used for this class.
     */
    public lgstar() {
    }

    /**
     * Main control flow for the test harness program for the iterated base 2
     * logarithm.
     * <p>
     * Function Signature: function: {int} -> {int}
     * <p>
     * Program Plans: Prepare to read from the standard input stream at the
     * console, read the number for which the iterated base 2 log is to be
     * computed, compute the iteratated base 2 log, and display the result.
     * <p>
     * Precondition Axioms: (optional) 
     * <p>
     * Postcontdition Axioms: none
     * <p>
     * @throws IOException   The exception is not handled, but the exception
     *                       code is displayed.
     */    
    public static void main(String [] args) throws IOException {
        /** value of the iterated base 2 log */
        int lg_star_value = 0;
        /** number for which to compute the base 2 iterated log */
        long n = 0;
        System.out.println("Enter the non-negative number for which to compute"
                           + " lg* (n > 1):");
        BufferedReader in =new BufferedReader(new InputStreamReader(System.in));
        try {
            String text = in.readLine();
            n = Long.parseLong(text);
            lg_star_value = iterated_log_base2(n);
            System.out.println("lg* of " + n + " is " + lg_star_value);
        }
        catch (IOException exception) {
            exception.printStackTrace(System.err);
	    System.exit(-1);
        }

   }//end of main method

    /**
     * Compute the base 2 logarithm of a number, using the change of base
     * forumla.
     * <p>
     * Function Signature: function: {real} -> {real}
     * <ul>
     * <li>domain function ::= {x member of real| x > 0}
     * </ul>
     * <p>
     * Program Plans: apply the change of base formula: 
     * log base <i>b</i>(<i>a</i>) = log base <i>c</i>(<i>a</i>)/log base 
     * <i>c</i>(<i>b</i>)
     * <p>
     * Precondition Axioms: x > 0 
     * <p>
     * Postcontdition Axioms: base 2 log computed
     * <p>
     * @param x      number for which the base 2 log is needed.
     * @return (a/b) the base 2 log of the input value.
     */
    private static double lg(double x) {
        // note that java.lang.Math log(double) returns the natural logarithm
        double a = Math.log(x);
        double b = Math.log(2.0);
        return (a/b);
    }

    /**
     * Iterated base 2 logarithm function.
     * <p>
     * Function Signature: function: {int} -> {int}
     * <ul>
     * <li>domain function ::= {x member of int | x > 0}
     * </ul>
     * <p>
     * Program Plans: Count the number of times the base 2 log of the input 
     *    number can be taken.  Stop when i = 0, the base case or the base 2 
     *    log of the current value is undefined.
     * <p>
     * Precondition Axioms: n > 1
     * <p>
     * Postcontdition Axioms: iterated log value > 0
     * <p>
     * @param n   number for which the iterated base 2 log is needed
     * @return (i-1) the iterated base 2 log of the input value.
     */    
    private static int iterated_log_base2(long n) {
        int i;
        double lg_star;
        i = 0;
        lg_star = (double) n;
        while (lg_star > 0) {
            i++;
            lg_star = lg(lg_star);
        }
        return (i-1);
    }
}   
