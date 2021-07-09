import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.lang.reflect.Method;
import java.net.ServerSocket;
import java.net.Socket;

public class CalculadoraServer {

    private PrintWriter out;
    private BufferedReader in;
    private ServerSocket serverSocket;
    private Socket clientSocket;

    public void start(int port) {
        try {
            serverSocket = new ServerSocket(port);
            System.out.println("Server up, waiting connections...");

            while (true) {

                clientSocket = serverSocket.accept();
                out = new PrintWriter(clientSocket.getOutputStream(), true);
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

                System.out.println("Receiving connection, waiting for operations...");

                String op = in.readLine();

                if (op.equals("quit")) {
                    break;
                }

                String o1 = in.readLine();
                String o2 = in.readLine();

                Method operation = Calculadora.class.getMethod(op, double.class, double.class);
                double result = (double) operation.invoke(null, Double.parseDouble(o1), Double.parseDouble(o2));
                out.println(result);
                out.close();
                in.close();
            }
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
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String... args) {
        CalculadoraServer server = new CalculadoraServer();
        server.start(9090);
    }
}
