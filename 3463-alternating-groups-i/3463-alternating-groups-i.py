class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        if not colors:
            return 0
        
        n = len(colors)
        count = 0
        
        
        prev_color = colors[-1]
        
        for i in range(n):
            current_color = colors[i]
            next_color = colors[(i + 1) % n]
            
           
            if current_color != prev_color and current_color != next_color:
                count += 1
            
            prev_color = current_color
        
        return count