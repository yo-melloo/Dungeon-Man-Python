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
            mob = {'name':'Oolong','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        if (level == 32):
            mob = {'name':'Tigrinho Rei Do Inferno','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 4 -------
        if (level <= 30):
            if(luck == 0):
                mob = {'name':'Silvio Santos','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'Helicoptero da Record','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'Caçamba do Motorzinho','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'Aplicativo de Relacionamento','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 30):
            mob = {'name':'Doutor Estranho','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 3 -------
        if (level <= 20):
            if(luck == 0):
                mob = {'name':'Hulk','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'Homem de Ferro','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'Gigante de Aço','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'Dinossauro','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 5):
            mob = {'name':'Mago Mestre','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        if (level == 20):
            mob = {'name':'Mega Uganda Knuckles','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
            
        # ------ ESTAGIO 2 -------
        if (level <= 10):
            if(luck == 0):
                mob = {'name':'Professor de Má-temática','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'Zumbi','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'Esfinge','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'Medusa','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'}
        if (level == 10):
            mob = {'name':'Minotauro','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        # ------ ESTAGIO 1 -------
        if (level < 5):
            if(luck == 0):
                mob = {'name':'Vampyr','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 1'}
            if(luck == 1):
                mob = {'name':'Golem','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 2'}
            if(luck == 2):
                mob = {'name':'Goblin','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 3'}
            if(luck == 3):
                mob = {'name':'Esqueleto','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT MOB 4'} 
        if (level == 5):
            mob = {'name':'Slime','hp': 100,'atk':10,'def':10,'spd':10,'spc_attack':'NONE', 'desc':'DEFAULT BOSS MOB'}
        
        return mob
    