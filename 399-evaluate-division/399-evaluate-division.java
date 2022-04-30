class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, String> rootMap = new HashMap<>();  // {val, root}
        Map<String, Double> distMap = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String Ai = equations.get(i).get(0), Bi = equations.get(i).get(1);
            String r1 = find(rootMap, distMap, Ai);
            String r2 = find(rootMap, distMap, Bi);
            rootMap.put(r1, r2);
            distMap.put(r1, distMap.get(Bi) * values[i] / distMap.get(Ai));
        }
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String Cj = queries.get(i).get(0), Dj = queries.get(i).get(1);
            if (!rootMap.containsKey(Cj) || !rootMap.containsKey(Dj)) {
                res[i] = -1.0;
                continue;
            }
            String r1 = find(rootMap, distMap, Cj);
            String r2 = find(rootMap, distMap, Dj);
            if (!r1.equals(r2)) {
                res[i] = -1.0;
                continue;
            }
            res[i] = (double) distMap.get(Cj) / distMap.get(Dj);
        }
        return res;
    }
    
    String find(Map<String, String> rootMap, Map<String, Double> distMap, String s) {
        if (!rootMap.containsKey(s)) {
            rootMap.put(s, s);
            distMap.put(s, 1.0);
            return s;
        }
        if (rootMap.get(s).equals(s)) return s;
        // find further root, update it
        String lastP = rootMap.get(s);
        String p = find(rootMap, distMap, lastP);
        rootMap.put(s, p);
        distMap.put(s, distMap.get(s) * distMap.get(lastP));
        return p;
    }
}