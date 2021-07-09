public class Calculadora {    

    public static double somar(double oper1, double oper2) {
        return oper1 + oper2;
    }

    public static double subtrair(double oper1, double oper2) {
        return oper1 - oper2;
    }

    public static double multiplicar(double oper1, double oper2) {
        return oper1 * oper2;
    }

    public static double dividir(double oper1, double oper2) {
        if (oper2 == 0) {
            return 0;
        }
        return oper1 / oper2;
    }
}