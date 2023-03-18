import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class HelloWorld{
    
   public static void main(String[] args) throws IOException {
    String filename = null;
    if(args.length!=0){
        filename= args[0];
    }
    FileReader fileReader=new FileReader(filename);
    BufferedReader in=new BufferedReader(fileReader);
       int n = Integer.parseInt(in.readLine());
       for(int i = 0; i < n; i++) {
    	   String string=in.readLine();
           if(string==null)
               break;
           System.out.println("Hello, " + string + "!");
       }
       in.close();
   }
}