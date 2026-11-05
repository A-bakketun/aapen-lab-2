from uib_inf100_graphics.event_app import run_app
from uib_inf100_graphics.helpers import load_image, scaled_image
from PIL import Image
import random
import uib_inf100_music as music
import os
import sys
#######
#
#Idee myldring
#
# meelee boss figther :)



###to do

# animasjon flipping
# flere animasjoner for enemy
# boss 1:
#           Idle animation
#           walking animation
#           attack1 , 2 , 3 animation
#           hit animation
#           gud er ikke på min side
#           lage flere enemies
#           polishe hitboxes
#           Mac rebind
#           Boss 2
#           final boss
### 
#hvor mange bosser trenger jeg?
#minst 3, helst 5


############
# OS check og JSON check stjal jeg fra Snaken min
# hvor jeg stjal det fra følgende kilder:
##########kilder:
#https://docs.python.org/3/library/sys.html#sys.platform (docs for å finne ut hvordan jeg kan finne ut av OS fordi noen folk har mac)
#https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed (Stackoverflow for å finne ut av hvordan sjekke om en JSON fil finnes)
#funksjon det gjelder ( check_json(app)) ( er ikke en komplett rip men er ganske likt kopiert)
#
#
#

def app_started(app):
    
    #timer 
    app.timer_delay = 50

    #states
    app.game_state = "Menu"
    app.boss_fight = ""
    app.boss_stage = ""
    app.debug = False

    #player
    app.player_pos_x = 300 - 48
    app.player_pos_y = 400
    app.player_pos_hix = 300
    app.player_pos_hiy = 448
    app.player_state = ""
    app.player_facing = 1
    app.show_basic_attack = 0
    app.basic_attack_cooldown = 0
    app.player_color = "red"
    app.player_sprint = 0
    app.listening_to_input = 0
    app.dash_timer = 0
    app.dodge_timer = 0
    app.player_health = 10
    app.i_frames = 0
    app.attack_stops_movement = 0
    app.player_money = 0
    app.animation_counter = 0
    app.do_animation = 0
    app.attack_hitbox = []
    app.idle_counter = 0
    app.difficulty = "Baby"
    #enemy
    app.enemy_pos_x = 100
    app.enemy_pos_hix = 200
    app.enemy_pos_y = 450
    app.enemy_pos_hiy = 700
    app.enemy_hit = 0
    app.enemy_movement_CD = 10
    app.enemy_spawn = 0
    app.enemy_attack_x = 0
    app.enemy_attack_y = 0
    app.show_boss_attack = 0
    app.enemy_cd = 0
    app.boss_stagger = 0
    app.enemy_do_animation = 0
    app.enemy_projectile_cd = 20
    app.projectile_1 = [[0 , 0 , 0 ,0],
                        [0 , 0 , 0 , 0]
    ]
    app.show_projectile_1 = False
    app.show_projectile_2 = False
    app.projectile_speed = 0
    #input delay and others
    app.input_delay = 0
    app.input_delay_menu = 0
    app.menu_selector = 0
    #image_handler
    image_handler(app)
    sound_handler(app)
    
    #buttons
    main_menu_buttons(app)
    map_buttons(app)
    settings_buttons(app)
    #colors
    app.background_color = "ivory"
    app.button_color = "bisque"
    app.boss_color = "green"
    app.main_menu_song.play()
    app.enter_bind = "Enter"


    
    #system greier
    app.os_windows = True
    clean_fixes(app)


def clean_fixes(app):
    #profile? kanskje
    get_system(app)
    if app.os_windows == False:
        app.enter_bind = "Return"

def get_system(app):
    temp = sys.platform
    if temp == "darwin":
        app.os_windows = False 


def image_handler(app):
    create_player_animations(app)
    create_boss_one_animations(app)
    create_backgrounds(app)
    create_boss_two_animations(app)
    create_hud_images(app)

def sound_handler(app):
    #menyer og sånt
    app.main_menu_song = music.load_looping_sound("Story_of_Alfred/Music_assets/Main_theme.mp3")
    app.map_song = music.load_looping_sound("Story_of_Alfred/Music_assets/map_song.mp3")
    app.death_song = music.load_looping_sound("Story_of_Alfred/Music_assets/death_song.mp3")

    #bosser og sånt
    app.music_boss_one = music.load_looping_sound("Story_of_Alfred/Music_assets/Boss_one_song.mp3")
    app.music_boss_two = music.load_looping_sound("Story_of_Alfred/Music_assets/boss_2.mp3")     
    app.music_boss_three = music.load_looping_sound("Story_of_Alfred/Music_assets/boss_3.mp3")
    app.final_boss_song = music.load_looping_sound("Story_of_Alfred/Music_assets/Final_boss.mp3")
    
def profile_manager(app):
    pass

