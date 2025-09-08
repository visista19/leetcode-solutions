import java.util.*;

class Pair{
    String first;
    int second;
    Pair(String _first, int _second){
        this.first=_first;
        this.second=_second;
    }
}
class Solution {
    public int wordLadderLength(String startWord, String targetWord,
                                String[] WordList) {
        // Code here
        Queue<Pair> q= new LinkedList<>();
        q.add(new Pair(startWord,1));
        Set<String> st= new HashSet<String>();
        int n=WordList.length;
        for(int i=0;i<n;i++){
            st.add(WordList[i]);
        }
        st.remove(startWord);
        while(!q.isEmpty()){
            String word = q.peek().first;
            int steps=q.peek().second;
            q.remove();
            if(word.equals(targetWord)==true) return steps;
            for(int i=0;i<word.length();i++){
                for(char ch='a';ch<='z';ch++){
                    char RBC[] = word.toCharArray();
                    RBC[i]=ch;
                    String replacedS= new String(RBC);
                    if(st.contains(replacedS)==true){
                        st.remove(replacedS);
                        q.add(new Pair(replacedS, steps+1));
                    }
                }
            }
        }
        return 0;
    }
}