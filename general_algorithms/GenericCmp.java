import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * generic compare class
 */
abstract class Cmp<T> {
    public abstract int cmp(T a, T b);
}

/**
 * generic class
 */
class Val {
    public int num = 0;

    Val(int num) {
        this.num = num;
    }

    @Override
    public String toString() {
        return this.num + "";
    }

}

public class GenericCmp {
    public static void main(String args[]) {
        ArrayList<Val> a = new ArrayList<>();
        a.add(new Val(4));
        a.add(new Val(2));
        a.add(new Val(3));

        ArrayList<Val> b = new ArrayList<>();
        b.add(new Val(2));
        b.add(new Val(2));
        b.add(new Val(3));

        testFunc(a, b, new Cmp<Val>() {
            @Override
            public int cmp(Val a, Val b) {
                if (a.num < b.num) {
                    return -1;
                }
                return 0;
            }
        });

        ArrayList<String> a1 = new ArrayList<>();
        a1.add("a");

        ArrayList<String> b1 = new ArrayList<>();
        b1.add("a");

        testFunc(a, b, new Cmp<String>() {
            @Override
            public int cmp(String a, String b) {
                return a.equals(b) ? 0 : 1;
            }
        });

    }

    static void testFunc(List a, List b, Cmp cmp) {
        System.out.print(cmp.cmp(a.get(0), b.get(0)));
    }
}