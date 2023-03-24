import random

level = 1


def PlayGame(level):

    m = 3 * level

    game_Data = {
        "level": level,
        "m": 3,
        "pr_map": [],

        "user_coordinates": [],
        "wolf_coordinates": [],
        "fire_coordinates": [],
        "treasure_coordinates": [],
        "enemy_coordinates": [],

        "user_xp": 50,
        "wolf_xp": 30,
        "fire_xp": 25,
        "treasure_xp": 25,

        "isGameActive": True,
        
        "wolf_sample": [],
        "fire_sample": [],
        "treasure_sample": [],
    }
    print()

    def DrawMap():
        for row in range(m):
            for col in range(m):
                temp = [row, col]
                game_Data["pr_map"].append(temp)

    # Center user on grid/map
    def GetUserCoordinates():
        game_Data["user_coordinates"] = game_Data["pr_map"][int(
            len(game_Data["pr_map"])/2)]

    # random wolf coordinates
    def GetRandomWolfCor():
        game_Data["wolf_sample"] = game_Data["pr_map"]
        game_Data["wolf_sample"].remove(game_Data["user_coordinates"])
        game_Data["wolf_coordinates"] = random.sample(
            game_Data["wolf_sample"], level)
        game_Data["enemy_coordinates"].append(game_Data["wolf_coordinates"])
        return game_Data["wolf_coordinates"]

    # random fire coordinates
    def GetRandomFireCor():
        game_Data["fire_sample"] = game_Data["wolf_sample"]
        for i in game_Data["wolf_coordinates"]:
            game_Data["fire_sample"].remove(i)  # Removes the users coordinates
        game_Data["fire_coordinates"] = random.sample(
            game_Data["fire_sample"], level)
        game_Data["enemy_coordinates"].append(game_Data["fire_coordinates"])
        return game_Data["fire_coordinates"]

    # random fire coordinates
    def GetRandomTreasureCor():
        game_Data["treasure_sample"] = game_Data["fire_sample"]
        for i in game_Data["fire_coordinates"]:
            game_Data["treasure_sample"].remove(i)
        game_Data["treasure_coordinates"] = random.sample(
            game_Data["treasure_sample"], level*2)
        return game_Data["treasure_coordinates"]

    print()
    DrawMap()
    GetUserCoordinates()
    GetRandomWolfCor()
    GetRandomFireCor()
    GetRandomTreasureCor()

    def ShowData():
        print("###########################################################################################")
        print("##### Map grid =>", game_Data["pr_map"])
        print("##### 00. LoadGme\n##### 10. SaveGme \n##### 99. QUIT")
        print("#####")
        print("#####  User-Coordinates  => ", game_Data["user_coordinates"])
        print('#####  Wolf-Coordinates  => ', game_Data["wolf_coordinates"])
        print('#####  Fire-Coordinates  => ', game_Data["fire_coordinates"])
        print('#####  Treasure-Coordinates  => ',
              game_Data["treasure_coordinates"])
        print("#####  Enemy Locations => ", game_Data["enemy_coordinates"])
        print("#####  User XP => ", game_Data["user_xp"])
        print("###########################################################################################")

    ShowData()

    # Move player per node
    def move_player(direction):
        print()
        if -1 < game_Data["user_coordinates"][0] <= m-1 and -1 < game_Data["user_coordinates"][1] <= m-1:
            if direction == "00":
                LoadGme()
            elif direction == "10":
                SaveGme()
            elif direction == "99":
                game_Data["isGameActive"] = False
                return game_Data["isGameActive"]

            elif direction == "8":
                if game_Data["user_coordinates"][0] == m-1:
                    print("You cant jump out off the map, try again")
                else:
                    game_Data["user_coordinates"][0] += 1
            elif direction == "2":
                if game_Data["user_coordinates"][0] == 0:
                    print("You cant jump out off the map, try again")
                else:
                    game_Data["user_coordinates"][0] -= 1
            elif direction == "6":
                if game_Data["user_coordinates"][1] == m-1:
                    print("You cant jump out off the map, try again")
                else:
                    game_Data["user_coordinates"][1] += 1
            elif direction == "4":
                if game_Data["user_coordinates"][1] == 0:
                    print("You cant jump out off the map, try again")
                else:
                    game_Data["user_coordinates"][1] -= 1
            else:
                print("======== Invalid move made!!! ========")
            checkLocationDrop()
            ShowData()
        else:
            return False

