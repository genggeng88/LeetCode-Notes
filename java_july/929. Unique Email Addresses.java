class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> set = new HashSet<>();

        for (String email : emails) {
            int idx = email.indexOf('@');
            String local = email.substring(0, idx);
            String domain = email.substring(idx);

            int plusIdx = local.indexOf('+');
            if (plusIdx != -1) {
                local = local.substring(0, plusIdx);
            }
            
            local = local.replace(".", "");
            set.add(local+domain);
        }
        return set.size();
    }
}