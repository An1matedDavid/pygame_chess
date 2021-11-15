import datetime
st = str(datetime.datetime.now()).split('.')[0].replace(" ", "_").replace(":", "-")
f = open("game_history/myfile_"+st+".txt", "w")
f.write("Now the file has more content!")
f.close()