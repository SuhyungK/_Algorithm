// 돌 게임 3

package Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_9657 {
    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n+4];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 1;
        dp[4] = 1;

        for (int i = 5; i < n+1; i++) {
            if (dp[i-1] == 2 || dp[i-3] == 2 || dp[i-4] == 2) {
                dp[i] = 1;
            } else {
                dp[i] = 2;
            }
        }

        if (dp[n] == 2) {
            System.out.println("CY");
        } else {
            System.out.println("SK");
        }
    }
}
