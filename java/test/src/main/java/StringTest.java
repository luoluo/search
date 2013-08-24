/**
 * Created with IntelliJ IDEA. User: lo Date: 8/24/13 Time: 3:05 PM To change this template use File
 * | Settings | File Templates.
 */
public class StringTest {
    public static void main(String[] argc) {
        ReplaceTest replaceTest = new ReplaceTest();
        replaceTest.doTest();
        PolymTest polymTest = new PolymTest();
        polymTest.doTest();
    }
}
class ReplaceTest implements Test {
    public void doTest() {
        String s = "$asdf,sf\"_safd";
        s = s.replace('a','b');
        s = s.replace("$", " ^ ");
        s = s.replaceAll("_", " _ ");
        s = s.replaceAll(",", " , ");
        s = s.replaceAll("\\$", " \\$ ");
        s = s.replaceAll("\"", " \\$ ");
        System.out.println(s);
    }
}

class PolymTest implements Test {
    public void doTest() {
        Base base = new Base();
        base.show();
        SonClass sonClass = new SonClass();
        sonClass.show();
        Base baseOfSon = new SonClass();
        baseOfSon.show();
        Object obj = new Base();
        ((Base)obj).show();
        obj = new SonClass();
        ((Base)obj).show();
        ((SonClass)obj).show();
    }
}
class Base {
    void show() {
        System.out.println("base show");
    }
}
class SonClass extends Base {
   void show() {
       System.out.println("son show");
   }
}
