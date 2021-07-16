<h2>611. Valid Triangle Number</h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, return <em>the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>

### My Solution
- First, sort the given nums array
- start from index 2, pick l, r index.
- if nums[l] + nums[r] > nums[i], it can be a valid triangle. index between l and r is greater than nums[l] so all nums between l and r are also valid.
- if valid triangle, move r to left. else move l to right.
- keep going until l > r