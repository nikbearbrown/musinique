### CHAPTER 3: Sorting — Making Order

**Core Claim:** Sorting is the foundational operation of information processing, but it obeys harsh diseconomies of scale (Big-O notation reveals that sorting costs superlinearly). The optimal approach for most human sorting problems is *less* sorting than intuition suggests: Bucket Sort exploits knowledge of the distribution, Merge Sort parallelizes efficiently, and in many cases search beats sort. Sports tournaments instantiate sorting algorithms with distinct trade-offs between efficiency and noise-robustness.

**Supporting Evidence:**
- Herman Hollerith's census tabulation machines (1890) as origins of modern computing
- Big-O notation: O(1) constant, O(N) linear, O(N log N) linearithmic, O(N²) quadratic, O(2^N) exponential, O(N!) factorial
- Bubble sort and insertion sort: both O(N²); Obama's famous rejection of bubble sort
- Merge sort (von Neumann 1945): O(N log N); proven optimal for comparison-based sorting
- Bucket Sort (Preston Sort Center, King County Library): linear time O(N) when bucket distribution is known; requires domain knowledge of the data
- Steve Whitaker study (2011): email filing by hand ("Am I wasting my time organizing email?")—conclusion: yes, empirically
- Lewis Carroll's 1883 critique of single-elimination tennis tournaments: silver medal is "a lie" with probability (1 - 16/31)
- Comparison-counting sort (round robin): most noise-robust sorting algorithm known; corresponds to regular season standings in sports
- Noisy comparator problem: bubble sort is more robust than merge sort under noise—its "inefficiency" becomes a virtue

**Logical Method:** Algorithmic complexity analysis + cross-domain structural analogy (sports = sorting algorithms) + empirical studies on email behavior.

**Logical Gaps:**
- The "search beats sort" conclusion for email and bookshelves is empirically supported by Whitaker's study, but the conditions under which it holds (fast search tools, sparse retrieval need) are not fully specified. In contexts where search is slow or imprecise, sorting still wins.
- The noise-robustness argument for bubble sort is theoretically interesting, but the chapter presents it without quantitative comparison to alternatives. For moderate noise levels, which algorithm is actually superior is an empirical question not answered here.
- The sports-as-sorting-algorithm framing is insightful but trades on a structural similarity that breaks down at the level of purpose: sports are entertainment products where "making order" is secondary to generating compelling contests. The authors acknowledge this but then use sports to illustrate algorithmic principles as if purpose didn't matter to the analysis.
- Dodgson's critique of single elimination is mathematically correct but the proposed fix (his own variant) is called "cumbersome" without analysis of whether it actually solves the problem better than alternatives.

**Methodological Soundness:** Strong on computational theory; the applied analogies hold at the structural level but require care about purpose differences.

---
