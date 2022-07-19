public class app {

    Runtime r = Runtime.getRuntime();
    Process p = null;
    String command = "mongoimport --db users --collection contacts --type csv --file /Users/nataliestepankevycova/Downloads/PrimeAwardSummariesAndSubawards_2022-07-11_H19M28S57512750.csv";
  try {
        p = r.exec(command);
        System.out.println("Reading csv into Database");

    } catch (Exception e){
        System.out.println("Error executing " + command + e.toString());
    }
}
