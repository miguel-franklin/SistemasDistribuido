import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class CalculadoraClientSocket {

    public static void main(String[] args) {

        // TODO Auto-generated method stub
        double oper1 = 10, oper2 = 20;
        String operacao = "dividir"; // somar subtrair dividir multiplicar
        String result = "";
        try {

            // Conex�o com o Servidor
            Socket clientSocket = new Socket("127.0.0.1", 9090);
            DataOutputStream socketSaidaServer = new DataOutputStream(clientSocket.getOutputStream());

            // Enviando os dados
            socketSaidaServer.writeBytes(operacao + "\n");
            socketSaidaServer.writeBytes(oper1 + "\n");
            socketSaidaServer.writeBytes(oper2 + "\n");
            socketSaidaServer.flush();

            // Recebendo a resposta
            BufferedReader messageFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            result = messageFromServer.readLine();

            System.out.println("resultado=" + result);
            clientSocket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
