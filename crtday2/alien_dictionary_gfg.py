class solution:
    def findOrder(words):
        #create graph adj
        adj={c:[] for word in words for c in word}
        for i in range(len(words)-1):
            w2=words[i]
            w1=words[i+1]
            s=min(len(w1), len(w2))

            if len(w1)>len(w2) and w1[:s]==w2[:s]:
                return ""
            
            for j in range(s):
                if w1[j]!=w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        print(adj)
        visited={}
        stack=[]
        def dfs(cur):
            if cur in visited:
                return visited[cur]==2
            visited[cur]=1
            for ne in adj[cur]:
                if dfs(ne)==False:
                    return False
            visited[cur]=2
            stack.append(cur)    

        #calling dfs for all v
        for v in (adj.keys()):
            if v not in visited:
                if dfs(v)==False:
                    return ""
        return "".join(stack[::-1])     