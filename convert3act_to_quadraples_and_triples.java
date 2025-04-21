import java.util.HashMap;
import java.util.Map;

public class convert3act_to_quadraples_and_triples {

    public static void main(String[] args) {

        String[] threeac = {
                "t1=a+b",
                "t2=c-d",
                "t3=t1*t2",
                "x=t3"

        };
        System.out.println("The Quadraples are : ");
        threeac_to_quadraples(threeac);
        threeac_to_triples(threeac);

    }

    public static void threeac_to_quadraples(String[] threeac) {
        System.out.println("Index\tOperator\toperand1\toperand2\tresult");
        for (int i = 0; i < threeac.length; i++) {
            String stmt = threeac[i];

            String[] part = stmt.split("=");
            String result = part[0];
            String exp = part[1];

            if (!exp.matches(".*[+\\-*/].*")) {
                System.out.println(i + "\t\t" + " = " + "\t\t" + exp + "\t\t" + "  " + "\t\t" + result);
                continue;
            }

            String operator = "";
            String op1, op2;

            if (exp.contains("+")) {
                operator = "+";

            } else if (exp.contains("-")) {
                operator = "-";

            } else if (exp.contains("*")) {
                operator = "*";

            } else if (exp.contains("/")) {
                operator = "/";

            }
            String[] parts = exp.split("[+\\-*/]");
            op1 = parts[0];
            op2 = parts[1];

            System.err.println(i + "\t\t" + operator + "\t\t" + op1 + "\t\t" + op2 + "\t\t" + result);

        }
    }

    public static void threeac_to_triples(String[] threeac) {
        Map<String, String> variables = new HashMap<String, String>();

        System.out.println("The Triples of 3AC are : ");

        for (int i = 0; i < threeac.length; i++) {
            String stmt = threeac[i];
            String[] part = stmt.split("=");
            String result = part[0];
            variables.put(result, Integer.toString(i));
            String exp = part[1];

            String operator = "";

            if (exp.contains("+")) {
                operator = "+";
                String[] parts = exp.split("\\+");
                String op1 = variables.containsKey(parts[0]) ? variables.get(parts[0]) : parts[0];
                String op2 = variables.containsKey(parts[1]) ? variables.get(parts[1]) : parts[1];
                System.out.println("( " + i + "\t" + operator + "\t" + op1 + "\t" + op2 + " )");

            } else if (exp.contains("-")) {
                operator = "-";
                String[] parts = exp.split("-");
                String op1 = variables.containsKey(parts[0]) ? variables.get(parts[0]) : parts[0];
                String op2 = variables.containsKey(parts[1]) ? variables.get(parts[1]) : parts[1];
                System.out.println("( " + i + "\t" + operator + "\t" + op1 + "\t" + op2 + " )");

            } else if (exp.contains("*")) {
                operator = "*";
                String[] parts = exp.split("\\*");
                String op1 = variables.containsKey(parts[0]) ? variables.get(parts[0]) : parts[0];
                String op2 = variables.containsKey(parts[1]) ? variables.get(parts[1]) : parts[1];
                System.out.println("( " + i + "\t" + operator + "\t" + op1 + "\t" + op2 + " )");

            } else if (exp.contains("/")) {
                operator = "/";
                String[] parts = exp.split("/");
                String op1 = variables.containsKey(parts[0]) ? variables.get(parts[0]) : parts[0];
                String op2 = variables.containsKey(parts[1]) ? variables.get(parts[1]) : parts[1];
                System.out.println("( " + i + "\t" + operator + "\t" + op1 + "\t" + op2 + " )");
            }

        }

    }

}
