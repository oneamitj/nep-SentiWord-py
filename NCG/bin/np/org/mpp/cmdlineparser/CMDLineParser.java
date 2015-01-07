/**
 * 
 */

/**
 * @author mpp
 *
 */
import java.util.*;
//import java.io.
public class CMDLineParser {

	/**
	 * @param args
	 */
	private String [] arguments;
	private Hashtable<String, String> optionHash;
	private ArrayList <String> optionsMan;
	private ArrayList <String> optionsOpt;
	CMDLineParser(String arguments[]){
		this.arguments=arguments;
		this.optionHash=new Hashtable<String, String>();
		this.optionsMan=new ArrayList<String>();
		this.optionsOpt=new ArrayList<String>();
	}
	public void loadOptionsMan(String []optionList){
		int i;
		for(i=0;i<optionList.length;i++){
			this.optionsMan.add(optionList[i]);
		}
	}
	public void loadOptionsOpt(String []optionList){
		int i;
		for(i=0;i<optionList.length;i++){
			this.optionsOpt.add(optionList[i]);
		}
	}
	public void parseAndLoad() {
		int i=0;
		String temp=null;
		while(i<arguments.length){
			temp=arguments[i];
			try {
				if (!temp.startsWith("-")){
					System.out.println ("Incorrect input format.");
					System.exit(0);
					//break;
				}else if ( temp.startsWith("-")&&!this.optionsMan.contains(temp)){
					System.out.println("Input error");
					System.exit(0);
					//break;
				}
			}catch (Exception e){
				System.out.println(e);
				//System.exit(0);
			}
			if(temp.startsWith("-")){
				if(this.optionsMan.contains(temp)){
					++i;
					if(arguments[i].startsWith("-")){
						System.out.println("Options "+temp+" should be followed by value");
						break;
					}
					if(i>=arguments.length){
						System.out.println("Options "+temp+" should be followed by value");
						break;
					}
					if(!arguments[i].startsWith("-")){
						this.optionHash.put(temp, arguments[i]);
					}
					else{
						System.out.println("Options "+temp+" should be followed by value");
					}
					++i;
				}
				else if(this.optionsOpt.contains(temp)){
					this.optionHash.put(temp, null);
					++i;
				}				
				
			}
		}
	}
	
	public String get(String option){
		if(this.optionHash.containsKey(option)){
			return this.optionHash.get(option);
		}
		else{
			return null;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CMDLineParser clp=new CMDLineParser(args);
		String manOpts[]={"-c", "-i","-y","-s"};
		String optOpts[]={"-x","-z"};
		clp.loadOptionsMan(manOpts);
		clp.loadOptionsOpt(optOpts);
		clp.parseAndLoad();
		System.out.println(clp.get("-s"));

	}
}
