import pygame
import os

####################기본 초기화 (반드시 해야하는 것들)###################
pygame.init()

# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")

# FPS
clock = pygame.time.Clock()

##################################여기까지 기본 초기화

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지 높이 위에 캐릭터를 두기 위해서

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x_RIGHT = 0
character_to_x_LEFT = 0
# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -13, -11]

# 공들의 개수
balls = []
# 최초 발생하는 큰 공을 추가
balls.append({
    "pos_x": 50,  # 공의 x좌표
    "pos_y": 50,  # 공의 y좌표
    "img_idx": 0,  # 공의 이미지 인덱스
    "to_x": 3,  # 공의 x축 이동 방향(3이면 왼쪽, -3이면 오른쪽
    "to_y": -6,
    "init_spd_y": ball_speed_y[0]
})

#사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성

#게임 종료 메시지 / Time Out, Mission Complete, Game Over
game_result = "Game Over"

# 총 시간
total_time = 30
# 시간 계산
start_ticks = pygame.time.get_ticks()  # 첫 시작 시간 정보를 받아옴

# 이벤트 루프

running = True
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수
    # print("fps : ", clock.get_fps())
    # 키보드, 마우스 등 이벤트 처리
    for event in pygame.event.get():  # event는 입력같은 이벤트를 받아들임
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_pos_y = character_y_pos
                weapons.append([weapon_pos_x, weapon_pos_y])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT = 0
            if event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0

    character_x_pos = character_x_pos + character_to_x_LEFT + character_to_x_RIGHT

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치를 위로
    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] #y값이 0보다 클 때만 존재하므로 그게 아니면 없어짐

    # 공 위치 정의

    for ball_idx, ball_val in enumerate(balls): #enumerate : index와 value값을 받아와줌
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1 # 벽에 닿으면 방향을 반대로 바꾸어줌

        # 세로 위치
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"] # 스테이지에 튕겨서 올라감
        else:
            ball_val["to_y"] += 0.5  # 포물선을 그리는 효과

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 경계값 처리

    # . 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    #캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos


    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break

    #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons): #enumerate 이용
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y


        # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기
                ball_to_remove = ball_idx

                if ball_img_idx < 3: #가장 작은 공이 아니라면
                    #현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    # 나눠진 공 정보

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    balls.append({
                        "pos_x": ball_pos_x + ball_width / 2 - small_ball_width/2,  # 공의 x좌표
                        "pos_y": ball_pos_y + ball_height / 2 - small_ball_height/2,  # 공의 y좌표
                        "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x": -3,  # 공의 x축 이동 방향(3이면 왼쪽, -3이면 오른쪽
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx+1]
                    })
                    balls.append({
                        "pos_x": ball_pos_x + ball_width / 2 - small_ball_width / 2,  # 공의 x좌표
                        "pos_y": ball_pos_y + ball_height / 2 - small_ball_height / 2,  # 공의 y좌표
                        "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x": 3,  # 공의 x축 이동 방향(3이면 왼쪽, -3이면 오른쪽
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx+1]
                    })

                break

    #충돌된 공 or 무기 없애기
        if ball_to_remove != -1:
            del balls[ball_to_remove]
            ball_to_remove = -1
        if weapon_to_remove != -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1

    if len(balls) == 0:
        game_result = "Mission Complete!"
        break
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_pos_x, weapon_pos_y in weapons:
        screen.blit(weapon, (weapon_pos_x, weapon_pos_y))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render("Time : {0}".format(int(total_time - elapsed_time)),True ,(255,255,255))
    screen.blit(timer,(10, 10))

    # 시간 초과했다면
    if total_time - elapsed_time < 0 :
        game_result="Time Over"
        running = False

    pygame.display.update()  # 게임화면을 다시 그리기(호출)

msg = game_font.render(game_result, True, (255,0,0)) #노란색
msg_rect = msg.get_rect(center =(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(1000)
# pygame 종료
pygame.quit()
