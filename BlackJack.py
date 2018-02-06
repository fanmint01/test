import random
import time

# プレイヤーの持つ手札を表示する関数

def disp(which_player, p_cards):
    print("あなたの手札は: {0} 、".format(p_cards) if which_player == "my"
          else "相手の手札は: {0}です。\n".format(p_cards))

# SCOREをプレイヤーのリスト型に返す関数

def get_score(search_score):
    score = search_score % 14
    if score == 1:
        return 11
    elif score > 10:
        return 10
    else :
        return score

# 勝敗を判定して表示する関数

def hantei(my_score, enemy_score):
    print("結果を発表します...")
    time.sleep(3)
    if my_score > 21 and enemy_score <= 21 or my_score < enemy_score and enemy_score <= 21:
        print("あなたは敗北しました...")
    elif my_score <= 21 and enemy_score > 21 or my_score > enemy_score and my_score <= 21:
        print("あなたの勝利デス！")
    else :
        print("Drow_Game")

# カード情報を持つ辞書型を作成

cards = {"s-A": 1, "s-2": 2, "s-3": 3, "s-4": 4, "s-5": 5, "s-6": 6, "s-7": 7,
          "s-8": 8, "s-9": 9, "s-10": 10, "s-J": 11, "s-Q": 12, "s-K": 13,
         "d-A": 15, "d-2": 16, "d-3": 17, "d-4": 18, "d-5": 19, "d-6": 20,"d-7": 21,
         "d-8": 22, "d-9": 23, "d-10": 24, "d-J": 25, "d-Q": 26, "d-K": 27,
         "c-A": 29, "c-2": 30, "c-3": 31, "c-4": 32, "c-5": 33, "c-6": 34, "c-7": 35,
          "c-8": 36, "c-9": 37, "c-10": 38, "c-J": 39, "c-Q": 40, "c-K": 41,
         "h-A": 43, "h-2": 44, "h-3": 45, "h-4": 46, "h-5": 47, "h-6": 48, "h-7": 49,
          "h-8": 50, "h-9": 51, "h-10": 52, "h-J": 53, "h-Q": 54, "h-K": 55}

# カードを二枚ずつ配る処理

print("\n----GameStart!----\n\nカードを配っています...\n"
      "s = スペード, d = ダイア, c = クラブ, h = ハート\n")
time.sleep(5)

random.seed()
give_player_select = False
give_end = False
my_cards = []
enemy_cards = []
rand_log = []
log_flag = False

while give_end == False:
    rand = random.randint(0, 55)
    if rand % 14 == 0:
        continue
    for i in range(len(rand_log)):
        if rand == rand_log[i]:
            log_flag = True
            break
    for c_name, value in cards.items():
        if log_flag == True:
            log_flag = False
            break   
        if rand == value and give_player_select == False:
            my_cards.append(c_name)
            my_cards.append(value)
            rand_log.append(value)
            if len(my_cards) == 4:
                give_player_select = True
            break
        elif rand == value and give_player_select == True:
            enemy_cards.append(c_name)
            enemy_cards.append(value)
            rand_log.append(value)
            if len(enemy_cards) == 4:
                give_end = True
            break

# お互いのSCOREを計算し、総スコアを出す処理

my_cards[1] = get_score(my_cards[1]) 
my_cards[3] = get_score(my_cards[3])
my_sum_score = my_cards[1] + my_cards[3]

if my_sum_score > 21:
    for i in range(2):
        if my_cards[i] == 11:
            my_cards[i] = 1
            my_sum_score = my_cards[1] + my_cards[3]
        if my_sum_score <= 21:
            break

enemy_cards[1] = get_score(enemy_cards[1])
enemy_cards[3] = get_score(enemy_cards[3])
enemy_sum_score = enemy_cards[1] + enemy_cards[3]