def create_player_animations(app):

    #### idle animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/idle1.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/idle2.png")
    image2 = scaled_image(image, 2)
    app.player_idle_animation = [image1 , image2, image1, image2]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_idle_animation1 = [rimage1, rimage2 , rimage1, rimage2]
    #attack animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack3.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack4.png")
    image4 = scaled_image(image , 2)
    app.player_attack_animation = [image4 , image3, image2, image1]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_attack_animation1 = [rimage4, rimage3, rimage2, rimage1]

    ### walking animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking3.png")
    image3 = scaled_image(image , 2)

    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    
    app.player_walking_animation = [image1 , image2 , image3, image2]
    app.player_walking_animation1 = [rimage1, rimage2, rimage3, rimage2]
    image = load_image("Story_of_Alfred/Sprite_assets/player/iframe.png")
    image1 = scaled_image(image , 2)
    image2 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_iframes = image1
    app.player_iframesr = image2

def create_boss_one_animations(app):
    image = load_image("Story_of_Alfred/Sprite_assets/Boss_1.png")
    image1 = scaled_image(image, 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss_one_idle = [image1]
    app.boss_one_idle1 = [rimage1]

    image = load_image("Story_of_Alfred/Sprite_assets/Boss_1_charge.png")
    image1 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss_one_charge = [image1]
    app.boss_one_charge1 = [rimage1]


    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/3.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/4.png")
    app.boss1_attack1 = [image1, image2, image3, image4]

    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack1f = [rimage1, rimage2, rimage3, rimage4]


    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/5.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/6.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/7.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/8.png")
    image5 = scaled_image(image , 2)
    app.boss1_attack2 = [image1, image2, image3, image4,image5]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    rimage5 = image5.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack2f = [rimage1, rimage2, rimage3, rimage4, rimage5]
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/3.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/4.png")
    image4 = scaled_image(image , 2)
    app.boss1_attack3 = [image1, image2, image3, image4]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack3f = [rimage1, rimage2, rimage3, rimage4]


def create_boss_two_animations(app):
    
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/3.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/4.png")
    image5 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/5.png")
    image6 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/6.png")
    image7 = scaled_image(image , 2)
    app.boss_two_idle = [image1, image2,image3, image4, image5, image6, image7]



    image = load_image("Story_of_Alfred/Sprite_assets/b2_a1_0.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a1_1.png")
    image2 = scaled_image(image , 2)
    app.b2_a1_i = [image1, image2]
    image = load_image("Story_of_Alfred/Sprite_assets/b2_p1.png")
    image1 = scaled_image( image , 2)
    app.b2_p1_i = image1
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a3_0.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a3_1.png")
    image2 = scaled_image(image , 2)
    app.b2_a3_i = [image1, image2]


def create_backgrounds(app):
    image = load_image("Story_of_Alfred/Sprite_assets/Background.png")
    #image = scaled_image(image)
    app.main_menu_bg = image
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b1.png")
    image1 = scaled_image(image , 2)
    app.boss_one_bg = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b2.png")
    image1 = scaled_image(image, 2)
    app.boss_two_bg = image1

def create_hud_images(app):
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/Frame_1.png")
    image1 = scaled_image(image , 2)
    app.healthbar = image1
def timer_fired(app):

    if app.game_state == "Running":

        player_movement(app)
        timer_player_char_one(app)
        if app.boss_fight == "One":
            boss_one_timer(app)
        if app.boss_fight == "Two":
            boss_two_timer(app)


def input_delay(app):
    if app.input_delay > 0:
        app.input_delay -= 1
    if app.input_delay_menu > 0:
        app.input_delay_menu -= 1

def timer_player_char_one(app):
    player_animation_timer(app)
    if app.i_frames > 0:
        app.player_color = "pink"
    else:
        app.player_color = "red"
    if app.basic_attack_cooldown > 0:
        app.basic_attack_cooldown -= 1
    if app.dodge_timer > 0:
        app.dodge_timer -= 1
    if app.dash_timer > 0:
        app.dash_timer -= 1
    if app.attack_stops_movement > 0:
        app.attack_stops_movement -= 1
    if app.i_frames > 0:
        app.i_frames -= 1
    if app.show_basic_attack > 0:
        app.show_basic_attack -= 1
    if app.idle_counter > 0:
        app.idle_counter -= 1
    if app.idle_counter == 0 and app.player_moving == False:
        app.player_state = "Idle"
    if app.player_health <= 0:
        kill_player(app)
    input_delay(app)
    

### animation timere
def player_animation_timer(app):
    app.do_animation += 1

    if app.do_animation > 10:
        if app.animation_counter < 3:
            app.animation_counter += 1
            app.do_animation = 0
        elif app.animation_counter == 3:
            app.animation_counter = 0
            app.do_animation = 0


def boss_animation_timer(app):
    app.enemy_do_animation += 1
    if app.enemy_do_animation > 10:
        if app.enemy_animation_counter > 4:
            app.enemy_animation_counter += 1
            app.enemy_do_animation = 0
        else:
            app.enemy_animation_counter = 0
            app.enemy_do_animation = 0



### timere kan importeres fra et annet dokument??
##### boss timere
def boss_one_timer(app):
    #finn ut retningen til boss
    if app.enemy_pos_x > app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = 1
    if app.enemy_pos_x < app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = -1
    #regn ut hva boss skal gjøre
    if app.enemy_action == "Idle":
        boss_one_action_calc(app)

    #kan boss gjøre noe?
    #hver action gir en cd
    #burde ryddes opp?
    if app.enemy_cd == 0:
        if app.enemy_action == "Walk_West":
            app.enemy_pos_x -= 20
            app.enemy_pos_hix -= 20
            app.enemy_cd += 10
            app.enemy_action = "Idle"
        elif app.enemy_action == "Walk_East":
            app.enemy_pos_x += 20
            app.enemy_pos_hix += 20
            app.enemy_cd += 10
            app.enemy_action = "Idle"
        elif app.enemy_action == "Attack_1":
            if app.boss_stagger == 0:
                app.b1_a1_f = 0
                app.animate_b1_a1 = True
            app.boss_stagger += 1
            if app.boss_stagger % 4 == 0:
                app.b1_a1_f += 1
            if app.boss_stagger > 10:
                boss_one_attack_1(app)
                app.enemy_cd += 8
                app.enemy_action = "Attack_2"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.b1_a1_f = 0

        elif app.enemy_action == "Attack_2":                
            app.boss_stagger += 1
            if app.boss_stagger % 2 == 0:
                app.b1_a1_f += 1
            if app.boss_stagger > 4:
                boss_one_attack_2(app)
                app.enemy_cd += 20
                app.enemy_action = "Idle"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.animate_b1_a1 = False

        elif app.enemy_action == "Attack_3":
            if app.boss_stagger == 0:
                app.b1_a1_f = 0
                app.animate_b1_a1 = True
            app.boss_stagger += 1
            if app.boss_stagger % 2 == 0:
                app.b1_a1_f += 1
            if app.boss_stagger > 4:
                boss_one_attack_3(app)
                app.enemy_cd +=10
                app.enemy_action = "Idle"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.animate_b1_a1 = False

    #ta ned cd et punkt
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1

        

def boss_two_timer(app):
    
    if app.boss_stage == "One":

        if app.enemy_action == "Idle":
            boss_two_action_calc_phase_1(app)
        if app.enemy_cd == 0:
           
            if app.enemy_action == "Attack_1":
                app.boss_stagger += 1
                if app.boss_stagger == 1:
                    boss_two_show_attack_1(app)
                    app.stop_showing_b2_a1 = 30
                if app.boss_stagger > 12:
                    boss_two_attack_1(app)
                    app.enemy_cd += 20
                    app.enemy_action = "Idle"
                    
            if app.enemy_action == "Attack_2":
                boss_two_attack_2(app)
                app.enemy_cd += 20
                app.enemy_action = "Idle"
                app.enemy_projectile_cd += 50
            if app.enemy_action == "Attack_3":

                app.boss_stagger += 1
                if app.boss_stagger == 1:
                    boss_two_show_attack_3(app)
                    app.stop_showing_b2_a3 = 20
                if app.boss_stagger > 8:
                    boss_two_attack_3(app)
                    app.enemy_cd += 12
                    app.enemy_action = "Idle"


    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.stop_showing_b2_a1 > 0:
        app.stop_showing_b2_a1 -= 1
    if app.stop_showing_b2_a1 == 0:
        app.show_attack_1 = False 
    if app.stop_showing_b2_a3 > 0:
        app.stop_showing_b2_a3 -= 1
    if app.stop_showing_b2_a3 == 0:
        app.show_attack_3 = False
    if app.enemy_tp_cd > 0:
        app.enemy_tp_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1
    if app.enemy_projectile_cd > 0:
        app.enemy_projectile_cd -= 1
    app.animation_tick += 1
    if app.animation_tick % 7 == 0:
        if app.b2_animation <= 6:
            app.b2_animation_f += 1
            app.b2_animation += 1
        if app.b2_animation >= 7:
            app.b2_animation_f = 0
            app.b2_animation = 0
    
    projectile_manager_1(app)
    if app.boss_two_teleport == True:
        if app.tp_counter > 0:
            app.tp_counter -= 1
        if app.tp_counter == 0:
            random_factor = (10 * random.randrange(11))
            app.boss_two_teleport = False
            if app.enemy_pos_x - 1700 + random_factor < 50:
                app.enemy_pos_x = 720
                app.enemy_pos_hix = 736
            else:
                app.enemy_pos_x -= 1600 + random_factor
                app.enemy_pos_hix -= 1600 + random_factor
                
                


#####
def boss_one_action_calc(app):
    if app.enemy_pos_x >= app.player_pos_x + 100:
            app.enemy_action = "Walk_West"
    elif app.enemy_pos_x <= app.player_pos_x - 100:
            app.enemy_action = "Walk_East"
    elif random.randrange(5) == 3:
        app.enemy_action = "Attack_3"
    else:
        app.enemy_action = "Attack_1"

def boss_two_action_calc_phase_1(app):
    #teleport kanskje
    #range attack (untill hit)
    #summon on top of player
    #two phases
    attack_prompt = random.randrange(2)
    #move if need to move


    #or else do an attack
    if attack_prompt == 0 and app.enemy_action == "Idle":
            app.enemy_action = "Attack_1"
            
    elif attack_prompt == 1 and app.enemy_projectile_cd == 0 and app.enemy_action == "Idle" and app.b2_p_cd == False:
            app.enemy_action = "Attack_2"

    if attack_prompt == 1 and app.enemy_action == "Idle":
            app.enemy_action = "Attack_3"

def boss_two_action_calc_phase_2(app):
    attack_prompt = 1
    if attack_prompt == 0 and app.enemy_action == "Idle":
        app.enemy_action = "Attack_1"
    elif attack_prompt == 1 and app.enemy_action == "Idle":
        app.enemy_action = "Attack_3"
    
#### attacks


############################
############ Boss one ################
#################################
def boss_one_attack_1(app):

    if app.enemy_direction == 1:
        app.enemy_attack_x1 = app.enemy_pos_x -10 * app.enemy_direction
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 60 * app.enemy_direction
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix -10 * app.enemy_direction
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix - 60 * app.enemy_direction
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
            app.player_health -= 10
            app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_one_attack_2(app):
    #disse variablene trenger ikke være app hvis jeg ikke skal vise angrepene
    if app.enemy_direction == 1:
        app.enemy_attack_x1 = app.enemy_pos_x -20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x + 10 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix -20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 10 
        app.enemy_attack_y2 = app.enemy_pos_y + 10

    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_one_attack_3(app):
    if app.enemy_direction == 1:

        app.enemy_attack_x1 = app.enemy_pos_x - 20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix + 20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10

    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

############################
############ Boss two ################
#################################
def boss_two_attack_1(app):
    app.b2_a1_c = 1
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 12
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_two_show_attack_1(app):
    random_factor = random.randrange(3)
    app.enemy_attack_x1 = app.player_pos_x - 20 + (10 * random_factor)
    app.enemy_attack_y1 = app.player_pos_hiy
    app.enemy_attack_x2 = app.player_pos_hix + 20 + (10 * random_factor)
    app.enemy_attack_y2 = app.player_pos_hiy - 20
    app.show_attack_1 = True
    app.b2_a1_c = 0

    
def boss_two_attack_2(app):
    area = app.player_pos_x + 12, app.player_pos_hix -12
    app.b2_p_cd = False
    create_projectile_1(app, area)

def boss_two_attack_3(app):
    app.b2_a3_c = 1
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 8
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_two_show_attack_3(app):
    random_factor = random.randrange(-10, 10)
    app.enemy_attack_x1 = app.player_pos_x - 20 + (10 * random_factor)
    app.enemy_attack_y1 = app.player_pos_hiy
    app.enemy_attack_x2 = app.player_pos_hix + 20 + (10 * random_factor)
    app.enemy_attack_y2 = app.player_pos_hiy - 20
    app.show_attack_3 = True
    app.b2_a3_c = 0


def teleport_boss_two(app):
    app.tp_counter = 40
    app.boss_two_teleport = True
    app.enemy_pos_x += 1500
    app.enemy_pos_hix += 1500

##### animation handlers

def boss_animation_handler(app):
    pass

####projectile manager
def create_projectile_1(app, area):
    x1 = area[0]
    x2 = area[1]

    y1= 100
    y2= 124

    app.projectile_1 = [[x1, y1 , x2 ,y2],
                        [x1 + 60, y1-300, x2+ 60, y2-300]
                ]
    app.projectile_speed = 10
    app.show_projectile_1 = True
    app.show_projectile_2 = True

def projectile_manager_1(app):
    if app.projectile_1[0][1] < 700:
        app.projectile_1[0][1] += app.projectile_speed
        app.projectile_1[0][3] += app.projectile_speed
    else:
        app.show_projectile_1 = False
        

    if app.projectile_1[1][1] < 700:
        app.projectile_1[1][1] += app.projectile_speed
        app.projectile_1[1][3] += app.projectile_speed
    else:
        app.show_projectile_2 = False
        app.b2_p_cd = False
    if app.projectile_1[0][1] <= app.player_pos_hiy and app.projectile_1[0][1] >= app.player_pos_y:
        if collision_detection_enemy_attack(app, app.projectile_1[0]) == True and app.i_frames == 0:
            app.player_health -= 5
            app.i_frames += 5


    if app.projectile_1[1][1] <= app.player_pos_hiy and app.projectile_1[1][1] >= app.player_pos_y:
        if collision_detection_enemy_attack(app, app.projectile_1[1]) == True and app.i_frames == 0:
            app.player_health -= 5
            app.i_frames += 5
##############Keys#################


def key_released(app, event):
    if (event.key == "Enter"):
        input_delay(app)
    if app.game_state == "Running":
        if (event.key == "a") and app.player_direction == "West":
            app.player_moving = False
            
        if (event.key == "d") and app.player_direction == "East":
            app.player_moving = False



def key_pressed(app, event):
    if app.game_state == "Menu":
        if (event.key == app.enter_bind):
            main_menu_pressed(app)
        elif (event.key == "w"):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == "s"):
            if app.menu_selector < 2:
                app.menu_selector += 1

    if app.game_state == "Map":
        if (event.key == app.enter_bind) and app.input_delay_menu == 0:
            map_button_pressed(app)

        elif (event.key == "w"):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == "s"):
            if app.menu_selector < 2:
                app.menu_selector += 1
    if app.game_state == "Boss_One_Down":
        if (event.key == app.enter_bind):
            next_boss(app)
    if app.game_state == "Boss_Two_Down":
        if (event.key == app.enter_bind):
            next_boss(app)

    if app.game_state == "Dead":
        if (event.key == "r"):
            if app.player_lives > 0:
                if app.boss_fight == "One":
                    init_boss_1(app)
                    init_playable_character_one(app)
                if app.boss_fight == "Two":
                    init_boss_2(app)
                    init_playable_character_one(app)

            else:
                map_init(app)

    if app.game_state == "Running":
        if (event.key == "h") and app.dash_timer == 0:
            app.player_pos_x += 40 * app.player_facing
            app.player_pos_hix += 40 * app.player_facing
            app.dash_timer = 20
            app.i_frames += 2
        if (event.key == "g") and app.dodge_timer == 0:
            app.dodge_timer += 20
            player_dodge(app)
        if (event.key == "a") and app.input_delay == 0 and app.attack_stops_movement == 0:
            app.player_direction = "West"
            app.player_moving = 1
        elif (event.key == "d") and app.input_delay == 0 and app.attack_stops_movement == 0:
            app.player_direction = "East"
            app.player_moving = 1 
        elif (event.key == "j") and app.basic_attack_cooldown == 0:
            basic_attack(app)
            

    app.listening_to_input = event.key
