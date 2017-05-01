class Team(object):
	def __init__(self, team_name):
		self.team_name = team_name
		self.team_salary = 0
		self.max_salary = 10000
		self.team_strength = 0
		self.players = []


	def total_team_strength(self):
		self.team_strength = ((self.players[0].strength) + (self.players[1].strength) + (self.players[2].strength))
		print "TEAM STRENGTH: " + str(self.team_strength)



	def available_salary(self):
		self.team_salary = self.max_salary - ((self.players[0].salary) + (self.players[1].salary) + (self.players[2].salary))
		print "AVAILABLE SALARY: " + str(self.team_salary)


	def print_roster(self):
		for players in self.players:
			print players.name

	def add_player(self, player_obj):
		self.players.append(player_obj)

	def del_player(self, player_obj):
		self.players.remove(player_obj)

	def compete(self):
		pass

	
	def falcon_display(self):
		print """ 
		               /T /I          
                              / |/ | .-~/    
                          T\\ Y  I  |/  /  _  
         /T               | \\I  |  I  Y.-~/  
        I l   /I       T\ |  |  l  |  T  /   
 __  | \\l   \\l  \\I l __l  l   \\   `  _. |    
 \\ ~-l  `\\   `\  \  \\ ~\  \   `. .-~   |    
  \\   ~-. "-.  `  \  ^._ ^. "-.  /  \\   |    
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./    
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]     
^.___~\"--._    ~-{  .-~ .  `\ Y . /    |     
 <__ ~\"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______     
       ^--.,___.-~\"  /_/   !  `-.~\"--l_ /     ~"-.  
              (_/ .  ~(   /'     \"~\"--,Y   -=b-. _) 
               (_/ .  \\  :           / l           \\
                \ /    `.    .     .^   \\_.-~"~--. ) 
                 (_/ .   `  /     /       !       )/  
                  / / _.   '.   .':      /        ' 
                  ~(_/ .   /    _  `  .-<_      
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\ 
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"               
		"""

	def panther_display(self):
		print """ 
 :~-._                                                 _.-~:
    : :.~^o._        ________---------________        _.o^~.:.:
     : ::.`?88booo~~~.::::::::...::::::::::::..~~oood88P'.::.:
     :  ::: `?88P .:::....         ........:::::. ?88P' :::. :
      :  :::. `? .::.            . ...........:::. P' .:::. :
       :  :::   ... ..  ...       .. .::::......::.   :::. :
       `  :' .... ..  .:::::.     . ..:::::::....:::.  `: .'
        :..    ____:::::::::.  . . ....:::::::::____  ... :
       :... `:~    ^~-:::::..  .........:::::-~^    ~::.::::
       `.::. `\   (8) \\b:::..::.:.:::::::d/  (8)   /'.::::'
        ::::.  ~-._v    |b.::::::::::::::d|    v_.-~..:::::
        `.:::::... ~~^?888b..:::::::::::d888P^~...::::::::'
         `.::::::::::....~~~ .:::::::::~~~:::::::::::::::'
          `..:::::::::::   .   ....::::    ::::::::::::,'
            `. .:::::::    .      .::::.    ::::::::'.'
              `._ .:::    .        :::::.    :::::_.'
                 `-. :    .        :::::      :,-'
                    :.   :___     .:::___   .::
          ..--~~~~--:+::. ~~^?b..:::dP^~~.::++:--~~~~--..
            ___....--`+:::.    `~8~'    .:::+'--....___
          ~~   __..---`_=:: ___gd8bg___ :==_'---..__   ~~
           -~~~  _.--~~`-.~~~~~~~~~~~~~~~,-' ~~--._ ~~~-
              -~~            ~~~~~~~~~             ~~-
		"""
	
	def saint_display(self):
		print """
     	              8
                    .d8b.
                _.d8888888b._
              .88888888888888b.
             d88888888888888888b
             8888888888888888888
             Y88888888888888888P
              'Y8888888888888P'
            _..._ 'Y88888P' _..._
          .d88888b. Y888P .d88888b.
         d888888888b 888 d88888888b
         888P  `Y8888888888P'  Y888
          b8b    Y88888888P    d8Y
           `"'  #############  '"`
                  dP d8b Yb
              Ob=dP d888b Yb=dO
               `"` O88888O `"`
                    'Y8P'
                      '
		 """