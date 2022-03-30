class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0 || matrix == null)
            return false;
        int start = 0, row = matrix.length, col = matrix[0].length;
        int end = row * col - 1, mid;
        while (start <= end)
        {
            mid = (start + end)/2;
            if (matrix [mid / col][mid % col] == target)
                return true;
            if (matrix [mid / col][mid % col] < target)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return false;
    }
}