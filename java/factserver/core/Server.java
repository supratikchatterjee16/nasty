package factserver.core;

import java.net.Socket;
import java.net.ServerSocket;

import java.io.PrintWriter;
import java.io.IOException;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.Scanner;
import java.util.Date;

public class Server implements Runnable{
	private int port;
	private static RelationExtractor ext;
	public Server(int p){
		this.port = p;
		this.ext = new RelationExtractor();
	}
	public void log(Object obj){
		try{
		FileWriter fw = new FileWriter("log.txt",true);
		fw.write(obj.toString()+"\n");
		fw.close();
		}catch(IOException e){}
	}
	public void run(){
		Thread.currentThread().setName("server");
		String id = "["+Thread.currentThread().getName()+"] ";
		try{
			int n=0;
			boolean on=true;
			ServerSocket ss = new ServerSocket(8001);
			Socket s = null;
			StringBuffer str = null;
			log(id+"Server ready for connections.");
			while(on){
				s = ss.accept();
				Date date = new Date();
				log(id+"Connection made to : "+s+" "+date.toString());
				BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
				PrintWriter pw = new PrintWriter(s.getOutputStream());
				str = new StringBuffer();
				while((n=br.read())!=(int)'\0'||n == -1)
					str.append((char)n);
				//log(str);
				Scanner sc = new Scanner(str.toString());
				String response = "";
				String action = sc.next();
				String data = str.substring(action.length()+1);
				if(action.equals("parse")) response = ext.parse(data);
				else if(action.equals("command")){
					log(id+"Command recieved : "+str.substring(8));
					if(data.equals("exit")){
						s.close();
						break;
					}
				}
				//log(response);
				response+="\0";
				pw.print(response);
				pw.flush();
				s.close();
				log(id+"Transmission complete");
			}
		}catch(Exception e){
			log(id+"An exception occured : "+e);
			e.printStackTrace();
		}
		return;
	}
	//Sample
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