#listener key_pressed bare etter en key?


##############################
############init game#######
############################

def init_baby(app):
    app.player_lives = 3

def init_easy(app):
    app.player_lives = 1

def init_hard(app):
    pass

################################
###############init classes##########
###############################
def init_playable_character_one(app):
    app.player_direction = "East"
    app.player_state = "Idle"
    app.player_moving = False
    app.player_health = 100
    app.player_pos_x = 300 -48
    app.player_pos_y = 380
    app.player_pos_hix = 300
    app.player_pos_hiy = 424 

def soft_init_player(app):
    app.player_direction = "East"
    app.player_state = "Idle"
    app.player_pos_x = 300 -48
    app.player_pos_y = 380
    app.player_pos_hix = 300
    app.player_pos_hiy = 424 

def init_boss_1(app):
    music.stop_all_sounds()
    app.boss_fight = "One"
    app.boss_stage = ""
    app.enemy_action = "Idle"
    app.enemy_direction = 1
    app.enemy_health = 900
    app.enemy_pos_x = 700
    app.enemy_pos_hix = 740
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.game_state = "Running"
    app.music_boss_one.play()
    app.animate_b1_a1 = False
    app.b1_a1_f = 0
    app.animation_tick = 0
    app.stagger = False

def init_boss_2(app):
    music.stop_all_sounds()
    app.enemy_direction = 1
    app.show_attack_1 = False
    app.show_attack_3 = False
    app.boss_fight = "Two"
    app.boss_stage = "One"
    app.enemy_action = "Idle"
    app.enemy_health = 1200
    app.enemy_pos_x = 720
    app.enemy_pos_hix = 736
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.enemy_cd = 20
    app.game_state = "Running"
    app.music_boss_two.play()
    app.enemy_attack_pos_x = 0
    app.enemy_attack_pos_y = 0
    app.stop_showing_b2_a1 = 0
    app.stop_showing_b2_a3 = 0
    app.enemy_tp_cd = 0
    app.boss_two_teleport = False
    app.b2_p_cd = False
    app.b2_animation_f = 0
    app.animation_tick = 0
    app.b2_animation = 0

