package PGM.Lv3.단속카메라;

import java.util.*;

public class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparingInt(r -> r[1]));

        int endTime = -30001;
        int answer = 0;
        for (int[] route : routes) {
            if (endTime < route[0]) {
                endTime = route[1];
                answer++;
            }
        }

        return answer;
    }
}
