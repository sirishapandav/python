class solution:
    def asteriodCollision(self,asteroids: list[int])->int:
        st=[]
        for ast in asteroids:
            while st and ast<0 and st[-1]>0:
                if -ast>st[-1]:
                    st.pop()
                    continue
                elif -ast==st[-1]:
                    st.pop()
                break
            else:
                st.append(ast)
        return st
            
