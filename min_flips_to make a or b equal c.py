class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        b_a,b_b,b_c=format(a,"b"),format(b,"b"),format(c,"b")
        
        m=max(len(b_a),len(b_b),len(b_c))
        b_a,b_b,b_c=b_a.zfill(m),b_b.zfill(m),b_c.zfill(m)
        
        flips=0
        
        for i in range(m):
            
            if b_c[i]=='0':
                
                if b_a[i]=='0' and b_b[i]=='0':
                    print("c,a,b,f",b_c[i],b_a[i],b_b[i],flips)
                    continue
                if b_a[i]=='1':
                    
                    flips+=1
                if b_b[i]=='1':
                    flips+=1
            if b_c[i]=='1':
                if b_a[i]=='1' or b_b[i]=='1':
                    print("c,a,b,f",b_c[i],b_a[i],b_b[i],flips)
                    continue
                else: 
                    flips+=1
            print("c,a,b,f",b_c[i],b_a[i],b_b[i],flips)
        print(flips)
        return flips
            