def init_boss_3(app):
    pass
def init_final_boss(app):
    music.stop_all_sounds()
    app.boss_fight = "Final"
    app.boss_stage = "One"
    app.enemy_health = 3000
    app.enemy_pos_x = 700
    app.enemy_pos_hix = 740
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.game_state = "Running"
    

    




######

###########player management######
    
def player_movement(app):
    if app.player_direction == "West" and app.attack_stops_movement == 0:
        app.player_facing = -1
    elif app.player_direction == "East" and app.attack_stops_movement == 0:
        app.player_facing = 1 

    if app.player_direction == "West" and app.player_moving == True and app.attack_stops_movement == 0:
        app.player_pos_x -= 10 
        app.player_pos_hix -= 10
        app.player_state = "Walking"
    elif app.player_direction == "East" and app.player_moving == True and app.attack_stops_movement == 0:
        app.player_pos_x += 10 
        app.player_pos_hix += 10
        app.player_state = "Walking"

def player_health(app):
    if app.player_health == 0:
        pass

def basic_attack(app):
    app.basic_attack_cooldown += 10
    app.attack_stops_movement = 12
    app.show_basic_attack = 10
    app.player_state = "Attack"
    app.idle_counter = 10
    app.do_animation = 5
    app.animation_counter = 0

    if app.player_direction == "East":
        attack_hitbox = app.player_pos_hix, app.player_pos_y+40, app.player_pos_hix + 60, app.player_pos_y+20
    if app.player_direction == "West":
        attack_hitbox = app.player_pos_x - 60, app.player_pos_y+40, app.player_pos_x, app.player_pos_y+20
    app.attack_hitbox = attack_hitbox
    if attack_collision_detection(app, attack_hitbox) == True:
        app.enemy_hit = 10
        if app.enemy_health - 50 <= 0:
            kill_enemy(app)

        elif app.enemy_health >= 0:
            app.enemy_health -= 50

        if app.boss_fight == "Two" and app.boss_stage == "One":
            teleport_boss_two(app)

