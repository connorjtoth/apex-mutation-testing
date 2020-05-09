private class LessThanExpression {
    private Boolean v1 = 3 < 5;
    private static Boolean v2 = 3 < 5;

    private Boolean method() {
        if (3 < 5 && 5 < 3) {
            return v1;
        }
        else {
            return v2;
        }
    }
}