class TwoSum {
    public List<Integer> ds;
    public TwoSum() {
        ds = new ArrayList<>();
    }
    
    public void add(int number) {
        ds.add(number);
    }
    
    public boolean find(int value) {
        Set<Integer> pair = new HashSet<>();

        for(int el : ds){
            if(pair.contains(el)){
                return true;
            }
            pair.add(value-el);
        }
        return false;
    }
}