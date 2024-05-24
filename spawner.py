import random
import interations

class Mob:
    def __init__(self, mobinfo) -> None:
        '''
        #mob = {'name':'mob DEFAULT','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB'}
        self.mobname = mobinfo['name']
        self.mobHP = mobinfo['hp']
        #self.mobMaxHP = mobinfo['max_hp']
        self.mobATK = mobinfo['atk']
        self.mobDEF = mobinfo['def']
        self.mobSPD = mobinfo['spd']
        self.mobDesc = mobinfo['desc']
        '''
        pass
    
    def spawn(level, luck):
        #mob = {'name':'mob DEFAULT','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB'}
        
        # -------ESTAGIO FINAL----
        if (level == 31):
            mob = {'name':'DEMON KING','hp': 1300,'atk':380,'def':225,'spd':300,'spc_attack':'NONE', 'desc':'SUBBOSS MOB'}
        if (level == 32):
            mob = {'name':'OOLONG SATAN','hp': 2200,'atk':460,'def':325,'spd':300,'spc_attack':'NONE', 'desc':'ULTIMATE BOSS MOB'}
        
        # ------ ESTAGIO 4 -------
        if (level <= 30):
            defaultmob = {'name':'DEFAULT STAGE 4','hp': 950,'atk':480,'def':280,'spd':90,}
            
            if(luck == 0):
                mob = {'name':'mob 1','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 1):
                mob = mob = {'name':'mob 2','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 2):
                mob = mob = {'name':'mob 3','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 3):
                mob = mob = {'name':'mob 4','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
        if (level == 5):
            mob = mob = {'name':'BOSS STAGE 4','hp': defaultmob['hp'] * 5,'atk':defaultmob['atk'] * 5,'def':defaultmob['def'] * 5,'spd':defaultmob['spd'] * 2,'spc_attack':'NONE', 'desc':'BOSS 1'}
        
        # ------ ESTAGIO 3 -------
        if (level <= 20):
            defaultmob = {'name':'DEFAULT STAGE 3','hp': 700,'atk':450,'def':200,'spd':60,}
            
            if(luck == 0):
                mob = {'name':'mob 1','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 1):
                mob = mob = {'name':'mob 2','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 2):
                mob = mob = {'name':'mob 3','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 3):
                mob = mob = {'name':'mob 4','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
        if (level == 5):
            mob = mob = {'name':'BOSS STAGE 3','hp': defaultmob['hp'] * 5,'atk':defaultmob['atk'] * 5,'def':defaultmob['def'] * 5,'spd':defaultmob['spd'] * 2,'spc_attack':'NONE', 'desc':'BOSS 1'}
            
        # ------ ESTAGIO 2 -------
        if (level <= 5):
            defaultmob = {'name':'DEFAULT STAGE 2','hp': 300,'atk':200,'def':90,'spd':40,}
            
            if(luck == 0):
                mob = {'name':'mob 1','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 1):
                mob = mob = {'name':'mob 2','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 2):
                mob = mob = {'name':'mob 3','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 3):
                mob = mob = {'name':'mob 4','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
        if (level == 5):
            mob = mob = {'name':'BOSS STAGE 2','hp': defaultmob['hp'] * 5,'atk':defaultmob['atk'] * 5,'def':defaultmob['def'] * 5,'spd':defaultmob['spd'] * 2,'spc_attack':'NONE', 'desc':'BOSS 1'}
        
        # ------ ESTAGIO 1 -------
        if (level < 5):
            defaultmob = {'name':'DEFAULT STAGE 1','hp': 120,'atk':60,'def':25,'spd':30,}
            
            if(luck == 0): # -- very easy
                mob = {'name':'mob 1','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 1): # -- easy
                mob = mob = {'name':'mob 2','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 2): # -- medium
                mob = mob = {'name':'mob 3','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
            if(luck == 3): # -- hard
                mob = mob = {'name':'mob 4','hp': defaultmob['hp'],'atk':defaultmob['atk'],'def':defaultmob['def'],'spd':defaultmob['spd'],'spc_attack':'NONE', 'desc':'DEFAULT MOB 1 - very easy'}
        if (level == 5): # -- boss
            mob = mob = {'name':'BOSS STAGE 1','hp': defaultmob['hp'] * 5,'atk':defaultmob['atk'] * 5,'def':defaultmob['def'] * 5,'spd':defaultmob['spd'] * 2,'spc_attack':'NONE', 'desc':'BOSS 1'}
        
        return mob
    
    def attack(mob, player, stack, playername):
        stack = random.randint(0,100)
        print(f"mob stacks >> {stack}")
        playerDEF = player['def']
        mobATK = mob['atk']
        sorte = random.randint(0,3)
        mobCRIT = int(mob['atk'] * (sorte / 10))
        if (stack >= 100):
            stack = 0
            print('*** DANO CRÍTICO ***\n')
            dano = mobATK + mobCRIT - playerDEF
            if (dano <= 0): 
                dano = 0
                print('*** DANO ZERO ***\n')
            else:
                print('*** DANO CRÍTICO ***')
                print(f">> {playername} sofreu {dano}DMG de dano\n")
        else:
            dano = mobATK - playerDEF
            if (dano <= 0): 
                dano = 0
                print('*** DANO ZERO ***\n')
            else:
                print(f">> {playername} sofreu {dano}DMG de dano\n")

        player['hp'] -= dano
        if player['hp'] < 0:
            player['hp'] = 0
        return player