print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

congratulations = ('''

                    Cft1tfC0                                              0GCCG0                    
                 L;   ...   :tGLLLLCCCCCCCCCCCCCCCCCCGCGGGGGGGGGGGGG0  Gi::;iii;:iC                 
               G:  ;1i;;i1t1                     .............,,,,,, ,;.1G0GCCG00f,;0               
              G. ,f;  ;ii;,10:   C0000000000 0                      . ,0 LtLLLfii  i.0              
              ; .f, :0    0,1 ::;                                   : G tL      t 0 ,;              
              : .f  i      0;G                                      ;. GL       0 L i,              
              f  t, .C       0 0                                    ii 0        :.   f              
               ; .t,  L        L0                                   1t        0: 0 :;               
                i .1;  i       fL                                   ,f       f , 0:1                
                 f. ;1, .f     G1                                  L L     C, t f:L                 
                  0i .11, ,C    :0                                 , 0   L, i0G;i0                  
                    G; ,1t, :C  t;                                1 ;  L, ;GG1iG                    
                      Gi ,tt: :C ,L                              L  ff. ;CC11G                      
                        01.,1f; :1.G                            G.    ;LCtt0                        
                           L:,ifi. .0                          G.   ;fLtL                           
                             G1:if1. C                        L   :tfLG                             
                                f;it;;                        t:.ifC0                               
                                  Cii0 0                     C 0tG                                  
                                 0  C, Lf0                 f:f0t                                    
                                 GLCff  G1t0            0t..C  CGGC0                                
                                          L:t          1. i                                         
                                            ;,0      G, .L                                          
                                             ;.0    0. .C                                           
                                             G i    t  1                                            
                                             0 :    t  L                                            
                                             G ,    f  G                                            
                                             C .    L  0                                            
                                             L  0   C .                                             
                                             t  G   0 ,                                             
                                             i  C   0 ,                                             
                                            0.  0    i 0                                            
                                         Gfi.  t     0::fC0                                         
                                     0f;.  .;1L        Cf111fL0                                     
                                     i tLG0                 GCi0                                    
                                     Cf                       L                                     
                                   L111111ttttfffffLLLLCCCCCGGGG0                                   
                                   i LLLGGCCCGCCCGGGGG0000  00  1                                   
                                   i    i;:,,,.........,,,:;1   :                                   
                                   ; 0 0  i1iiiiiiiiii11i1; :  0 G                                  
                                   ; G  , 0               G t  C C                                  
                                   ; G  , 0                 L  L L                                  
                                   : G  , LCCCCGGGGGG00000 ;0  f t                                  
                                 1...C  tiiii111ttfffLCCCG00   t ..f                                
                                 i 1                           0G, t                                
                                 ; .,.,.....                   ..  i                                
                                 GLLfffffffffftttttttttttttttttttffC     
                                 
''')

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.') 

left_right = input('Left or Right?').lower()

if left_right == 'left': 
    swim_or_wait = input('Swim or Wait?').lower()
    if swim_or_wait == 'wait':
        each_door = input('Wich door? (RED / BLUE / YELLOW)').lower()
        if each_door == 'yellow':
            print('You win!')
            print(congratulations)
        elif each_door == 'red':
            print('Burned by fire! GAME OVER!')
        elif each_door == 'blue':
            print('Eaten by beasts! GAME OVER!')
        else:
            print('Game Over!')
    else:
        print('Attacked by trout! GAME OVER!')
else:
    print('Fall into a hole! GAME OVER!')
