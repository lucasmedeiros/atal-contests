import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().trim().split(" ");

        int rows = Integer.parseInt(input[0]);
        int cols = Integer.parseInt(input[1]);

        int[][] m = new int[rows][cols];

        for (int i = 0; i < rows; i++){
            String m_line = br.readLine();
            for (int j = 0; j < cols; j++){
                m[i][j] = m_line.charAt(j);
            }
        }
        
        ArrayList<ArrayList<Integer>> g = new ArrayList<>();
        
        for (int i = 0; i <= rows * cols; i++){
            g.add(new ArrayList<>());
        }

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                int point1 = (i) * cols + j + 1;
                if(i - 1 >= 0 && m[i - 1][j] == m[i][j]){
                    int point2 = (i - 1) * cols + j + 1;
                    g.get(point1).add(point2);
                    g.get(point2).add(point1);
                }
                if(j - 1 >= 0 && m[i][j - 1] == m[i][j]){
                    int point2 = i * cols + (j - 1) + 1;
                    g.get(point1).add(point2);
                    g.get(point2).add(point1);
                }
            }
        }
        
        boolean[] visited_array = new boolean[rows*cols+1];
        
        for (int i = 1; i <= rows * cols; i++){
            if(visited_array[i] == false){
                Pair ans = dfs(g,i,visited_array);
                int edges = ans.getDegreeSum()/2;
                if(edges > ans.getVertices()-1){
                    System.out.println("Yes");
                    return;
                }
            }
        }
        
        System.out.println("No");
    }
    public static Pair dfs(ArrayList<ArrayList<Integer>> g, int start, boolean[] visited_array) {
        int vertices = 1;
        int degreeSum = g.get(start).size();
        
        visited_array[start] = true;

        for (int i = 0; i < g.get(start).size(); i++){
            if (visited_array[g.get(start).get(i)] == false) {
                Pair smallAns = dfs(g, g.get(start).get(i), visited_array);
                vertices += smallAns.getVertices();
                degreeSum += smallAns.getDegreeSum();
            }
        }
        Pair ans = new Pair(vertices, degreeSum);
        return ans;
    }
}

class Pair {
    private int vertices;
    private int degreeSum;

    public Pair(int vertices, int degreeSum) {
        this.vertices = vertices;
        this.degreeSum = degreeSum;
    }

    public int getVertices() {
        return this.vertices;
    }

    public int getDegreeSum() {
        return this.degreeSum;
    }
}
