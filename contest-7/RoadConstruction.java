import java.io.*;
import java.util.*;

public final class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int MAXN = 1005;
    boolean[] in = new boolean[MAXN];

    String[] input = br.readLine().trim().split(" ");
    int n = Integer.parseInt(input[0]);
    int m = Integer.parseInt(input[1]);

    for (int i = 0; i < m; i++) {
      String[] input2 = br.readLine().trim().split(" ");
      int u = Integer.parseInt(input2[0]);
      int v = Integer.parseInt(input2[1]);
      in[u] = true;
      in[v] = true;
    }

    int x = 1;
    while (in[x]) {
      x++;
    }

    System.out.println(n - 1);

    for (int i = 1; i < x; ++i) {
      System.out.println(i + " " + x);
    }

    for (int i = x + 1; i <= n; ++i) {
      System.out.println(x + " " + i);
    }
  }
}
