import java.io.*;
import java.util.*;

public final class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int MAXN = 5010;

    int[][] dp = new int[MAXN][MAXN];

    int n = Integer.parseInt(br.readLine());
    String[] input = br.readLine().trim().split(" ");
    int q = Integer.parseInt(br.readLine());

    for (int i = 0; i < n; i++) {
      dp[0][i] = Integer.parseInt(input[i]);
    }
    
    for (int i = 1; i < n; i++) {
      for (int j = 0; j <= n - i; j++) {
        dp[i][j] = dp[i - 1][j + 1] ^ dp[i - 1][j];
      }
    }
  
    for (int i = 1; i < n; i++) {
      for (int j = 0; j < n - i; j++) {
        dp[i][j] = Math.max(dp[i][j], Math.max(dp[i - 1][j], dp[i - 1][j + 1]));
      }
    }

    for (int i = 0; i < q; i++) {
      int l, r;
      String[] input2 = br.readLine().split(" ");
      l = Integer.parseInt(input2[0]);
      r = Integer.parseInt(input2[1]);
      --l;
      int len = r - l - 1;
      System.out.println(dp[len][l]);
    }
  }
}
