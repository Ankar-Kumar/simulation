import pygame
import numpy as np

def main():
    # pygame initalization
    pygame.init()
    pygame.display.set_caption("Bomber vs Fighter")

    screen_size = (650, 650)
    screen = pygame.display.set_mode(screen_size)

    running = True

    while running:
                screen.fill((0, 0, 0))
      
                xb, yb = np.random.randint(0, 600, 2)
                xf, yf = (50, 50)
                vf = 20
                minDist = 100
                maxDist = 600
                fx=xf
                fy=yf
                bx=xb
                by=yb
                
                cnt = 0

                while(True):
                    cnt += 1
                    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
                    print(dist)
                   
                    if (dist <= minDist):
                        print('Bomber caught at step: ' + str(cnt))
                        break
                    elif (dist >= maxDist):
                        print('Bomber escaped at step: ' + str(cnt))
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
    
    pygame.time.delay(3000)
    pygame.quit()

if __name__ == '__main__':
    main()