def player_dodge(app):
    app.i_frames = 6


def player_dead_check(app):
    if app.player_health > 1:
        #player død
        
        pass

####collison detection

def attack_collision_detection(app, attack_hitbox):
    hitbox_lo_x = attack_hitbox[0] 
    hitbox_lo_y = attack_hitbox[1]
    hitbox_hi_x = attack_hitbox[2] 
    hitbox_hi_y = attack_hitbox[3] 
    #if hit, enemy_hit += 10
    if hitbox_lo_x >= app.enemy_pos_x and hitbox_lo_x <= app.enemy_pos_x + 100:
        enemy_hit = True
        return enemy_hit
    elif hitbox_hi_x >= app.enemy_pos_x and hitbox_hi_x <= app.enemy_pos_x + 50:
        enemy_hit = True
        return enemy_hit
    
def collision_detection_enemy_attack(app, attack_hitbox):
    hitbox_lo_x = attack_hitbox[0] 
    hitbox_lo_y = attack_hitbox[1]
    hitbox_hi_x = attack_hitbox[2] 
    hitbox_hi_y = attack_hitbox[3] 

    #to fix##############
    if hitbox_lo_x >= app.player_pos_x and hitbox_hi_x <= app.player_pos_x:
        enemy_hit = True
    elif hitbox_lo_x >= app.player_pos_hix and hitbox_hi_x <= app.player_pos_hix:
        enemy_hit = True
    elif (hitbox_lo_x + hitbox_hi_x) / 2 >= app.player_pos_x and (hitbox_lo_x + hitbox_hi_x) / 2 <= app.player_pos_hix:
        enemy_hit = True
    elif app.player_pos_x >= hitbox_lo_x and app.player_pos_x <= hitbox_hi_x:
        enemy_hit = True
    elif app.player_pos_hix >= hitbox_lo_x and app.player_pos_hix <= hitbox_hi_x:
        enemy_hit = True
    else:
        enemy_hit = False
    return enemy_hit

