public class FirstNonRepeated {
    public static Character firstNonRepeated(String source) {
        for (int i = 0; i < source.length(); i++) {
            boolean repeated = false;
            for (int j = 0; j < source.length(); j++) {
                if (i != j && source.charAt(i) == source.charAt(j)) {
                    repeated = true;
                    break;
                }
            }
            if (!repeated) {
                return source.charAt(i);
            }
        }
        return null;
    }
}