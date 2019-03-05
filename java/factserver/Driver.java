package factserver;

import factserver.core.*;

class Driver{
	public static void main(String[] args){
		Thread server = new Thread(new Server(8001));
		server.start();
		try{
			server.join();
		}catch(Exception e){e.printStackTrace();}
	}
}
