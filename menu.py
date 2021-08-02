import pygame
import os

UpgradeMenu_image = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UpgradeMenu_Width = 200
UpgradeMenu_height = 200
Upgrade_image    = pygame.image.load(os.path.join("images", "upgrade.png"))
Sell_image    = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        
        self.UpgradeMenu_image = pygame.transform.scale(UpgradeMenu_image, (UpgradeMenu_Width,UpgradeMenu_height))
        self.Menu_width = UpgradeMenu_Width
        self.Menu_height = UpgradeMenu_height
        self.rect  = self.UpgradeMenu_image.get_rect()
        self.rect.center = (x,y)
        self.rect.collidepoint(x, y)
        self.x = x -70//2
        self.y = y -70//2
        self.Upgrade_image = pygame.transform.scale(Upgrade_image, (70, 30))
        self.Sell_image = pygame.transform.scale(Sell_image, (70, 30))
        self.__buttons = [Button(self.Upgrade_image,'upgrade',self.x,self.y-self.Menu_height//4),
                          Button(self.Sell_image,'sell',self.x,self.y+self.Menu_height//2-5) ]  # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        
        # draw menu
        win.blit(self.UpgradeMenu_image,(self.rect))
        # draw button
        #win.blit(self.Upgrade_image,(self.rect))
        win.blit(self.Upgrade_image,(self.x,self.y-self.Menu_height//4))
        win.blit(self.Sell_image,(self.x,self.y+self.Menu_height//2-5))
        # (Q2) Draw buttons here
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        #print(self.rect.collidepoint(x, y))
        if self.rect.collidepoint(x, y) :
            return True
        else :
            return False
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return f'{self.name}'
        pass






