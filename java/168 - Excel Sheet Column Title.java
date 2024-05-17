class Solution {
    public String convertToTitle(int columnNumber) {
        String result = "";
        Map<Integer, Character> mapping = new HashMap<>();
        char start = 'A';
        for(int i=0; i<26; i++){
            mapping.put(i+1, (char)(start+i));
        }
        
        while(columnNumber > 26){
            int residule = columnNumber%26;
            if (residule == 0){
                result = 'Z' + result;
                columnNumber -= 26;
            }
            else{
                result = mapping.get(residule) + result;
            }
            columnNumber /= 26;
        }

        result = mapping.get(columnNumber)+result;
        return result;
    }
}