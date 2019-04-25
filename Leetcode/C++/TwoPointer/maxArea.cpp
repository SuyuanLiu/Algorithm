/*
Solution: 
- 双指针
- 定义指针i,j作为容器的左右边界， 容器的面积是(j - i) * min(height[i], height[j]);
- 下面介绍两种方法：

Solution 1：时间复杂度 O(n^2)
- j遍历数组，i在[0,j]内进行遍历；

Solution 2：时间复杂度 O(n)
- 要使得容器面积大，希望宽度和高度度都尽量大；
- 初始时，i,j分别放在数组的首尾，此时容器宽度最大；
- 因为h = min(height[i], height[j])，所以进入height[i] <= h这个while循环的条件就是，h=height[i],
  面积就是(j - i) * height[i]，那么就要尽量去找比较大的height[i],所以i++;
  同理，当h=height[j]时；
- 如果height[i] == height[j], 两个while循环都会进入，这个不会影响，因为最大面积边界要么是[i,j],要么在[i+1, j-1]之内；
  不可能是[i+1,j]或者[i,j+1],这两种情况的面积都小于[i,j];
*/
//  Solution 1
class Solution {
public:
    int maxArea(vector<int>& height) {
        int container = 0, i = 0, j = 1;
        while(j < height.size()){
            i = 0;
            while(i < j){
                int temp = (j - i) * min(height[i], height[j]);
                container = max(container, temp);
                i++;
            }
            j++;
        }
        return container;
    }
};


// Solution 2
class Solution {
public:
    int maxArea(vector<int>& height) {
        int container = 0, i = 0, j = height.size()-1;
        while(i < j){
            int h = min(height[i], height[j]);
            container = max(container, (j-i)*h);
            while(height[i] <= h and i < j){
                i++;
            }
            while(height[j] <= h and i < j){
                j--;
            }
        }
        return container;        
    }
};