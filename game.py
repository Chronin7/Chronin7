# import do not tuch
import random
import util_functions
# Maps do not tuch
mid=[["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","l","i1","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","h","h","h","l","h","h","speshal","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","h","h","h","h","ni1","l","l","h","h","i2","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","h","u","h","h","l","l","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","u","u","h","l","h","s","l","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","u","c","h","b","h","h","l","l","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","h","h","h","h","l","h","h","h","h","h","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","u","f","f","f","f","f","f","f","f","f","h","u","h","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","h","f","f","f","f","f","s","f","f","f","f","f","h","h","h","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","f","f","f","f","c","f","f","f","t","p","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","f","f","s","f","f","f","f","f","f","f","f","p","f","f","ni2","f","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","i3","f","f","f","f","f","f","f","i4","p","p","p","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","r","f","f","f","f","f","f","f","f","f","p","p","p","f","f","f","f","f","f","f","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","t","p","r","f","r","f","f","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","p","t","w","w","i5","w","w"],
["w","w","w","w","w","w","p","f","b","r","f","f","p","p","p","p","p","p","c","u","f","f","f","f","f","f","f","f","f","f","w","w","f","f","f","w"],
["w","w","w","w","w","f","p","f","f","t","r","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","b","w","f","p","f","f","w"],
["w","w","w","w","f","p","p","p","f","f","f","b","r","c","p","spawn","p","p","p","p","f","f","f","f","f","f","f","f","r","s","p","p","p","p","f","w"],
["w","w","w","w","f","p","p","p","p","p","p","p","p","r","t","t","p","p","p","p","r","f","f","f","f","f","f","f","r","p","t","p","p","p","f","w"],
["w","w","w","w","f","c","f","f","p","p","p","p","p","r","t","t","r","r","p","r","p","f","f","f","f","f","f","f","f","r","p","p","p","p","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","r","r","p","c","r","p","t","f","f","s","f","f","f","c","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","p","p","p","p","p","p","p","p","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","f","f","f","f","f","f","f","f","f","f","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w"],
["w","w","w","w","w","s","s","f","f","s","s","s","s","s","p","p","p","p","p","p","f","f","f","f","f","f","f","f","f","f","f","f","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","s","w","w","s","s","s","f","f","f","f","f","f","f","f","f","f","f","w","aw","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","w","s","s","s","s","w","w","w","w","s","s","s","f","f","f","f","s","s","s","s","s","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","s","s","s","s","s","s","s","s","s","i7","s","s","s","w","w","aw","aw","i6","aw","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","s","s","w","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","w","w","aw","aw","aw","aw","aw","aw","w","w","w"],
["w","w","w","w","w","i8","s","s","w","w","w","s","s","s","s","s","s","s","s","t","s","s","s","s","w","w","w","w","aw","aw","ni3","aw","aw","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","s","s","s","s","s","s","s","s","s","s","s","s","w","w","w","w","w","w","aw","aw","aw","w","w","w","w"],
["w","w","w","w","w","s","s","w","w","w","w","w","s","s","s","s","s","s","s","ni4","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","s","s","s","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]
upper=[["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","sk","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","sk","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","b","b","b","g","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","b","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","g","sk","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","boss","boss","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","boss","boss","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","boss","boss","boss","boss","u","u","u","u","u","u","u","u","u","u","g","","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","boss","boss","u","u","u","u","u","u","u","u","u","u","g","s","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","puzzle","g","g","g","ni","u","u","u","u","u","u","u","u","u","u","g","u","u","b","b","b","g","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","g","g","g","g","g","u","u","u","u","u","u","u","u","u","u","g","g","g","b","b","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","g","spehsal","g","g","u","u","u","u","u","u","u","u","u","u","g","t","s","g","g","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","g","g","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","b","g","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","b","u","u","u","u","u","u","u","u","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","b","g","g","g","g","g","g","g","u","u","u","u","g","puzzle","g","speshal","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","s","g","b","u","g","ni","g","g","g","g","b","u","u","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","u","u","u","g","g","u","u","u","b","b","g","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","u","u","u","u","u","u","g","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","g","g","u","u","u","u","g","g","u","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","b","g","g","g","g","g","g","g","u","u","u","u","g","puzzle","g","speshal","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","g","s","g","b","u","g","ni","g","g","g","g","b","u","u","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","u","u","u","u","g","g","u","u","u","b","b","g","g","g","g","g","g","g","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","g","g","g","g","g","g","u","u","u","g","g","u","u","u","u","u"],
["u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u","u"]]
underground=[["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","u","u","u","u","u","u","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","u","u","u","h","h","h","l","i","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","u","h","u","h","h","u","h","l","l","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","h","u","h","u","h","h","h","h","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","h","u","h","h","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","u","h","h","c","h","u","h","u","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","h","h","h","h","h","u","h","h","u","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","u","h","h","h","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","u","h","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","c","g","u","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","g","u","h","h","u","g","g","g","ui","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","g","g","g","u","g","u","i","g","g","g","ni","u","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","i","g","g","g","g","g","g","u","g","g","u","u","u","g","g","ui","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","u","g","g","g","g","g","g","u","g","u","i","g","g","u","u","g","g","g","u","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","g","u","g","g","boss teleport","u","g","g","g","g","g","g","g","i","u","u","u","u","u","u","u","u","w","w"],
["w","w","w","w","w","w","u","g","g","g","g","g","u","g","g","g","g","u","c","u","g","g","g","g","g","u","g","g","g","g","g","g","g","ni","u","w"],
["w","w","w","w","w","u","g","g","g","g","g","u","g","g","g","g","g","g","u","u","g","g","g","g","g","u","g","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","g","g","g","g","g","g","u","g","c","g","g","g","g","g","g","g","g","g","g","g","i","u","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","u","w"],
["w","w","w","w","u","c","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","g","g","g","g","u","g","g","g","g","g","g","g","u","w","w"],
["w","w","w","w","u","g","g","g","g","g","g","g","g","g","u","g","g","c","g","g","g","g","g","g","g","u","t","c","g","g","g","g","u","w","w","w"],
["w","w","w","w","u","g","g","i","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","u","w","w","w"],
["w","w","w","w","w","u","g","g","g","g","g","u","u","g","g","g","u","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","g","u","w","w","u","g","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","u","g","g","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","g","c","u","w","w","w","w","w","u","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","g","g","u","w","w","w","u","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","i","u","w","w","w","u","g","g","g","g","g","i","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","u","g","g","g","g","g","g","g","g","g","g","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","u","u","w","w","w","w","w","u","u","u","u","u","u","u","g","g","i","u","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","u","u","u","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]
#dictonarys do not tuch
location_dict={
"h":{"name":"hot land","description":"a land of heat","special":None},
"l":{"name":"lava land","description":"tell the maker","special":"not valid location"},	
"w":{"name":"water","description":"tell the maker","special":"Not valid location"},
"i":{"name":"item","description":["You found an item!","youv already sherched here"],"special":"item"},
"ni":{"name":"nessasary item","description":["You found a nessasary item!","youv already sherched here"],"special":"item"},
"c":{"name":"cave","description":"a dark cave","special":["desend","ascend"]},
"sk":{"name":"sky lift","description":"a sacred place with powerfull lifting runes","special":["ascend","desend"]},
"b":{"name":"bridge","description":"a rickety bridge","special":None},
"t":{"name":"town","description":"a small town","special":"town"},
"f":{"name":"feild","description":"a wide open feild","special":None},
"r":{"name":"river","description":"a flowing river","special":"passable with gem of water"},
"spawn":{"name":"spawn point","description":"the place where your adventure begins","special":None},
"s":{"name":"snow","description":"a cold snowy area","special":None},
"u":{"name":"unreachable","description":"tell the maker","speshal"}
}
monster_dict={
"dragon":{"tier":2,"hp":150,"dmg":30,"drops":{"name":"dragon tooth","quantity":1,"useable":False,"effect":{"buff":50,"xp":50}},"resistance":"fire","description":"A large fire-breathing dragon.","speshal spwan location":["~water","~lava","hot","~river","~snow"]},
"blob":{"tier":1,"hp":80,"dmg":15,"drops":{"name":"slime gel","quantity":1,"useable":True,"effect":{"heal":20,"xp":25}},"resistance":"water","description":"A gooey blob that oozes around.","speshal spwan location":["~water","~lava","~river","~snow"]},
"orc":{"tier":2,"hp":120,"dmg":25,"drops":{"name":"orc tusk","quantity":1,"useable":True,"effect":{"buff":10,"xp":25}},"resistance":"wind","description":"A brutish orc warrior.","speshal spwan location":["~lava","~water","~river"]},
"troll":{"tier":2,"hp":130,"dmg":28,"drops":{"name":"troll club","quantity":1,"useable":False,"effect":{"buff":10,"xp":50}},"resistance":"wind","description":"A large and strong troll.","speshal spwan location":["~lava","~water","bridge","~river"]},
"goblin":{"tier":1,"hp":30,"dmg":12,"drops":{"name":"goblin ear","quantity":1,"useable":False,"effect":{"buff":5,"xp":15}},"resistance":"darkness","description":"A sneaky goblin.","speshal spwan location":["~water","~lava","cave","~river"]},
"knight":{"tier":3,"hp":200,"dmg":40,"drops":{"name":"knight's shield","quantity":1,"useable":False,"effect":{"buff":20,"xp":75}},"resistance":"light","description":"A heavily armored knight.","speshal spwan location":["~water","~lava","town","bridge","~river"]},#if spawn on brige have speshal dialog (none shall pass, its only a flesh wound, tis but a scratch, ive had worse)
"construct":{"tier":3,"hp":180,"dmg":35,"drops":{"name":"mechanical gear","quantity":1,"useable":False,"effect":{"buff":15,"xp":60}},"resistance":"electric","description":"A mechanical construct brought to life.","speshal spwan location":["~water","~lava","cave","~river"]},
"Animated statue":{"tier":2,"hp":140,"dmg":22,"drops":{"name":"stone shard","quantity":1,"useable":False,"effect":{"buff":10,"xp":40}},"resistance":"wind","description":"A statue that has come to life.","speshal spwan location":["~water","~lava","cave","hot","~river"]},
"Possessed cow":{"tier":1,"hp":90,"dmg":18,"drops":{"name":"haunted horn","quantity":1,"useable":False,"effect":{"buff":8,"xp":30}},"resistance":"darkness","description":"A cow possessed by a spirit.","speshal spwan location":["~water","~lava","feild","~river"]},
"mermaid":{"tier":2,"hp":110,"dmg":20,"drops":{"name":"song of the sea","quantity":1,"useable":True,"effect":{"heal":15,"xp":35}},"resistance":"water","description":"A mystical mermaid.","speshal spwan location":["water","~lava","~hot","~feild","~cave","~bridge","river","~town","~snow"]},
"Lava monster":{"tier":2,"hp":160,"dmg":27,"drops":{"name":"lava core","quantity":1,"useable":True,"effect":{"bomb core":12,"xp":45}},"resistance":"fire","description":"A creature made of molten lava.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"Fish lord":{"tier":3,"hp":190,"dmg":33,"drops":{"name":"trident of the deep","quantity":1,"useable":False,"effect":{"buff":25,"xp":80}},"resistance":"water","description":"The ruler of all fish.","speshal spwan location":["water","~lava","~hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"Lava warden":{"tier":3,"hp":210,"dmg":38,"drops":{"name":"ember shield","quantity":1,"useable":False,"effect":{"buff":30,"xp":90}},"resistance":"fire","description":"A guardian of the lava realms.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"blain":{"tier":100,"hp":9999,"dmg":500,"drops":{"name":"debug item","quantity":1,"useable":True,"effect":{"ඞ":9999}},"resistance":"darkness","description":"one of the makers of the game","speshal spwan location":["debug"]},
"liam":{"tier":100,"hp":9999,"dmg":500,"drops":{"name":"debug item","quantity":1,"useable":True,"effect":{"ඞ":9999}},"resistance":"darkness","description":"one of the makers of the game","speshal spwan location":["debug"]},
"yeti":{"tier":2,"hp":150,"dmg":30,"drops":{"name":"yeti fur","quantity":1,"useable":False,"effect":{"buff":20,"xp":50}},"resistance":"ice","description":"A large ape-like creature covered in fur.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"ice cube":{"tier":1,"hp":70,"dmg":12,"drops":{"name":"frost shard","quantity":1,"useable":True,"effect":{"heal":15,"xp":20}},"resistance":"ice","description":"A small cube of ice that has come to life.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"Nyx-spawn":{"tier":3,"hp":200,"dmg":40,"drops":{"name":"shadow essence","quantity":1,"useable":False,"effect":{"buff":30,"xp":75}},"resistance":"darkness","description":"A creature born from the shadows.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"phoenix":{"tier":3,"hp":180,"dmg":35,"drops":{"name":"phoenix feather","quantity":1,"useable":True,"effect":{"heal++":30,"xp":60}},"resistance":"fire","description":"A mythical bird that rises from its ashes.","speshal spwan location":["~water","lava","hot","~feild","~cave","~bridge","~town","~river","~snow"]},
"shadow beast":{"tier":2,"hp":140,"dmg":22,"drops":{"name":"dark fang","quantity":1,"useable":False,"effect":{"buff":15,"xp":40}},"resistance":"darkness","description":"A beast that lurks in the shadows.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"ghost":{"tier":1,"hp":60,"dmg":10,"drops":{"name":"ectoplasm","quantity":1,"useable":True,"effect":{"heal":10,"xp":15}},"resistance":"darkness","description":"A wandering spirit.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"zombie":{"tier":1,"hp":50,"dmg":8,"drops":{"name":"rotting flesh","quantity":1,"useable":False,"effect":{"buff":5,"xp":10}},"resistance":"darkness","description":"A reanimated corpse.","speshal spwan location":["~water","~lava","~hot","~feild","~cave","~bridge","~town","~river","snow"]},
"lord king":{"tier":10,"hp":1000,"dmg":100,"drops":{"name":"king's crown","quantity":1,"useable":False,"effect":{"buff":100,"xp":500}},"resistance":"light","description":"The ultimate ruler.","speshal spwan location":["debug"]},
"lord king's guard":{"tier":5,"hp":500,"dmg":50,"drops":{"name":"guard's emblem","quantity":1,"useable":False,"effect":{"buff":50,"xp":250}},"resistance":"light","description":"The elite guard of the lord king.","speshal spwan location":["debug"]},
"shadow dragon":{"tier":10,"hp":1200,"dmg":120,"drops":{"name":"shadow scale","quantity":1,"useable":False,"effect":{"buff":120,"xp":600}},"resistance":"darkness","description":"A dragon born from shadows.","speshal spwan location":["debug"]},
"samus aran":{"tier":50,"hp":3000,"dmg":300,"drops":{"name":"power suit","quantity":1,"useable":False,"effect":{"buff":3000,"xp":1500}},"resistance":"electric","description":"A legendary bounty hunter.","speshal spwan location":["debug"]},#nentendo pleese dont sue me
"korock":{"tier":0,"hp":1,"dmg":1,"drops":{"name":"the soul of a korock you monster","quantity":1,"useable":False,"effect":{"buff":9999,"xp":9999}},"resistance":"wind","description":"A small plant-like creature from the land of hyrule.","speshal spwan location":["debug"]},
"nintendo":{"tier":100000000000000000000000000000000000000000000000,"hp":999999999999999999999999999999999999999999999999,"dmg":999999999999999999999999999999999999999999999999,"drops":{"name":"no one can get this item","quantity":1,"useable":False,"effect":{"buff":100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,"xp":100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}},"resistance":"light","description":"the ultimate being","speshal spwan location":["debug"]}}
#team manager
class TeamManager:
	def __init__(self, hp, dmg, drops, resistance, teir, name, description, level=None, mana=None, xp=None):
		# Expect lists for multi-entity teams
		self.hp_max = list(hp)
		self.hp = list(hp)
		self.dmg = list(dmg)
		self.drops = list(drops)
		self.resistance = list(resistance)
		self.teir = list(teir)
		self.name = list(name)
		self.description = list(description)
		# n is number of people in the team
		n = len(self.hp)
		if level is None:
			self.level = [1] * n
		else:
			self.level = list(level)
		if mana is None:
			self.mana_max = [10] * n
			self.mana = [10] * n
		else:
			self.mana_max = list(mana)
			self.mana = list(mana)
		if xp is None:
			self.xp = [0] * n
		else:
			self.xp = list(xp)
	def __repr__(self):
		return f'{{"hp_max":self.hp_max,"hp":self.hp,"dmg":self.dmg,"drops":self.drops,"resistance":self.resistance,"teir":self.teir,"name":self.name,"description":self.description,"level":self.level,"max_mana":self.mana_max,"mana":self.mana,"xp":self.xp}}'
	def __str__(self):
		return """
"""
	def getattribute(self, attr_name, person=0):
		if hasattr(self, attr_name):
			val = getattr(self, attr_name)
			try:
				return val[person]
			except Exception:
				return val
		return None

	def heal(self, heal_amount, person):
		if 0 <= person < len(self.hp):
			self.hp[person] = min(self.hp[person] + heal_amount, self.hp_max[person])

	def damage(self, damage_amount, damage_type, person):
		if not (0 <= person < len(self.hp)):
			return
		actual = damage_amount
		if self.resistance and person < len(self.resistance):
			if self.resistance[person] == damage_type:
				actual = damage_amount // 2
		self.hp[person] = max(self.hp[person] - actual, 0)
		print(f"{self.name[person]} took {actual} damage (HP now {self.hp[person]})")

	def if_dead(self, person, targets=None):
		if 0 <= person < len(self.hp) and self.hp[person] <= 0:
			self.remove(person, targets)
	def defeated(self):
		if len(self.get_continuous_players())<1:
			return True
		else:
			return False
	def remove(self, person, targets=None):
		if not (0 <= person < len(self.hp)):
			return
		if self.teir[person] == 0:
			print(f"{self.name[person]} is unconscious")
			self.hp[person] = -1
			if isinstance(targets, list) and person in targets:
				try:
					targets.remove(person)
				except ValueError:
					pass
		else:
			print(f"You got {self.drops[person]} and killed {self.name[person]}")
			if isinstance(targets, list):
				if 0 <= person < len(targets):
					targets.pop(person)

	def level_up(self, person):
		global monster_spawn_rate
		if not (0 <= person < len(self.level)):
			return
		self.level[person] += 1
		self.hp_max[person] += 10
		self.hp[person] = self.hp_max[person]
		self.mana_max[person] += 10
		self.mana[person] = self.mana_max[person]
		if self.level[person] % 7 == 0:
			monster_spawn_rate = min(monster_spawn_rate + 5, 70)
		self.dmg[person] += 10

	def add_buff(self, damage_buff, person):
		if 0 <= person < len(self.dmg):
			self.dmg[person] += damage_buff

	def attack(self, players_go, continuous_players, enemies,players):
		global inventory
		if players_go:
			
			for player_index in continuous_players:
				print(f'{players.getattribute("name",0)} is at {players.getattribute("hp",0)} hp\n{players.getattribute("name",1)} is at {players.getattribute("hp",1)} hp\n{players.getattribute("name",2)} is at {players.getattribute("hp",2)} hp\n')
				if enemies.defeated():
					break
				choise = util_functions.get_valid_type(int,"0 to run away, 1 to attack, 2 to use item: ","that is not a number 0,1 or 2",[0,1,2])
				if choise == 0:
					if util_functions.alternate_random((0,5),int)==1:
						print("the monsters where too fast and caught you as you tried to run away")
						continue
					else:
						print("you successfully ran away!")
						return "ran"
				elif choise == 2 and inventory.get_inventory() is not None:
					inventory.choose_item_and_use(True,continuous_players,enemies)
				damage = self.dmg[player_index]
				if len(enemies.hp) == 0:
					continue
				target = random.randint(0, len(enemies.hp) - 1)
				enemies.damage(damage, "normal", target)
				enemies.if_dead(target, list(range(len(enemies.hp))))
		else:
			for i in range(len(enemies.hp)):
				if enemies.hp[i] <= 0:
					continue
				tier_val = enemies.teir[i] if i < len(enemies.teir) and enemies.teir[i] > 0 else 1
				num = random.randint(1, max(1, tier_val))
				if num == 1:
					if not continuous_players:
						continue
					target = random.choice(continuous_players)
					enemies.damage(enemies.dmg[i], "normal", target)
					self.if_dead(target, continuous_players)
				elif num == 2:
					for j in continuous_players:
						enemies.damage(enemies.dmg[i], "normal", j)
						self.if_dead(j, continuous_players)
				elif num == 3:
					if not continuous_players:
						continue
					target = random.choice(continuous_players)
					enemies.damage(enemies.dmg[i] // 2, "resistant", target)
					self.if_dead(target, continuous_players)
				elif num == 4:
					for j in continuous_players:
						enemies.damage(enemies.dmg[i] // 2, "resistant", j)
						self.if_dead(j, continuous_players)

	def get_continuous_players(self):
		continuous_players = []
		for i in range(len(self.hp)):
			if self.hp[i] > 0:
				continuous_players.append(i)
		return continuous_players

	def gain_mana(self, mana_amount, person):
		if 0 <= person < len(self.mana):
			self.mana[person] = min(self.mana[person] + mana_amount, self.mana_max[person])
	#def 
class InventoryManager:
	def __init__(self, starting_inventory=None):
		self.inventory = starting_inventory.copy() if starting_inventory else {}
	def __str__(self):
		return f"{self.get_inventory()}"
	def use(self, item_name, continuous_players, person):
		if item_name in self.inventory and self.inventory[item_name].get("useable", False):
			self.effect_function(self.inventory[item_name].get("effect", {}), continuous_players, person)
			self.inventory[item_name]["quantity"] -= 1
			if self.inventory[item_name]["quantity"] <= 0:
				self.inventory.pop(item_name)
		else:
			raise Exception(f"Item '{item_name}' not usable or not found")

	def grant(self, item):
		if not isinstance(item, dict) or "name" not in item:
			raise Exception("Invalid item format")
		if item.get("useable", False):
			name = item["name"]
			if name in self.inventory:
				self.inventory[name]["quantity"] += item.get("quantity", 1)
			else:
				self.inventory[name] = item.copy()

	def get_length(self):
		return len(self.inventory)

	def get_inventory(self):
		return self.inventory

	def effect_function(self, effect,party,person):
		if not isinstance(effect, dict):
			return
		# healing and mana effects
		if "heal" in effect:
			party.heal(10, person)
		if "heal+" in effect:
			party.heal(30, person)
		if "heal++" in effect:
			party.heal(party.hp_max[person], person)
		if "ether" in effect:
			party.gain_mana(10, person)
		if "elixir" in effect:
			party.gain_mana(10, person)
			party.heal(10, person)
		if "hi-ether" in effect:
			party.gain_mana(30, person)
		if "hi-elixir" in effect:
			party.gain_mana(party.mana_max[person], person)
			party.heal(party.hp_max[person], person)

		# debug item
		if "ඞ" in effect:
			for i in range(len(party.hp)):
				party.heal(party.hp_max[i], i)
				party.gain_mana(party.mana_max[i], i)
			dmg = util_functions.get_valid_type(int,"")
			for i in range(len(enemies.hp)):
				enemies.damage(dmg, "normal", i)

		# items/efects
		if "bomb core" in effect:
			dmg = effect["bomb core"]
			for i in range(len(enemies.hp)):
				enemies.damage(dmg, "fire", i)
		if "lightning core" in effect:
			dmg = effect["lightning core"]
			for i in range(len(enemies.hp)):
				enemies.damage(dmg, "electric", i)
		if "blizzard core" in effect:
			dmg = effect["blizzard core"]
			for i in range(len(enemies.hp)):
				enemies.damage(dmg, "ice", i)
		if "fire core" in effect:
			enemies.damage(effect["fire core"], "fire", person)
		if "electric core" in effect:
			enemies.damage(effect["electric core"], "electric", person)
		if "ice core" in effect:
			enemies.damage(effect["ice core"], "ice", person)
	def choose_item_and_use(self,usable,party,enemy_party):
		key=[]
		if usable:
			iteration=0
			print("0 to return")
			for num,x in enumerate(inventory.get_inventory()):
				if x["useable"]:
					iteration+=1
					print(f"{iteration} for {x}")
					key.append(x)
			while True:
				choise = util_functions.get_valid_type(int,"what do you want to use: ","that is not a valid input, press enter to continue",(0,iteration))
				if choise==0:
					return "returned"
				item=self.inventory[key[choise-1]]
				key=[]
				if item["effect"] not in ["heal"]:
					while True:
						print("0 to return")
						for num,x in enumerate(enemy_party.get_continuous_players()):
							key.append(num)
							print(f"{num+1} to atack {x}")
						choise=util_functions.get_valid_type(int,"who do you want to atack; ","that is not a valid input, press enter to continue",(0,num+1))
						if choise==0:
							break
						else:
							choise=enemy_party[choise]
							self.use(item[3])
				
		else:
			iteration=0
			for num,x in enumerate(inventory.get_inventory()):
				if not x["useable"]:
					iteration+=1
					print(f"{iteration} for {x}")

monster_spawn_rate = 20

enemies = TeamManager(
	hp=[50,50,50],
	dmg=[10,15,20],
	drops=[{"name":"bomb core","quantity":1,"useable":True,"effect":{"fire":30}},
		{"name":"lightning core","quantity":1,"useable":True,"effect":{"electricity":30}},
		{"name":"blizzard core","quantity":1,"useable":True,"effect":{"ice":30}}],
	resistance=["fire","electric","ice"],
	teir=[1,2,3],
	name=["Goblin","Orc","Troll"],
	description=["A weak goblin","A strong orc","A huge troll"]
)
party = TeamManager(
	hp=[100,80,60],
	dmg=[12,8,15],
	drops=[{}, {}, {}],
	resistance=["none","none","none"],
	teir=[0,0,0],
	name=["Hero","Mage","Rogue"],
	description=["Brave hero","Wise mage","Sneaky rogue"]
)
starting_inventory = {
	"potion": {"name":"potion","quantity":3,"useable":True,"effect":{"heal":30}},
	"magic weapon": {"name":"magic weapon","quantity":1,"useable":False,"effect":{}},
	"water gem": {"name":"water","quantity":1,"useable":True,"type":"chaos gem","damage":40,"description":"A gem of water"}
}

inventory = InventoryManager(starting_inventory)

def setup_new_game():
	game_state = {}
	game_state['party'] = party
	game_state['enemies_template'] = enemies
	game_state['inventory'] = inventory
	game_state['pos'] = [15, 18]  # x, y
	game_state['area'] = 'mid'
	game_state['battle_chance'] = 20
	game_state['monster_spawn_rate'] = monster_spawn_rate
	return game_state
def get_tile_at(pos, area):
	x, y = pos
	if area == 'mid':
		return mid[y][x]
	if area == 'upper':
		return upper[y][x]
	if area == 'underground':
		return underground[y][x]
	return None

def spawn_monsters_from_template(template, party_levels, max_spawn=3):
	avg_level = max(1, sum(party_levels) // len(party_levels))
	spawn_count = random.randint(1, min(avg_level, max_spawn))
	spawned_hp = []
	spawned_dmg = []
	spawned_drops = []
	spawned_res = []
	spawned_teir = []
	spawned_name = []
	spawned_desc = []
	for _ in range(spawn_count):
		idx = random.randint(0, len(template.hp)-1)
		spawned_hp.append(template.hp_max[idx])
		spawned_dmg.append(template.dmg[idx])
		spawned_drops.append(template.drops[idx])
		spawned_res.append(template.resistance[idx])
		spawned_teir.append(template.teir[idx])
		spawned_name.append(template.name[idx])
		spawned_desc.append(template.description[idx])
	return TeamManager(spawned_hp, spawned_dmg, spawned_drops, spawned_res, spawned_teir, spawned_name, spawned_desc)
