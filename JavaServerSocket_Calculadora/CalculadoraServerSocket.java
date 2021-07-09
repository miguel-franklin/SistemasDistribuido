import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.lang.reflect.Method;
import java.net.ServerSocket;
import java.net.Socket;

public class CalculadoraServerSocket {

    private PrintWriter out;
    private BufferedReader in;
    private ServerSocket serverSocket;
    private Socket clientSocket;

    public void start(int port) {
        try {
            //Diferente do io.socket aqui usamos net.ServerSocket que faz o processo obter o bind na porta especificada
            serverSocket = new ServerSocket(port);
            System.out.println("Server up, waiting connections...");

            while (true) {

                //Aqui o programa dar um lock e espera um cliente se conectar na porta
                clientSocket = serverSocket.accept();

                //Buffer de entrada e PrintWriter de saida poderia ser um buffer tambem mas optei pelo o PrintWriter
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                out = new PrintWriter(clientSocket.getOutputStream(), true);                

                System.out.println("Receiving connection, waiting for operations...");


                //Aqui ler o string do nome da operacao
                String op = in.readLine();

                //Se operacao tiver o valor "quit" ele quebra o loop e invoca o stop
                if (op.equals("quit")) {
                    break;
                }

                //Ler os parametros do buffer 
                String o1 = in.readLine();
                String o2 = in.readLine();

                //Aqui usei um pouco de reflection pra evitar o switchs e ifs e elses
                Method operation = Calculadora.class.getMethod(op, double.class, double.class);

                //Invoka o metodo e obtem o resultado
                double result = (double) operation.invoke(null, Double.parseDouble(o1), Double.parseDouble(o2));

                //Envia de volta o resultado para o cliente
                out.println(result);

                //Fecha o stream de saida
                out.close();

                //Fecha o stream de entrada
                in.close();
            }

            //Fecha o server
            stop();

        } catch (Exception e) {
            System.out.println(e);
            System.exit(0);
        }
    }

    public void stop() {
        try {
            in.close();
            out.close();
            clientSocket.close();
            serverSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String... args) {
        CalculadoraServerSocket server = new CalculadoraServerSocket();
        server.start(9090);
    }

}
