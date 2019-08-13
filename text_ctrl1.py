path_w = '/Users/toshiyuki.suzuki/Documents/GitHub/basil/test_w.txt'

s = 'New fileooooooooo\nadfadfadsfadfad\nadsflakjdfajdl'

with open(path_w, mode='w') as f:
    f.write(s)

with open(path_w) as f:
    print(f.read())
