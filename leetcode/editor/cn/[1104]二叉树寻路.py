# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。 
# 
#  如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记； 
# 
#  而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。 
# 
#  
# 
#  给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：label = 14
# 输出：[1,3,4,14]
#  
# 
#  示例 2： 
# 
#  输入：label = 26
# 输出：[1,2,6,10,26]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= label <= 10^6 
#  
#  Related Topics 树 数学 二叉树 
#  👍 124 👎 0
from typing import List
import math
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        第i层编号为[2**i, 2 ** (i + 1) - 1]
        偶数层顺序排号，奇数层逆序。
        如果都是顺序排号的话，那么找其父节点就i//2
        如果lable位于奇数层k的话，父节点=(2 ** k + 2 ** (k + 1) - 1 - label))) // 2
        如果label位于偶数层k的话，父节点=2 ** k - 1 - (label // 2 - 2 ** (k - 1))
        """
        ans = [label]
        k = int(math.log2(label))
        while k:
            if k % 2:
                ans.append((2 ** k + 2 ** (k + 1) - 1 - ans[-1]) // 2)
            else:
                ans.append(2 ** k - 1 - (ans[-1] // 2 - 2 ** (k - 1)))
            k -= 1
        return ans[::-1]
# leetcode submit region end(Prohibit modification and deletion)
label = 14
print(Solution().pathInZigZagTree(label))