# Check what coordinates the user has moved to
    def checkLocationDrop():
        if game_Data["user_xp"] > 0:
            # If user same [x;y] as wolf [x;y]
            if game_Data["user_coordinates"] == game_Data["wolf_coordinates"]:
                fight = input(
                    "\nYou landed on wolf territory\n 1. Do you want to fight Wolf?\n 2. Run away\n   =>")
                Fight_Wolf(fight)
            elif game_Data["user_coordinates"] == game_Data["fire_coordinates"]:
                fight = input(
                    "\nYou landed on fire territory\n 1. Do you want to fight Fire?\n 2. Run away\n   =>")
                Fight_Fire(fight)
            elif game_Data["user_coordinates"] in game_Data["treasure_coordinates"] and len(game_Data["treasure_coordinates"]) > 0:
                Collect_Tressure(game_Data["user_coordinates"])

    def IsGamewon():
        if game_Data["user_xp"] > 0 and game_Data["enemy_coordinates"] == []:
            print("\n You won this level !!!!")
            PlayGame(level+1)

    # When user wolf on the fires grid/coorodinates
    def Fight_Wolf(fight):
        if fight == "1":
            if game_Data["user_xp"] > game_Data["wolf_xp"]:
                game_Data["user_xp"] = game_Data["user_xp"] - \
                    game_Data["wolf_xp"]
                print("\n The wolf beat you :\n User XP => ",
                      game_Data["user_xp"])
                game_Data["enemy_coordinates"].remove(
                    game_Data["wolf_coordinates"])
                game_Data["user_xp"] = game_Data["user_xp"]
                IsGamewon()
            else:
                game_Data["user_xp"] = 0
                print("\n   Death by wolf attack",
                      game_Data["wolf_coordinates"])
                print("   User XP => ", game_Data["user_xp"])
                print("   Game over!!!")
                game_Data["isGameActive"] = False
        elif fight == "2":
            return
        else:
            print("Invalid selection, try again")

    # When user lands on the fires grid/coorodinates
    def Fight_Fire(fight):
        if fight == "1":
            if game_Data["user_xp"] > game_Data["fire_xp"]:
                game_Data["user_xp"] = game_Data["user_xp"] - \
                    game_Data["fire_xp"]
                print("\n The fire beat you :\n User XP => ",
                      game_Data["user_xp"])
                game_Data["enemy_coordinates"].remove(
                    game_Data["fire_coordinates"])
                game_Data["user_xp"] = game_Data["user_xp"]
                IsGamewon()
            else:
                game_Data["user_xp"] = 0
                print("\n   You landed in the fire block",
                      game_Data["fire_coordinates"])
                print("   User XP => ", game_Data["user_xp"])
                print("   Game over!!!")
                game_Data["isGameActive"] = False
        elif fight == "2":
            return
        else:
            print("Invalid selection, try again")

    def Collect_Tressure(current_cor):
        game_Data["user_xp"] = game_Data["user_xp"] + game_Data["treasure_xp"]
        print("\n   Treasure collected => ", game_Data["user_xp"])
        game_Data["treasure_coordinates"].remove(current_cor)
        game_Data["treasure_coordinates"] = game_Data["treasure_coordinates"]
        ShowData()
        return True

    def SaveGme():
        f = open("PrometheusGameData.txt", "w")
        f.write(str(game_Data))
        print()
        print("Game Saved", f)

    def LoadGme():
        global game_Data
        with open("PrometheusGameData.txt") as f:
            game_Data = {str(k): v for line in f for (
                k, v) in [line.strip().split(None, 1)]}

        if game_Data == {}:
            print("No history")
        else:
            PlayGame(game_Data["level"])

    def Play():
        while game_Data["isGameActive"]:
            mov_direction = input(
                "\n Make a move :\n 8. up \n 2. down \n 4. left \n 6 right \n =>")
            move_player(mov_direction)

    Play()


PlayGame(level)