def collision_detection(app):
    if app.player_pos_x == app.enemy_pos_x or app.player_pos_x == app.enemy_pos_x + 50:
        if app.i_frames > 0:
            pass
        else:
            app.player_health -= 1
            app.i_frames += 4
    

    

def kill_enemy(app):
    killed_boss_init(app)

def killed_boss_init(app):
    if app.boss_fight == "One":
        app.game_state = "Boss_One_Down"
    if app.boss_fight == "Two":
        app.game_state = "Boss_Two_Down"
    
def next_boss(app):
    if app.boss_fight == "One":
        soft_init_player(app)
        init_boss_2(app)
    #if app.boss_fight == "Two":
        #init_boss_3(app)
    else:
        map_init(app)

def kill_player(app):
    death_screen_init(app)

##### settings controllere####
def main_menu_pressed(app):
    if app.menu_selector == 0:
        map_init(app)
        app.input_delay_menu += 1
        
    if app.menu_selector == 1:
        settings_init(app)

def map_button_pressed(app):
    if app.menu_selector == 0:
        init_boss_1(app)
        init_playable_character_one(app)
    if app.menu_selector == 1:
        init_boss_2(app)
        init_playable_character_one(app)

##### menyer init#####
def map_init(app):
    music.stop_all_sounds()

    app.game_state = "Map"
    app.map_song.play()

def settings_init(app):
    app.game_state = "Settings"


def death_screen_init(app):
    music.stop_all_sounds()
    app.game_state = "Dead"
    app.death_song.play()


