import java.io.*;
import java.util.*;

public final class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int MAXN = 4005;
    int minValue = Integer.MAX_VALUE;
    int[] deg = new int[MAXN];
    boolean[][] t = new boolean[MAXN][MAXN];

    String[] input = br.readLine().trim().split(" ");
    int n = Integer.parseInt(input[0]);
    int m = Integer.parseInt(input[1]);

    for(int i = 0; i < m; ++i) {
      String[] input2 = br.readLine().trim().split(" ");
      int a = Integer.parseInt(input2[0]);
      int b = Integer.parseInt(input2[1]);
      t[a][b] = t[b][a] = true;
      deg[a]++;
      deg[b]++;
    }

    for(int i = 1; i <= n; ++i) {
      for(int j = i + 1; j <= n; ++j) {
        if(t[i][j]) {
          for(int k = j + 1; k <= n; ++k) {
            if(t[i][k] && t[j][k])
              minValue = Math.min(minValue, deg[i] + deg[j] + deg[k]);
          }
        }
      }
    }

    if (minValue == Integer.MAX_VALUE) {
      System.out.println("-1");
    } else {
      System.out.println(minValue - 6);
    }
  }
}
