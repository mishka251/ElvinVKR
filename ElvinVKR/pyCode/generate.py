nums =[i/10 for i in range(0,11)]

percs2 =[[x,y] for x in nums for y in nums if x+y==1]
percs3 =[[x,y,z] for x in nums for y in nums for z in nums if x+y+z==1]
percs4 =[[x,y,z, x1] for x in nums for y in nums for z in nums for x1 in nums if x+y+z+x1==1]
percs5 =[[x,y,z, x1, y1] for x in nums for y in nums for z in nums for x1 in nums  for y1 in nums if x+y+z+x1+y1==1]
percs6 =[[x,y,z, x1, y1, z1] for x in nums for y in nums for z in nums for x1 in nums  for y1 in nums for z1 in nums if x+y+z+x1+y1+z1==1]

percsAll = {2:percs2, 3:percs3, 4:percs4, 5:percs5, 6:percs6}