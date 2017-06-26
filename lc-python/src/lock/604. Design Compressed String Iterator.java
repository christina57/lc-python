/*
604. Design Compressed String Iterator

Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
*/

public class StringIterator {
    
    private int marker = 0;
    private String compressed = "";
    private char buffer = ' ';
    private int buffer_count = 0;
    
    public StringIterator(String compressedString) {
        compressed = compressedString;
    }
    
    public char next() {
        if(hasNext()){
            if(buffer_count == 0){
                buffer = compressed.charAt(marker);
                int idx = marker+1;
                while(idx < compressed.length() && Character.isDigit(compressed.charAt(idx))){
                    idx++;
                }
                buffer_count = Integer.parseInt(compressed.substring(marker+1, idx));
                marker = idx;
            }
            buffer_count--;
            return buffer;
        } else {
            return ' ';
        }
    }
    
    public boolean hasNext() {
        return buffer_count != 0 || marker < compressed.length();
    }
}

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator obj = new StringIterator(compressedString);
 * char param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */