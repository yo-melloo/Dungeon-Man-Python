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
            mob = {'name':'mob subBOSS final stage','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        if (level == 32):
            mob = {'name':'mob FINAL BOSS','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 4 -------
        if (level <= 30):
            if(luck == 0):
                mob = {'name':'mob 13','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'mob 14','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'mob 15','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'mob 16','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 30):
            mob = {'name':'mob BOSS stage 4','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 3 -------
        if (level <= 20):
            if(luck == 0):
                mob = {'name':'mob 9','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'mob 10','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'mob 11','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'mob 12','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 5):
            mob = {'name':'mob BOSS','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        if (level == 20):
            mob = {'name':'mob BOSS stage 3','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
            
        # ------ ESTAGIO 2 -------
        if (level <= 10):
            if(luck == 0):
                mob = {'name':'mob 5','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'mob 6','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'mob 7','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'mob 8','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 10):
            mob = {'name':'mob BOSS stage 2','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 1 -------
        if (level < 5):
            if(luck == 0):
                mob = {'name':'mob 1','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'mob 2','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'mob 3','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'mob 4','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'} 
        if (level == 5):
            mob = {'name':'mob BOSS stage 1','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        return mob
    