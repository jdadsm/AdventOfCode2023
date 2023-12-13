def main():
    with open("day5/input.txt",'r') as file:
        input = file.readlines()
        
    seeds = input[0].removeprefix("seeds:").split()
    seeds = [int(seed) for seed in seeds]
    
    new_seeds = []
    for i in range(len(seeds)//2):
        new_seeds.append(rangeNumber(seeds[i*2],seeds[i*2+1]))
        
    input = input[1:]
    
    maps = []
    while input:
        line = input[0].removesuffix("\n")
        input = input[1:]
        if line == "":
            continue
        if line.endswith("map:"):
            maps.append([])
        elif line[-1].isdigit():
            maps[-1].append(line.split())
    
    
    values = new_seeds
    for map in maps:
        already_mapped = []
        while values:
            value = values.pop(0)
            leftovers = []
            for line in map:
                destination_start = int(line[0])
                source_start = int(line[1])
                source_range = int(line[2])
                in_bounds,out_of_bounds = value.intersect(source_start,source_range)
                already_mapped.extend([rn.map_to_next(destination_start-source_start) for rn in in_bounds])
                leftovers.extend(o for o in out_of_bounds if o not in leftovers)
            if None not in leftovers:
                common_part = leftovers[0]
                for rn in leftovers[1:]:
                    common_part = common_part.get_common_part(rn)
                    if not common_part:
                        break
                if common_part:
                    already_mapped.append(common_part)
        values.extend(already_mapped)
        
    min_location = values[1].start
    for v in values:
        if v.start < min_location and v.start:
            min_location = v.start
            
    print(min_location)
                    
    
class rangeNumber:
    def __init__(self,number,range):
        self.start = number
        self.range = range
        self.end = number+range-1
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        if self.start==self.end:
            return f"{self.start}"
        return f"({self.start}-{self.end})"
    
    def map_to_next(self,diff):
        return rangeNumber(self.start+diff,self.range)
    
    def get_common_part(self,rn):
        final_start = self.start
        final_end = self.end
        if rn.start > self.start:
            final_start = rn.start
        if rn.end < self.end:
            final_end = rn.end
        if final_start > final_end:
            return None
        return rangeNumber(final_start,final_end-final_start)
    
    def intersect(self,s,r):
        e = s+r
        
        if self.end < s or self.start > e:
            return [],[self]
        
        if self.start >= s:
            if self.end < e:
                return [self],[None]
            elif self.end >= e:
                return [rangeNumber(self.start,e-self.start)],[rangeNumber(e,self.end-e)]
        elif self.start < s:
            if self.end < e:
                return [rangeNumber(s,self.end-s)],[rangeNumber(self.start,s-self.start)]
            elif self.end >= e:
                return [rangeNumber(s,e-s)],[rangeNumber(self.start,s-self.start),rangeNumber(e,self.end-e)]
        
if __name__ == "__main__":
    main()