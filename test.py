def func(a, b, c, d=0, e=1, *f, g, h=3, **i):
  print(a,b,c,d,e, f, g, h, i)
  

func(1,2,3,4,5,6,7,8, g=10, x='a', y='b', z='c')
# func(1,2,3)