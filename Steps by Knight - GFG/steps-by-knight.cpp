// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution 
{
    private:
    bool isvalid(vector<vector<int>>& board, int i, int j) {
        int N = board.size();
        if(i >= 0 and i < N and j >= 0 and j < N and board[i][j] == -1) return true;
        return false;
    }
    
    public:
    //Function to find out minimum steps Knight needs to reach target position.
	int minStepToReachTarget(vector<int>&KnightPos,vector<int>&TargetPos,int N)
	{
	    vector<int> r{1,2,1,2,-1,-2,-1,-2};
	    vector<int> c{2,1,-2,-1,2,1,-2,-1};
	    vector<vector<int>> board(N, vector<int>(N, -1));
	    
	    queue<vector<int>> q;
	    q.push({N-KnightPos[1], KnightPos[0]-1});
	    int moves = 0; board[N-KnightPos[1]][KnightPos[0]-1] = 0;
	    
	    while(!q.empty()) {
	        int n = q.size();
	        while(n--) {
	            auto p = q.front();
	            int i = p[0], j = p[1];
	            q.pop();
	            
	            if(i == N-TargetPos[1] and j == TargetPos[0]-1) return moves;
	            
	            for(int m=0; m<8; m++) {
	                if(isvalid(board, i+r[m], j+c[m])) {
	                    q.push({i+r[m],j+c[m]});
	                    board[i+r[m]][j+c[m]] = moves+1;
	                }
	            }
	        }
	        moves++;
	    }
	    
	    return moves;
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		vector<int>KnightPos(2);
		vector<int>TargetPos(2);
		int N;
		cin >> N;
		cin >> KnightPos[0] >> KnightPos[1];
		cin >> TargetPos[0] >> TargetPos[1];
		Solution obj;
		int ans = obj.minStepToReachTarget(KnightPos, TargetPos, N);
		cout << ans <<"\n";
	}
	return 0;
}  // } Driver Code Ends