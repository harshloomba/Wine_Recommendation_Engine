{"filter":false,"title":"deliciousrec.py","tooltip":"/deliciousrec.py","undoManager":{"mark":72,"position":72,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["from pydelicious import get_popular,get_userposts,get_urlposts","","def initializeUserDict(tag,count=5):","  user_dict={}","   # get the top count' popular posts","  for p1 in get_popular(tag=tag)[0:count]:","  # find all users who posted this","   for p2 in get_urlposts(p1['href']):","    user=p2['user']","    user_dict[user]={}","  return user_dict"," "," "," ",""],"id":1}],[{"start":{"row":14,"column":0},"end":{"row":34,"column":22},"action":"insert","lines":["","def fillItems(user_dict):"," all_items={}"," # Find links posted by all users"," for user in user_dict:","  for i in range(3):","   try:","    posts=get_userposts(user)","    break","   except:","    print \"Failed user \"+user+\", retrying\"","    time.sleep(4)","  for post in posts:","   url=post['href']","   user_dict[user][url]=1.0","   all_items[url]=1","# Fill in missing items with 0"," for ratings in user_dict.values( ):","  for item in all_items:","   if item not in ratings:","     ratings[item]=0.0"],"id":2}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":[" "],"id":3}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":[" "],"id":4}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["#"],"id":5}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"remove","lines":["#"],"id":6}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["#"],"id":7}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"remove","lines":["#"],"id":8}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["t"],"id":9}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["i"],"id":10}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["i"],"id":11}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["i"],"id":12}],[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["m"],"id":13}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["e"],"id":14}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["."],"id":15}],[{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["s"],"id":16}],[{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"remove","lines":["s"],"id":17},{"start":{"row":25,"column":9},"end":{"row":25,"column":14},"action":"insert","lines":["sleep"]}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"remove","lines":[")"],"id":18}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"remove","lines":["4"],"id":19}],[{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"remove","lines":["("],"id":20}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"remove","lines":["p"],"id":21}],[{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"remove","lines":["e"],"id":22},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"remove","lines":["e"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"remove","lines":["l"]},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"remove","lines":["s"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"remove","lines":["."]}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["e"],"id":23}],[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["m"],"id":24}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["i"],"id":25}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["t"],"id":26}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"remove","lines":["p"],"id":27}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["e"],"id":28}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["e"],"id":29}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["p"],"id":30}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["("],"id":31}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":[")"],"id":32}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["5"],"id":33}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":4},"action":"remove","lines":["  "],"id":35}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"remove","lines":["  "],"id":36}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":37}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":4},"action":"remove","lines":["  "],"id":39}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"remove","lines":["  "],"id":40}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":41}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":4},"action":"remove","lines":["  "],"id":43}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"remove","lines":["  "],"id":44}],[{"start":{"row":25,"column":16},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":45}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["5"],"id":46}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["4"],"id":47}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":4},"action":"remove","lines":["","    "],"id":49}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":[" "],"id":50}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":[" "],"id":51}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["#"],"id":52}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"remove","lines":["#"],"id":53}],[{"start":{"row":25,"column":17},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":54}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":19},"action":"remove","lines":["  "],"id":55},{"start":{"row":25,"column":17},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":4},"action":"remove","lines":["  "],"id":56}],[{"start":{"row":26,"column":2},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":4},"action":"remove","lines":["","    "],"id":59}],[{"start":{"row":26,"column":2},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":60}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":4},"action":"remove","lines":["  "],"id":61}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["#"],"id":62}],[{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["p"],"id":64}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["r"],"id":65}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["i"],"id":66}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["n"],"id":67}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["t"],"id":68}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":[" "],"id":69}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["p"],"id":70}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["2"],"id":71}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["'"],"id":72}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["'"],"id":85}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1436841714172,"hash":"c7094f6a97f712c9f376bc0aa9f8b92ab98f1f5d"}