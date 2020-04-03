//Generates sequence of requests needed from request generator and saves them in a text file to be used later on
import java.util.Scanner;
import java.io.FileWriter;
import java.io.*;

public class ListReader{
	public Scanner sc = new Scanner(System.in);
	public static void main(String[]args){
		
		RequestGenerator rg = new RequestGenerator();
		
		try{
			FileWriter fw = new FileWriter(new File("requests.txt"),true);
			for (int i = 0; i<100000; i++){
				int x = rg.generateRequest();
				fw.write(Integer.toString(x)+ "\n");
				}
			fw.close();

		}
		catch (IOException ex) {
            ex.printStackTrace();
        }

			
	}
}