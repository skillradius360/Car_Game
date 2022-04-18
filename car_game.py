import pygame, sys, random, time

pygame.init()
screen_x,screen_y= 550,880
screen = pygame.display.set_mode((screen_x, screen_y))
fps_module = pygame.time.Clock()
pygame.display.set_caption("GADDI GAME")

pygame.mixer.Sound("sounds\music.wav").play().set_volume(0.1)
tyres= pygame.mixer.Sound("sounds\screech.mp3")
def score_counter():
    interval_score = (pygame.time.get_ticks() - score_) / 2000+0.1
    score_font = _Font.render(f"{round(interval_score)}", False, "black")
    screen.blit(score_font, score_font.get_rect(midtop=(100, 100)))
    return interval_score

def red_car_spawner(rect_list):

    if rect_list:
        for cars in rect_list:
            cars.y += 3
            screen.blit(red_car_scale, cars)

        rect_list = [cars for cars in rect_list if cars.y > 900]
        return rect_list
    else:
        return []

def orange_car_spawner(rect_list):
    if rect_list:
        for cars in rect_list:
            cars.y += 3
            screen.blit(orange_car_scale, cars)

        rect_list = [cars for cars in rect_list if cars.y > 900]
        return rect_list
    else:
        return []

def blue_car_spawner(rect_list):
    if rect_list:
        for cars in rect_list:
            cars.y += 3
            screen.blit(blue_car_scale, cars)

        rect_list = [cars for cars in rect_list if cars.y > 900]
        return rect_list
    else:
        return []

def player_Movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        green_car_rect.x -= 2
        tyres.play()
        tyres.set_volume(0.2)
    elif keys[pygame.K_RIGHT]:
        green_car_rect.x += 2
        tyres.play()
        tyres.set_volume(0.2)


def grass_Motion_left(grasses):
    if grasses:
        for instances in grasses:
            instances.y -= 3
            screen.blit(grass_Image_left, instances)
        grasses = [instances for instances in grasses if instances.y > -10]
        return grasses
    else:
        return []

def grass_Motion_right(grasses):
    if grasses:
        for instances in grasses:
            instances.y -= 3
            screen.blit(grass_Image_right, instances)
        grasses = [instances for instances in grasses if instances.y > -10]
        return grasses
    else:
        return []
def road_divide(divider):
    if divider:
        for bars in divider:
            bars.y+=3
            screen.blit(road_Divider, bars)
        return divider
    else:
        return []            

Road = pygame.image.load("GAME_IMAGES\Straight-Road-clipart-png.png")
Road_rect = Road.get_rect(midtop=(275, 0))
# HEader Score
_Font = pygame.font.Font("font\Pixeltype.ttf", 50)

# bot C A R S
red_car = pygame.image.load("GAME_IMAGES\Red_car.png").convert_alpha()
red_car_scale = pygame.transform.scale(red_car, (60, 60))


blue_car = pygame.image.load("GAME_IMAGES\BLUE_CAR.png").convert_alpha()
blue_car_scale = pygame.transform.scale(blue_car, (60, 100))

# ORANGECAR
orange_car = pygame.image.load("GAME_IMAGES\ORANGECAR.png").convert_alpha()
orange_car_scale = pygame.transform.scale(orange_car, (60, 80))

# Player
green_Car = pygame.image.load("GAME_IMAGES\green_car.png").convert_alpha()
green_Car_scale = pygame.transform.scale(green_Car, (60, 80))
green_car_rect = green_Car_scale.get_rect(midtop=(300, 700))
#FOR CHANGING THE IMAGE WHEN COLLISION HAPPENS.
green_car_image_change= green_Car_scale 
# Grass
grass_Image_right = pygame.image.load("GAME_IMAGES\grass_border_right.png").convert_alpha()
grass_Image_left = pygame.image.load("GAME_IMAGES\grass_border_left.png").convert_alpha()

#explosion
explode_Image = pygame.image.load("GAME_IMAGES\explode.png").convert_alpha()
explode_Image_scale=pygame.transform.scale(explode_Image,(100,120))

#ROAD DIVIDER
road_Divider= pygame.image.load("GAME_IMAGES\Road_divider.png").convert_alpha()


game_Runs = True
redcar_spawns_list = []
orangecar_spawns_list = []
bluecar_spawns_list = []
grass_List_left = []
grass_List_right = []
divider_list = []

redcar_Event = pygame.USEREVENT + 2
orangecar_Event = pygame.USEREVENT + 1
bluecar_Event = pygame.USEREVENT + 3
grass_motion_event_left = pygame.USEREVENT + 6
grass_motion_event_right = pygame.USEREVENT + 5
divider_Event = pygame.USEREVENT + 4


