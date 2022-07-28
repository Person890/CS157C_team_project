import com.mongodb.client.MongoDatabase; 
import com.mongodb.MongoClient; 
public class App { 
   
   public static void main( String args[] ) {  
      
      // Creating a Mongo client  172-31-82-48:27021
      MongoClient mongo = new MongoClient( "ec2-54-174-23-133.compute-1.amazonaws.com" , 27021 ); 

      // Accessing the database 
      MongoDatabase database = mongo.getDatabase("mydbs"); 

      for (String s : database.listCollectionNames()) {
         System.out.println(s);
      }   
   } 
}