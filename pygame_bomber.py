import pygame
import numpy as np

def main():
    # pygame initalization
    pygame.init()
    pygame.display.set_caption("Bomber vs Fighter")

    screen_size = (650, 650)
    screen = pygame.display.set_mode(screen_size)
    
    font1 = pygame.font.SysFont('arial.tft', 20)
    running = True

    while running:
                screen.fill((0, 0, 0))
        # for event in pygame.event.get():
        #         if event.type != pygame.QUIT:
        #           running= False
                
                xb, yb = np.random.randint(0, 600, 2)
                xf, yf = (50, 50)
                vf = 20
                minDist = 100
                maxDist = 600
                fx=xf
                fy=yf
                bx=xb
                by=yb
                pos1=font1.render('caught',True,(0,255,0))
                pos2=font1.render('escaped',True,(255,0,0))
                B=font1.render('B',True,(50, 50, 250))
                F=font1.render('F',True,(200, 50, 200))
                text1 = pos1.get_rect()
                text2=pos2.get_rect()
                B_text=B.get_rect()
                F_text=F.get_rect()
                cnt = 0
                B_text.center=(20,100)
                F_text.center=(20,140)
                screen.blit(B,B_text)
                screen.blit(F,F_text)
                
                while(True):
                    pygame.draw.circle(screen, (50, 50, 250), (bx,by), 2)
                    pygame.draw.circle(screen, (200, 50, 200), (fx,fy), 2)

                    cnt += 1
                    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
                    print(dist)
                   
                    if (dist <= minDist):
                        text1.center=(25,200)
                        screen.blit(pos1,text1)
                        print('Bomber caught at step: ' + str(cnt))
                        pygame.draw.line(screen, (0, 255, 0), (xb, yb), (xf, yf))
                        pygame.display.flip()
                        break
                    elif (dist >= maxDist):
                        text2.center=(25,200)
                        screen.blit(pos2,text2)
                        print('Bomber escaped at step: ' + str(cnt))
                        pygame.draw.line(screen, (255,0, 0), (xb, yb), (xf, yf))
                        pygame.display.flip()
                        break
                    else:
                        cosA, sinA = (xb-xf)/dist, (yb-yf)/dist
                        xf, yf = (xf+vf*cosA), (yf+vf*sinA)
                        xb, yb = np.random.randint(0, 600, 2)
                        
                        # display line
                        pygame.draw.line(screen, (50, 50, 250), (bx, by), (xb, yb))
                        pygame.draw.line(screen, (200, 50, 200), (fx, fy), (xf, yf))

                        fx=xf
                        fy=yf
                        bx=xb
                        by=yb
                    
                    pygame.display.flip()
                    pygame.time.delay(250)
                
                break
    
    pygame.time.delay(5000)
    pygame.quit()

if __name__ == '__main__':
    main()