if enemy_sum_score > 21:
    for i in range(2):
        if enemy_cards[i] == 11:
            enemy_cards[i] = 1
            enemy_sum_score = enemy_cards[1] + enemy_cards[3]
        if enemy_sum_score <= 21:
            break

# お互いの手札を公開する

disp("my", my_cards)
disp("enemy",enemy_cards)

# 追加で引くか選択し、勝敗を出力する

give_player_select = False
give_end = False
enemy_select = False
answer_flag = False

if enemy_sum_score <= 16:
    enemy_select = True
    
while answer_flag == False:
    answer = input("追加で引きますか？（はい/いいえ）")
    print("\n")
    if answer != "はい" and answer != "いいえ":
        print("ちょっとなんて言ってるかわからないです\n")
    else :
        answer_flag = True

# ユーザが追加で引く場合の処理

if answer == "はい":
    while give_end == False:
        rand = random.randint(0, 55)
        if rand % 14 == 0:
            continue
        for i in range(len(rand_log)):
            if rand == rand_log[i]:
                log_flag = True
                break
        for c_name, value in cards.items():
            if log_flag == True:
                log_flag = False
                break 
            if rand == value and give_player_select == False:
                my_cards.append(c_name)
                my_cards.append(value)
                rand_log.append(value)
                if len(my_cards) == 6:
                    give_player_select = True
                    if enemy_select == False:
                        give_end = True
                break
            elif rand == value and give_player_select == True:
                enemy_cards.append(c_name)
                enemy_cards.append(value)
                rand_log.append(value)
                if len(enemy_cards) == 6:
                    give_end = True
                break

# 追加で引いたカードのSCOREを計算し、総スコアを出す処理

    my_cards[5] = get_score(my_cards[5]) 
    my_sum_score += my_cards[5]
    if my_sum_score > 21:
        for i in range(3):
            if my_cards[i] == 11:
                my_cards[i] = 1
                my_sum_score = my_cards[1] + my_cards[3] + my_cards[5]
            if my_sum_score <= 21:
                break

    if enemy_select == True:    
        enemy_cards[5] = get_score(enemy_cards[5]) 
        enemy_sum_score += enemy_cards[5]
        if enemy_sum_score > 21:
            for i in range(3):
                if enemy_cards[i] == 11:
                    enemy_cards[i] = 1
                    enemy_sum_score = enemy_cards[1] + enemy_cards[3] + enemy_cards[5]
                if enemy_sum_score <= 21:
                    break

# 勝敗の判定

    hantei(my_sum_score, enemy_sum_score)
    print("\n")

# お互いの手札を公開する

    disp("my", my_cards)
    disp("enemy",enemy_cards)

# ユーザが追加で引かない場合の処理

elif answer == "いいえ":
    while give_end == False and enemy_select == True:
        rand = random.randint(0, 55)
        if rand % 14 == 0:
            continue
        for i in range(len(rand_log)):
            if rand == rand_log[i]:
                log_flag = True
                break
        for c_name, value in cards.items():
            if log_flag == True:
                log_flag = False
                break 
            if rand == value:
                enemy_cards.append(c_name)
                enemy_cards.append(value)
                rand_log.append(value)
                if len(enemy_cards) == 6:
                    give_end = True
                break

# 相手のSCOREを計算し、総スコアを出す処理

    if enemy_select == True:    
        enemy_cards[5] = get_score(enemy_cards[5]) 
        enemy_sum_score += enemy_cards[5]
        if enemy_sum_score > 21:
            for i in range(3):
                if enemy_cards[i] == 11:
                    enemy_cards[i] = 1
                    enemy_sum_score = enemy_cards[1] + enemy_cards[3] + enemy_cards[5]
                if enemy_sum_score <= 21:
                    break

# 勝敗の判定

    hantei(my_sum_score, enemy_sum_score)
    print("\n")

# お互いの手札を公開する

    disp("my", my_cards)
    disp("enemy",enemy_cards)

print("お疲れさまでした、またのご利用お待ちしております。")
time.sleep(8)

