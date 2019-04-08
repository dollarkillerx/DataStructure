class Factory{
    public static Operation createFactory(String use){
        Operation oper = null;
        switch (use) {
            case "+":
                oper = new OperationAdd();
                break;
            case "-":
                oper = new OperationSub();
                break;
            case "*":
                oper = new OperationSub();
                break;
            default:
                break;
        }
        return oper;
    }
}