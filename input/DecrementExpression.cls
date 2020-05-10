private class LeftShiftExpression {
    private Integer v1 = 3--
    private static Integer v2 = --(3 << 5)--;

    private Integer method() {
        if (3-- + 5 && 5-- << 3) {
            return --v1;
        }
        else {
            return v2--;
        }
    }
}