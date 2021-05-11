import java.io.*;
import java.util.*;

public final class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int MAXN = 200005;

    int[] dist = new int[MAXN];
    int[] cuts = new int[MAXN];

    int n;

    n = Integer.parseInt(br.readLine());

    String[] input = br.readLine().split(" ");

    for (int i = 1; i <= n; i++) {
      cuts[i] = Integer.parseInt(input[i - 1]);
    }

    for (int i = 0; i < n + 1; i++) dist[i] = -1;

    ArrayList<Integer> queue = new ArrayList<Integer>();
    queue.add(1);
    dist[1] = 0;

    while(queue.size() > 0) {
      int k = queue.remove(0);

      if (k + 1 <= n && dist[k + 1] == -1) {
        dist[k + 1] = dist[k] + 1;
        queue.add(k + 1);
      }

      if (dist[cuts[k]] == -1) {
        dist[cuts[k]] = dist[k] + 1;
        queue.add(cuts[k]);
      }

      if(k - 1 > 0 && dist[k - 1] == -1) {
        dist[k - 1] = dist[k] + 1;
        queue.add(k - 1);
      }
    }

    for (int i = 1; i <= n; i++) {
      System.out.print(dist[i] + " ");
    }
  }
}