#### mitt tegnebrett ##################
def redraw_all(app, canvas):
    if app.game_state == "Menu":
        draw_main_menu(app, canvas)
        draw_main_menu_selector(app, canvas)
        for button in app.main_menu_buttons:
            draw_main_menu_buttons(app, button , canvas)

    if app.game_state == "Map":
        draw_map_selector(app, canvas)
        for button in app.map_buttons:
            draw_map_buttons(app, button , canvas)
    if app.game_state == "Settings":
        for button in app.settings_buttons:
            draw_setting_buttons(app, button, canvas)


    if app.game_state == "Boss_One_Down":
        canvas.create_text(450, 450, text=f"Borg is dead\r press {app.enter_bind} to continue")
    if app.game_state == "Boss_Two_Down":
        canvas.create_text(450, 450, text=f"Berg is dead\r press {app.enter_bind} to continue")
    if app.game_state == "Dead":
        draw_death_screen(app, canvas)
    if app.game_state == "Running":
        draw_backgrounds(app, canvas)
        if app.show_basic_attack > 0 and app.debug == True:
            draw_basic_attack(app, canvas)
            draw_character_hitbox(app, canvas)
        draw_character_advanced(app, canvas)
        if app.debug == True:
            canvas.create_text ( 100, 300 ,
                                text=f"{app.player_state}",
                                font="times 30")
            canvas.create_text(100, 400,
                            text=app.enemy_action)
        
        if app.boss_fight == "One":
            if app.debug == True:
                draw_boss_one_hitbox(app, canvas)
                draw_boss_one_healthbar(app, canvas)
            draw_boss_one(app, canvas)
            
           

        if app.boss_fight == "Two":
            draw_boss_two(app, canvas)
            if app.show_boss_attack > 0 and app.debug == True:
                draw_boss_two_attack(app, canvas)
            if app.show_projectile_1 == True:
                canvas.create_image(app.projectile_1[0][0] + 12, app.projectile_1[0][1],pil_image=app.b2_p1_i)

            if app.show_projectile_2 == True:

                canvas.create_image(app.projectile_1[1][0] + 12, app.projectile_1[1][1],pil_image=app.b2_p1_i)


#### knapper for mitt tegnebrettapp.projectile_1 = [x1, y1 , x2 ,y2]

def main_menu_buttons(app):
    app.main_menu_buttons =[[100 , 100, 300 , 300 , "Start"],
                            [100 , 320 , 300 , 520 , "Settings"],
                            [100 , 540, 300 , 740, "Blank"]
                        ]
def map_buttons(app):
    #temp, må polishes
    app.map_buttons = [[100, 100, 400 , 400, "Boss 1"],
                       [100 , 450, 400 , 750, "Boss 2"],
                       [450, 100, 750, 400, "Boss 3"]
                    ]
def settings_buttons(app):

    app.settings_buttons = [[100, 100, 400 , 400, "Rebinds"],
                            [100, 450, 400, 750, "TOM"]
                            ]
################ tegne funksjoner ################

def draw_main_menu_buttons(app, button , canvas):
    x1, y1, x2, y2 , label = button
    canvas.create_rectangle(x1, y1, 
                            x2, y2,
                            fill=app.button_color)
    canvas.create_text( (x1 + x2)/2, (y1+y2)/2,
                       text=label)
    
def draw_map_buttons(app, button , canvas):
    x1, y1, x2, y2 , label = button
    canvas.create_rectangle(x1, y1, 
                            x2, y2,
                            fill=app.button_color)
    canvas.create_text( (x1 + x2)/2, (y1+y2)/2,
                       text=label)
def draw_setting_buttons(app, button , canvas):
    x1, y1, x2, y2 , label = button
    canvas.create_rectangle(x1, y1, 
                            x2, y2,
                            fill=app.button_color)
    canvas.create_text( (x1 + x2)/2, (y1+y2)/2,
                       text=label)

def draw_settings(app):
    pass
def draw_main_menu(app, canvas):

    canvas.create_image(450, 450 , pil_image=app.main_menu_bg)

def draw_main_menu_selector(app, canvas):
    canvas.create_rectangle(100, 100 + (app.menu_selector) * 220, 
                            300 , 300 + (app.menu_selector *220),
                            fill="", outline="red",width=5)
    
def draw_map_selector(app, canvas):
    canvas.create_rectangle(100, 100 + (app.menu_selector) * 350, 
                            400 , 400 + (app.menu_selector *350),
                            fill="", outline="red",width=5)

def draw_map(app, canvas):
    pass

def draw_character_hitbox(app, canvas):
    
    canvas.create_rectangle(app.player_pos_x, app.player_pos_y ,
                       app.player_pos_hix, app.player_pos_hiy,
                       fill=app.player_color)
    canvas.create_polygon(app.player_pos_x + 20 , app.player_pos_y - 30,
                          app.player_pos_x + 10 , app.player_pos_y - 40,
                          app.player_pos_x + 20, app.player_pos_y - 50,
                          fill="black"
                        )

    
