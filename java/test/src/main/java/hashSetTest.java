import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

public class hashSetTest {
    private static final HashSet<String> set = new HashSet<String>() {
        {
            add("A");
            add("B");
            add("C");
            add("D");
            add("E");
        }
    };
    private static final List<String> list = new ArrayList<String>() {
        {
            add("A");
            add("B");
            add("C");
            add("D");
            add("E");
        }
    };

    // other ways to construct
    private static final HashSet<String> set2 = new HashSet<String>(list);
    private static final List<String> list2 = new ArrayList<String>(set);

    private static void basicTest() {
        if(set.isEmpty()) {
            System.out.println("is set empty? " + set.isEmpty());
        }
        if(set.contains("A")) {
            System.out.println("is set contains A? " + set.contains("A"));
        }

        Iterator i = set.iterator();
        while(i.hasNext()) {
            System.out.println("has values: " + i.next());
        }

        set.remove("A");
        if(set.contains("A")) {
            System.out.println("is set contains A? " + set.contains("A"));
        }

        System.out.println("set size = " + set.size());
    }

    private static void convertTest() {
        convert2List();
        convert2Array();
    }
    private static void convert2List() {
        System.out.println("Convert to List Test");
        System.out.println("original: " + set);
        ArrayList<String> setlist = new ArrayList<String>(set);
        System.out.println("convert2: " + setlist);
    }
    private static void convert2Array() {
        System.out.println("Convert to Array Test");
        System.out.println("original: " + set);
        //way 1: set => list => array
        ArrayList<String> setlist = new ArrayList<String>(set);
        String[] listArray = setlist.toArray(new String[0]);
        System.out.println("convert2: " + Arrays.toString(listArray));
        //way 2: set => array
        String[] setArray = set.toArray(new String[set.size()]);
        System.out.println("convert2: " + Arrays.toString(setArray));

    }
    public static void main(String[] argc) {
        basicTest();
        convertTest();
    }
}
