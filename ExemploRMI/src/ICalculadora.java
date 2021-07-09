import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ICalculadora extends Remote{

	public int soma(int a, int b) throws RemoteException;

    public int subtrair(int a, int b) throws RemoteException;

    public int multiplicar(int a, int b) throws RemoteException;

    public double dividir(int a, int b) throws RemoteException;
}
