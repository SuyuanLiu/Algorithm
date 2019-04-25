/*
Solution 1:
- 暴力求解，时间复杂度 O(n^2)，空间复杂度 O(1);
- 求总的雨水量，实际上就是看每个bar能存储多少水，每个bar存储的水量取决于其左右两侧最大值中的最小值；
- 只要针对每个bar（遍历n次)，去看它左右两侧的最值（遍历n次）；

Solution 2：
- 动态规划，时间复杂度 O(n)，空间复杂度 O(n);
- 维护一个container数组，用来存放对于当前bar左右侧最大值中的最小值；
- 对height遍历两次，先从左到右，此时container中存放当前bar左侧的最大值；再从右到左遍历，找到当前bar右侧的最大值；

Solution 3：
- (目前不是很理解)有点贪心的思想，时间复杂度O(n),空间复杂度 O(1);
- 参考：https://blog.csdn.net/linhuanmars/article/details/20888505，以及LeetCode Disscus里面的高票答案；
- 从两边向中间扫描，核心思想是，向中间夹逼时能确定接下来移动另一侧窗口不可能使得结果变得更好，所以每次能确定移动一侧指针；
*/

// -------------Solution 1 --------------------
class Solution {
public:
	int trap(vector<int>& height) {
		if (height.size() < 3)   return 0;
		int res = 0;
        for(int i = 1; i + 1 < height.size(); i++){
            int j = i - 1;
            int left = 0, right = 0;
            while(j >= 0){
                if(height[j] > left)
                    left = height[j];
                j--;
            }
            j = i + 1;
            while(j < height.size()){
                if(height[j] > right)
                    right = height[j];
                j++;
            }
            res += min(left, right) > height[i] ? min(left, right) - height[i] : 0;
        }
        return res;        
	}
};

// -------------Solution 2 --------------------
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() < 3)
            return 0;
        int res = 0;
        vector<int> container(height.size());
        int maxRight = height[height.size()-1];
        container[0] = height[0]; container[height.size()-1] = height[height.size()-1];
        for(int i = 1; i + 1 < height.size(); i++){
            container[i] = height[i] > container[i-1] ? height[i] : container[i-1];
        }
        for(int i = height.size() - 2; i > 0; i--){
            maxRight = height[i] > maxRight ? height[i] : maxRight;
            res += min(container[i], maxRight) > height[i] ? min(container[i], maxRight) - height[i] : 0;
        }
        return res;
    }
};

// -------------Solution 3 --------------------
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() < 3)
            return 0;
        int res = 0;
        int left = 0, right = height.size() - 1;
        int maxLeft = 0, maxRight = 0;
        while(left < right){
            if(height[left] < height[right]){
                if(height[left] > maxLeft) 
                    maxLeft = height[left];
                else
                    res += maxLeft - height[left];
                left++;
            }
            else{
                if(height[right] > maxRight)
                    maxRight = height[right];
                else
                    res += maxRight - height[right];
                right--;
            }
        }
        return res;
    } 
};