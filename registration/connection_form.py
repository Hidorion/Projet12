# coding: utf-8

# Imports
from registration import pygame_textinput
import pygame

from registration.connection import check_logs
from registration.registration_player import sign_up 

# Code

data = {}

data = { 
    "username" : {
            "init" : {
                "object" : pygame_textinput.TextInput,
                "settings" : ("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35),
                "rect" : (300, 300, 250, 35), 
                "title" : ("Username:", True, (0, 0, 0))
            },
            "output" : {
                #username object
            }
    },
    "email" : {
            "init" : {
                "object" : pygame_textinput.TextInput,
                "settings" : ("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35),
                "rect" : (300, 350, 250, 35),
                "title" : ("Email:", True, (0, 0, 0))
            },
            "output" : {
                #email object
            }
    }, 
    "password" : {
            "init" : {
                "object" : pygame_textinput.TextInput,
                "settings" : ("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35, -1, True),
                "rect" : (300, 400, 250, 35), 
                "title" : ("Password:", True, (0, 0, 0))
            },
            "output" : {
                #password object
            }
    },
    "password_confirm" : {
            "init" : {
                "object" : pygame_textinput.TextInput,
                "settings" : ("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35, -1, True),
                "rect" : (300, 450, 250, 35),
                "title" : ("Password confirm:", True, (0, 0, 0))
            },
            "output" : {
                #password_confirm object
            }
    }
}

class Fields:
    def __init__ (self):
        self.sign_up_username = False
        self.sign_in_username = False
        self.email = False
        self.sign_up_password = False
        self.password_confirm = False
        self.sign_in_username = False
        self.sign_in_password = False

# def field_init(objects, rect, font_data, field_lenght = -1, password_field = False,):
#     setattr(objects, str(objects) + "_rect", pygame.Rect(rect))
#     setattr(objects, str(objects)+ "_title", objects.font_object.render(font_data))

#field_init()

def run_game():
    # Initialize and set up screen
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Connection Form")
    screen = pygame.display.set_mode((1200, 720))
    clock = pygame.time.Clock()


    # Create TextInput-object 
    sign_up_username = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35)
    sign_up_username_rect = pygame.Rect(300, 300, 250, 35)
    sign_up_username_title = sign_up_username.font_object.render("Username:", True, (0, 0, 0))

    email = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35)
    email_rect = pygame.Rect(300, 370, 250, 35)
    email_title = email.font_object.render("Email:", True, (0, 0, 0))

    sign_up_password = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35, -1, True)
    sign_up_password_rect = pygame.Rect(300, 440, 250, 35)
    sign_up_password_title = sign_up_password.font_object.render("Password:", True, (0, 0, 0))

    password_confirm = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35, -1, True)
    password_confirm_rect = pygame.Rect(300, 510, 250, 35)
    password_confirm_title = password_confirm.font_object.render("Confirm password:", True, (0, 0, 0))

    sign_in_username = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35)
    sign_in_username_rect = pygame.Rect(750, 300, 250, 35)
    sign_in_username_title = sign_in_username.font_object.render("Username:", True, (0, 0, 0))

    sign_in_password = pygame_textinput.TextInput("", "", 35, True, (0, 0, 0), (0, 0, 0), 400, 35, -1, True)
    sign_in_password_rect = pygame.Rect(750, 370, 250, 35)
    sign_in_password_title = sign_in_password.font_object.render("Password:", True, (0, 0, 0))

    sign_up_button_pict = pygame.image.load('registration/pics/sign_up.png')
    sign_up_button_pict = pygame.transform.scale(sign_up_button_pict, (100, 30))
    sign_up_button_rect = sign_up_button_pict.get_rect()
    sign_up_button_rect.x = 370
    sign_up_button_rect.y = 560
    

    sign_in_button_pict = pygame.image.load('registration/pics/sign_in.png')
    sign_in_button_pict = pygame.transform.scale(sign_in_button_pict, (100, 30))
    sign_in_button_rect = sign_in_button_pict.get_rect()
    sign_in_button_rect.x = 820
    sign_in_button_rect.y = 410



    # for key in data.keys():
    #     for init_values in key["init"]:
    #             pygame_textinput.TextInput(data[key])
    #             pygame.Rect(data[key]["init"]["rect"])
    #             key.font_object.render(data[key]["init"]["title"])



    running = True
    update_text = False


    # Set status to each text input field


    # Start main loop
    f = Fields()
    while running:
        # Start event loop
        events = pygame.event.get()
        list_model = [f.sign_up_username, f.email, f.sign_up_password, f.password_confirm, f.sign_in_username, f.sign_in_password]
        list_var = [sign_up_username, email, sign_up_password, password_confirm, sign_in_username, sign_in_password]
        
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sign_up_username_rect.collidepoint(event.pos):
                    f = Fields()
                    f.sign_up_username = True
                    update_text = True

                elif email_rect.collidepoint(event.pos):
                    f = Fields()
                    f.email = True
                    update_text = True

                elif sign_up_password_rect.collidepoint(event.pos):
                    f = Fields()
                    f.sign_up_password = True
                    update_text = True

                elif password_confirm_rect.collidepoint(event.pos):
                    f = Fields()
                    f.password_confirm = True
                    update_text = True

                elif sign_in_username_rect.collidepoint(event.pos):
                    f = Fields()
                    f.sign_in_username = True
                    update_text = True

                elif sign_in_password_rect.collidepoint(event.pos):
                    f = Fields()
                    f.sign_in_password = True
                    update_text = True

                elif sign_up_button_rect.collidepoint(event.pos):
                    inputs_list = []
                    inputs_list.append(sign_up_username.input_string)
                    inputs_list.append(email.input_string)
                    inputs_list.append(sign_up_password.input_string)
                    inputs_list.append(password_confirm.input_string)
                    inputs_tuple = tuple(inputs_list)
                    sign_up(inputs_tuple, screen, 3, 3)
                    
                    

                    

                elif sign_in_button_rect.collidepoint(event.pos):
                    inputs_list = []
                    inputs_list.append(sign_in_username.input_string)
                    inputs_list.append(sign_in_password.input_string)
                    inputs_tuple = tuple(inputs_list)
                    if check_logs(inputs_tuple) :
                        running = False
                        return False, inputs_list[0]
                    
                else:
                    f = Fields()
                    # update_text = False
                



        # Feed it with events every frame 
        if update_text:
            for num, model in enumerate(list_model):
                if model :
                    list_var[num].update(events)


        # Main menu
        banner = pygame.image.load('registration/pics/game_banner_named.png')
        banner = pygame.transform.scale(banner, (1200, 720))
        banner_rect = banner.get_rect()

        screen.blit(banner, (0, 0))

        # Create and show connection rect, all text fields in there
        connection_rect = pygame.Rect(250, 250, 350, 350)
        pygame.draw.rect(screen, (0, 0, 0), connection_rect, 1)
        #connection_rect.font_object.render("Connection:", True, (0, 0, 0))

        # Create and show sign in rect, all text fields in there
        sign_in_rect = pygame.Rect(700, 250, 350, 200)
        pygame.draw.rect(screen, (0, 0, 0), sign_in_rect, 1)

        # Show connection text fields rect
        pygame.draw.rect(screen, (0, 0, 0), sign_up_username_rect, 1)
        pygame.draw.rect(screen, (0, 0, 0), email_rect, 1)
        pygame.draw.rect(screen, (0, 0, 0), sign_up_password_rect, 1)
        pygame.draw.rect(screen, (0, 0, 0), password_confirm_rect, 1)

        # Show sign up text fields rect
        pygame.draw.rect(screen, (0, 0, 0), sign_in_username_rect, 1)
        pygame.draw.rect(screen, (0, 0, 0), sign_in_password_rect, 1)

        # Blit connection surface onto the screen    
        screen.blit(sign_up_username.get_surface(), (300, 300))
        screen.blit(sign_up_username_title, (sign_up_username_rect.x, sign_up_username_rect.y - 25))

        screen.blit(email.get_surface(), (300, 370))
        screen.blit(email_title, (email_rect.x, email_rect.y - 25))

        screen.blit(sign_up_password.get_surface(), (300, 440))
        screen.blit(sign_up_password_title, (sign_up_password_rect.x, sign_up_password_rect.y - 25))

        screen.blit(password_confirm.get_surface(), (300, 510))
        screen.blit(password_confirm_title, (password_confirm_rect.x, password_confirm_rect.y - 25))

        # Blit connection surface onto the screen    
        screen.blit(sign_in_username.get_surface(), (750, 300))
        screen.blit(sign_in_username_title, (sign_in_username_rect.x, sign_in_username_rect.y - 25))

        screen.blit(sign_in_password.get_surface(), (750, 370))
        screen.blit(sign_in_password_title, (sign_in_password_rect.x, sign_in_password_rect.y - 25))

        screen.blit(sign_up_button_pict, sign_up_button_rect)

        screen.blit(sign_in_button_pict, (sign_in_button_rect))

        # Refresh screen
        pygame.display.update()
        clock.tick(30)




