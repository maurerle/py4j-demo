package de.fh_aachen;
import py4j.GatewayServer;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        AdditionApplication app = new AdditionApplication();
        // app is now the gateway.entry_point
        GatewayServer server = new GatewayServer(app);
        System.out.println("Start Server for Py4J");
        server.start();
    }
}
