import java.util.*;

public class acslShortAnswer { /* Hi Ms. Bono! 
    Apologies if this is slightly different than the version on the website
    I lowk forgot the names of the methods, but it's the same functionality. */
    public static void main(String[] args){
        System.out.println(getSequences("1 3 9 27 24 21 22 43 65 63 60 56"));
    }
    public static String getSequences(String numbers){
        ArrayList<Integer> betterList=makeSequencesNice(numbers);
        String toRet="";
        String type="";
        double diff=0;
        boolean arith=false;
        boolean geom=false;
        boolean fib=false;
        boolean triang=false;
        for (int i = 0; i < betterList.size()-2; i++) { /*We look at every consecutive triple */
           /*Testing which sequences apply */
            arith=testArithmetic((int)betterList.get(i), (int)betterList.get(i+1),(int)betterList.get(i+2));
            geom=testGeometric((int)betterList.get(i), (int)betterList.get(i+1),(int)betterList.get(i+2));
            fib=testFibonacci((int)betterList.get(i), (int)betterList.get(i+1),(int)betterList.get(i+2));
            triang=testTriangular((int)betterList.get(i), (int)betterList.get(i+1),(int)betterList.get(i+2));
            if(arith==false&&geom==false&&fib==false&&triang==false){ /*If no sequences apply we continue */
                continue;
            }
            else if (arith==true){
                int num=(int)betterList.get(i+1)-(int)betterList.get(i); /*Finding the difference*/
                if(type.equals("A")&&num==(int)(diff)){ /*If this is a continuation of a sequence, we continue*/
                    continue;
                }
                else if(num==0){ /*If it's just the constant sequence, we denote so 
                (I don't remember how they did this in the ACSL but I like my way better haha) */
                    toRet+=" A0/G1 ";
                    continue;
                }
                else{ /* If it's a new sequence, we add it */
                    toRet+="A"+num;
                    type="A";
                    diff=num;
                }
            }
            /*Mostly identical process for the rest, I'll comment on the unique features of other sequences */
            else if (geom==true){
                double num=((double)betterList.get(i+1)/(double)betterList.get(i)); /*Since multiplication, we have to account for fractional differences. */
                if(type.equals("G")&&num==diff){
                    continue;
                }
                else{
                    toRet+=" G"+num;
                    type="G";
                    diff=num;
                }
            }
            else if (fib==true){
                int num=(int)betterList.get(i+1)-(int)betterList.get(i); /* If I recall correctly it asked 
                for the difference between the first two terms? 
                If not though, then just set whatever it asks for to*/
                if(type.equals("F")){ /* Because of recursive properties, if a_(n+2)=a_(n+1)+a_n holds 
                    for both i-1 and i, they're part of the same sequence.*/
                    continue;
                }
                else{
                    toRet+=" F"+num;
                    type="F";
                    diff=num;
                }
            }
            else if (triang==true){
                int num=(int)betterList.get(i+1)-(int)betterList.get(i);
                if(type.equals("T")){ /*Holds like Fibonacci because if common differences increase by one from
                    i-1 to i, i to i+1, and i+1 to i+2, it's triangular. */
                    continue;
                }
                else{
                    toRet+=" T"+num;
                    type="T";
                    diff=num;
                }
            }
        }
        return toRet;
    }
    public static boolean testArithmetic(int a, int b, int c){
        if (c-b==b-a){ /* by the definition of an arithmetic sequence */
            return true;
        }
        else{
            return false;
        }
    }
    public static boolean testGeometric(int a, int b, int c){
        if(a*c==b*b){ /* by the definiton of geometric sequence,
            and much better than using division
            since division rounds down, whereas multiplication isn't faulty with ints.*/
            return true;
        }
        else{
            return false;
        }

    }
    public static boolean testFibonacci(int a, int b, int c){
        if (c==a+b){ /*By the definition of a Fibonacci-type sequence. */
            return true;
        }
        else{
            return false;
        }
    }
    public static boolean testTriangular(int a, int b, int c){
        if (c-b==b-a+1&&b-a>0){ /*how they defined positive triangular sequences */
            return true;
        }
        if (c-b==b-a-1&&b-a<0){ /* how they defined negative triangular sequences */
            return true;
        }
        else{
            return false;
        }

    }
    public static ArrayList<Integer> makeSequencesNice(String numbers){ /*Essentially getting rid of spaces
        and formatting like a nice ArrayList*/
        ArrayList<String> stringList=new ArrayList<>();
        int count=0;
        for (int i = 0; i < numbers.length(); i++) { /*If there's a space, we move to the next entry in the ArrayList
        If not then we keep compiling. We need a String ArrayList first because the negative signs get weird. */
            if (numbers.substring(i,i+1).equals(" ")){
                count++; 
            }
            else if (i!=numbers.length()){
                stringList.set(count, stringList.get(count)+numbers.substring(i,i+1));
            }   
            else{
                stringList.set(count, stringList.get(count)+numbers.substring(i));
            }
        }
        ArrayList<Integer> toRet=new ArrayList<>();
        for (int i = 0; i < stringList.size(); i++) {
            toRet.add((int)(Integer.parseInt(stringList.get(i)))); /*Converting strings to int */
        }
        return toRet;
    }
}

