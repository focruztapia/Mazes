import requests

url = "http://ec2-34-211-81-131.us-west-2.compute.amazonaws.com"  # server url
uid = "105185700"  # your uid
resp = requests.post(url + "/session", data={"uid": uid})  # start new session
body = resp.json()
access_token = body["token"]  # retrieve access token from response body

resp = requests.get(url + "/game?token=" + access_token)  # get maze information
body = resp.json()

rows = body["size"][0] + 2
cols = body["size"][1] + 2
a = []
for row in range(rows):
    a += [[0]*cols]

x = body["cur_loc"][0] + 1
y = body["cur_loc"][1] + 1

a[x][y] = "v"

s = []  # create a new Stack named s

level = 0

while True:

    print("Traversing: (" + str(x) + ", " + str(y) + ")")

    if a[x][y + 1] != "v"\
            and a[x][y + 1] != "*"\
            and a[x][y + 1] != "#":

        resp1 = requests.post(url + "/game?token=" + access_token, data={"action": "down"})
        body1 = resp1.json()

        if body1["result"] == 0:
            s.append("up")  # push right neighbor onto stack s
            a[x][y + 1] = "v"
            y += 1
            continue

        elif body1["result"] == -1:
            a[x][y + 1] = "*"

        elif body1["result"] == -2:
            a[x][y + 1] = "#"

        elif body1["result"] == 1:
            s.clear()
            resp = requests.get(url + "/game?token=" + access_token)  # get maze information
            body = resp.json()
            if body["status"] == "FINISHED":
                break
            print("Levels Completed: " + str(body["levels_completed"]))
            rows = body["size"][0] + 2
            cols = body["size"][1] + 2
            a = []
            for row in range(rows):
                a += [[0] * cols]
            x = body["cur_loc"][0] + 1
            y = body["cur_loc"][1] + 1
            a[x][y] = "v"
            continue

    if a[x + 1][y] != "v"\
            and a[x + 1][y] != "*"\
            and a[x + 1][y] != "#":

        resp1 = requests.post(url + "/game?token=" + access_token, data={"action": "right"})
        body1 = resp1.json()

        if body1["result"] == 0:
            s.append("left")  # push right neighbor onto stack s
            a[x + 1][y] = "v"
            x += 1
            continue

        elif body1["result"] == -1:
            a[x + 1][y] = "*"

        elif body1["result"] == -2:
            a[x + 1][y] = "#"

        elif body1["result"] == 1:
            s.clear()
            resp = requests.get(url + "/game?token=" + access_token)  # get maze information
            body = resp.json()
            if body["status"] == "FINISHED":
                break
            print("Levels Completed: " + str(body["levels_completed"]))
            rows = body["size"][0] + 2
            cols = body["size"][1] + 2
            a = []
            for row in range(rows):
                a += [[0] * cols]
            x = body["cur_loc"][0] + 1
            y = body["cur_loc"][1] + 1
            a[x][y] = "v"
            continue

    if a[x][y - 1] != "v"\
            and a[x][y - 1] != "*"\
            and a[x][y - 1] != "#":

        resp1 = requests.post(url + "/game?token=" + access_token, data={"action": "up"})
        body1 = resp1.json()

        if body1["result"] == 0:
            s.append("down")  # push right neighbor onto stack s
            a[x][y - 1] = "v"
            y -= 1
            continue

        elif body1["result"] == -1:
            a[x][y - 1] = "*"

        elif body1["result"] == -2:
            a[x][y - 1] = "#"

        elif body1["result"] == 1:
            s.clear()
            resp = requests.get(url + "/game?token=" + access_token)  # get maze information
            body = resp.json()
            if body["status"] == "FINISHED":
                break
            print("Levels Completed: " + str(body["levels_completed"]))
            rows = body["size"][0] + 2
            cols = body["size"][1] + 2
            a = []
            for row in range(rows):
                a += [[0] * cols]
            x = body["cur_loc"][0] + 1
            y = body["cur_loc"][1] + 1
            a[x][y] = "v"
            continue

    if a[x - 1][y] != "v"\
            and a[x - 1][y] != "*"\
            and a[x - 1][y] != "#":

        resp1 = requests.post(url + "/game?token=" + access_token, data={"action": "left"})
        body1 = resp1.json()

        if body1["result"] == 0:
            s.append("right")  # push right neighbor onto stack s
            a[x - 1][y] = "v"
            x -= 1
            continue

        elif body1["result"] == -1:
            a[x - 1][y] = "*"

        elif body1["result"] == -2:
            a[x - 1][y] = "#"

        elif body1["result"] == 1:
            s.clear()
            resp = requests.get(url + "/game?token=" + access_token)  # get maze information
            body = resp.json()
            if body["status"] == "FINISHED":
                break
            print("Levels Completed: " + str(body["levels_completed"]))
            rows = body["size"][0] + 2
            cols = body["size"][1] + 2
            a = []
            for row in range(rows):
                a += [[0] * cols]
            x = body["cur_loc"][0] + 1
            y = body["cur_loc"][1] + 1
            a[x][y] = "v"
            continue

    direction = s[-1]

    if direction == "down":
        y += 1
    elif direction == "right":
        x += 1
    elif direction == "up":
        y -= 1
    elif direction == "left":
        x -= 1

    requests.post(url + "/game?token=" + access_token, data={"action": direction})
    s.pop()


print("Finished all 5 levels")
