import java.util.HashMap;

public class hashTest {
    private static final HashMap<String, Integer> map = new HashMap<String, Integer> () {
        {
            put("A", 1);
            put("B", 2);
            put("C", 3);
            put("D", 4);
        }

    };
    public static void main(String[] argc) {
        if(map.containsKey("A")) {
            System.out.println("is map Contains key A? " + map.containsKey("A"));
        }
        if(map.containsValue(1)) {
            System.out.println("is map Contains value 1? " + map.containsKey("A"));
        }
        if(map.isEmpty()){
            System.out.println("is map empty? " + map.isEmpty());
        }
        System.out.println("map size = " + map.size());
        for(String key : map.keySet()) {
            System.out.println(key + "->" + map.get(key));
        }
        
        map.clear();
        if(map.isEmpty()){
            System.out.println("is map empty? " + map.isEmpty());
        }
    }
}
