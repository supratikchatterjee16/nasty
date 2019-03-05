import java.net.*;
import java.io.*;

class Frontend{
	private static String list[] = {
		"parse Bihari had been praying for a rain. He then fornicated in it.",
		"parse I am an Indian. Rajiv Gandhi has been shot. He had been our prime minister for a long time.",
		"command exit"
	};
	public static void main(String[] args){
		try{
			String str="";
			int n = 0;
			for(int i=0;i<list.length;i++){
				Socket s = new Socket("localhost",8001);
				PrintWriter pw = new PrintWriter(s.getOutputStream());
				BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
				pw.print(list[i]+"\0");
				pw.flush();
				System.out.println("Sentence sent : "+list[i]);
				System.out.println("Awaiting incoming message");
				while((n=br.read())>0) System.out.print((char)n);
				s.close();
			}
		}catch(Exception e){
			
		}
	}
}
