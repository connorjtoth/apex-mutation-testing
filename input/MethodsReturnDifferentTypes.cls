private class MethodsReturnDifferentTypes {
    private Boolean v1 = 3 < 5;
    private static Boolean v2 = 3 < 5;

    private void method1() {}

    private void method1() {
        return;
    }

    private Boolean method2() {
        return true;
    }

    private Decimal method3() {
        Decimal dec = 0.5;
        return dec;
    }

    private Integer method4() {
        int a = 3;
        return a;
    }

    private String method5() {
        if (3 << 5 < 5) {
            return 'maybe we return here?';
        }
        else {
            return 'maybe we return a different' + 'place';
        }
        return null;
    }

    private String method6() {
        if (3 << 5 < 5) {
            return 'maybe we return here?';
        }
        else {
            return 'maybe we return a different' + 'place';
        }
        return (null);
    }

    private String method7() {
        String a = null;
        if (3 << 5 < 5) {
            a = 'not null';
        }
        return a;
    }
}