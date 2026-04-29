class Solution(object):
    def ladderLength(self,bw, ew, wl):
        if ew not in wl:
            return 0
        wl.append(bw)
        adj = {}
        for word in wl:
            for i in range(len(word)):
                pattern  = word[:i] + "*" + word[i+1:]
                if pattern in adj:
                    adj[pattern].append(word)
                else:
                    adj[pattern] = [word]
        queue = [bw]
        visited = {bw}
        res = 1
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur == ew:
                    return res
                for i in range(len(cur)):
                    pattern = cur[:i] + "*" + cur[i + 1:]
                    for ne in adj[pattern]:
                        if ne not in visited:
                            visited.add(ne)
                            queue.append(ne)
            res+=1
        return 0        