def draw_character_advanced(app, canvas):

    ### skal byttes ut til noe renere og penere
    draw_hud_player(app, canvas)
    if app.player_state == "Idle":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y+25, pil_image=app.player_idle_animation[app.animation_counter] )
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y+25, pil_image=app.player_idle_animation1[app.animation_counter] )
    if app.player_state == "Walking":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y + 25, pil_image=app.player_walking_animation[app.animation_counter])
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y + 25, pil_image=app.player_walking_animation1[app.animation_counter])
    if app.player_state == "Attack":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48 , app.player_pos_y + 25 , pil_image=app.player_attack_animation[app.animation_counter])
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y + 25 , pil_image=app.player_attack_animation1[app.animation_counter])
    if app.i_frames > 0:
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y+25, pil_image=app.player_iframes)
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x , app.player_pos_y+25, pil_image=app.player_iframesr)

def draw_boss_one(app , canvas):
    if app.show_boss_attack > 0 and app.debug == True:
        draw_boss_one_attack(app, canvas)
    if app.animate_b1_a1 == True and app.enemy_action == "Attack_1":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x-36, app.enemy_pos_y + 24, pil_image=app.boss1_attack1[app.b1_a1_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24, pil_image=app.boss1_attack1f[app.b1_a1_f])
    elif app.animate_b1_a1 == True and app.enemy_action == "Attack_2":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x-36, app.enemy_pos_y + 24, pil_image=app.boss1_attack2[app.b1_a1_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24, pil_image=app.boss1_attack2f[app.b1_a1_f])

    elif app.animate_b1_a1 == True and app.enemy_action == "Attack_3":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x -36, app.enemy_pos_y + 24,pil_image=app.boss1_attack3[app.b1_a1_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24,pil_image=app.boss1_attack3f[app.b1_a1_f])
    else:
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x +12, app.enemy_pos_y +24, pil_image=app.boss_one_idle[0])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 30 , app.enemy_pos_y +24, pil_image=app.boss_one_idle1[0])




   

def draw_boss_two(app, canvas):
    if app.debug == True:
        canvas.create_rectangle(app.enemy_pos_x, app.enemy_pos_y,
                                app.enemy_pos_hix, app.enemy_pos_hiy,
                                fill="green")
    canvas.create_image(app.enemy_pos_x-12, app.enemy_pos_y + 24, pil_image=app.boss_two_idle[app.b2_animation_f])
    if app.debug == True:
        canvas.create_text(app.enemy_pos_x, app.enemy_pos_y - 300,
                       text=app.enemy_health)
    if app.show_attack_1 == True:
        canvas.create_image(app.enemy_attack_x1 + 44, app.enemy_attack_y1 +1, pil_image=app.b2_a1_i[app.b2_a1_c])
    if app.show_attack_3 == True:
        canvas.create_image(app.enemy_attack_x1 + 44, app.enemy_attack_y1 +1, pil_image=app.b2_a3_i[app.b2_a3_c])


                     


def draw_basic_attack(app, canvas):
    canvas.create_rectangle(app.attack_hitbox[0], app.attack_hitbox[1],
                            app.attack_hitbox[2], app.attack_hitbox[3],
                            fill="blue")

def draw_enemy_attack(app, canvas):
    canvas.create_rectangle(app.enemy_attack_x, app.enemy_attack_y,
                            app.enemy_attack_x + 50, app.enemy_attack_y + 50,
                            fill="black")

def draw_boss_one_hitbox(app, canvas):
    canvas.create_rectangle(app.enemy_pos_x, app.enemy_pos_y,
                          app.enemy_pos_hix, app.enemy_pos_hiy,
                          fill=app.boss_color) 

def draw_boss_one_healthbar(app, canvas):
    canvas.create_text(app.enemy_pos_x, app.enemy_pos_y -300,
                       text=app.enemy_health)
    
def draw_boss_one_attack(app, canvas):
    canvas.create_rectangle(app.enemy_attack_x1, app.enemy_attack_y1,
                            app.enemy_attack_x2, app.enemy_attack_y2,
                            fill="blue")
def draw_boss_two_attack(app, canvas):
    canvas.create_rectangle(app.enemy_attack_x1, app.enemy_attack_y1,
                            app.enemy_attack_x2, app.enemy_attack_y2,
                            fill="blue")
def draw_death_screen(app, canvas):
    canvas.create_text(450, 450, 
                       text="You died\r press r to restart",
                       font="times, 30")

def draw_hud_player(app, canvas):
    
    canvas.create_rectangle(0 , 700 , 900, 900,
                            fill="ivory")

    canvas.create_image(200, 750, pil_image=app.healthbar)
    canvas.create_text(200, 750,
                       text=app.player_health,
                       font="times 20",
                       fill="white")
def draw_backgrounds(app, canvas):
    if app.boss_fight == "One":
        canvas.create_image(450 , 250, pil_image=app.boss_one_bg)
    if app.boss_fight == "Two":
        canvas.create_image(450 , 250, pil_image=app.boss_two_bg)
def app_stopped(app):
    music.stop_all_sounds()


run_app(width=900,height=900)