time.sleep(0.5)
pygame.time.set_timer(redcar_Event, 2500)  # ms
pygame.time.set_timer(orangecar_Event, 1500)  # ms#ms
pygame.time.set_timer(bluecar_Event, 3300)  # ms


pygame.time.set_timer(grass_motion_event_left, 120)  # ms
pygame.time.set_timer(grass_motion_event_right, 120)  # ms

pygame.time.set_timer(divider_Event,160)


score_ = 0 #FOR RESETING THE SCORE BACK TO ZERO AT PRESSING SPACE. 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == redcar_Event and game_Runs:
            redcar_spawns_list.append(
                red_car_scale.get_rect(
                    center=(random.randint(130, 410), random.randint(-100, 000))
                )
            )

        if event.type == orangecar_Event and game_Runs:
            orangecar_spawns_list.append(
                orange_car_scale.get_rect(
                    center=(random.randint(130, 410), random.randint(-100, 000))
                )
            )

        if event.type == bluecar_Event and game_Runs:
            bluecar_spawns_list.append(
                blue_car_scale.get_rect(
                    midbottom=(random.randint(130, 410), random.randint(-100, 000))
                )
            )

        if event.type == grass_motion_event_left and game_Runs:
            grass_List_left.append(grass_Image_left.get_rect(center=(30, 400)))

        if event.type == grass_motion_event_right and game_Runs:
            grass_List_right.append(grass_Image_right.get_rect(center=(520, 400)))

        if event.type == divider_Event and game_Runs:
            divider_list.append(road_Divider.get_rect(center=(275,440)))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_Runs = True
                score_ = pygame.time.get_ticks()+1
                green_car_image_change= green_Car_scale
                green_car_rect.x=screen_x/2


    if game_Runs:
        # pygame.mixer.Sound("car_sound.mp3").play()
        screen.blit(Road, Road_rect)
        #renders the lane divider 
        road_divide(divider_list)
        # SPAWNS RED CAR
        red_car_spawner(redcar_spawns_list)
        # SPAWNS ORANGE CAR
        orange_car_spawner(orangecar_spawns_list)
        # SPAWNS BLUE CAR
        blue_car_spawner(bluecar_spawns_list)
        # COUNTS SCORE
        last_Score = score_counter()
        # GREEN CAR MOVEMENT
        player_Movement()
        # GRASS MOTION LOOPING
        grass_Motion_left(grass_List_left)
        grass_Motion_right(grass_List_right)
        # screen.blit(explode_Image_scale,(200,100))
        
        # RED CAR COLLISION
        if redcar_spawns_list:
            for obstacles in redcar_spawns_list:
                if green_car_rect.colliderect(obstacles):
                    game_Runs = False
                    green_car_image_change= explode_Image_scale
  

        # BLUE CAR COLLISION
        if bluecar_spawns_list:
            for obstacless in bluecar_spawns_list:
                if green_car_rect.colliderect(obstacless):
                    game_Runs = False

                    green_car_image_change= explode_Image_scale
                    
        # ORANGE CAR COLLISION
        if orangecar_spawns_list:
            for obstaclesss in orangecar_spawns_list:
                if green_car_rect.colliderect(obstaclesss):
                    game_Runs = False
                    #CHANGES TO EXPLOSION WHEN COLLIDES
                    green_car_image_change= explode_Image_scale  
                    
        # GRASS COLLISION
        if grass_List_left:
            for grass in grass_List_left:
                if green_car_rect.colliderect(grass):
                    #CHANGES TO EXPLOSION WHEN COLLIDES
                    game_Runs= False  
                    green_car_image_change= explode_Image_scale
                              
        if grass_List_right:
            for grass in grass_List_right:
                if green_car_rect.colliderect(grass):
                    #CHANGES TO EXPLOSION WHEN COLLIDES
                    game_Runs = False   
                    green_car_image_change= explode_Image_scale
                    
                    
        screen.blit(green_car_image_change, green_car_rect)            
    else:
        instruction = _Font.render("Press 'SPACE' to start", True, (0, 0, 0))
        scores_header = _Font.render("Your Last Score:", True, (0, 0, 0))
        score_FOnt = pygame.font.Font("font\Pixeltype.ttf", 80)
      
        scores = score_FOnt.render(f"{int(last_Score)}", True, "orange")

        screen.blit(instruction, (120, 600))
        screen.blit(scores_header, (140, 300))
        screen.blit(scores, (260, 340))

        orangecar_spawns_list.clear()
        bluecar_spawns_list.clear()
        redcar_spawns_list.clear()
        grass_List_left.clear()
        grass_List_right.clear() 
        divider_list.clear()

    pygame.display.update()