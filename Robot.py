from Maze import CellState

class Robot:
    def __init__(self,x,y,direction,grille,maze,fenetre):
        self.x=x
        self.y=y
        self.dir=direction
        self.grille=grille
        self.maze=maze
        self.fenetre=fenetre
        
    def dessiner(self,direction,grille):
        grille.create_rectangle(self.x*25,self.y*25,(self.x+1)*25,(self.y+1)*25,fill="green")
        if direction == "E":
            grille.create_polygon(self.x*25,self.y*25,(self.x+1)*25,(self.y+0.5)*25,self.x*25,(self.y+1)*25)
        if direction == "S":
            grille.create_polygon((self.x+1)*25,self.y*25,(self.x+0.5)*25,(self.y+1)*25,self.x*25,(self.y)*25)
        if direction == "W":
            grille.create_polygon((self.x+1)*25,self.y*25,(self.x)*25,(self.y+0.5)*25,(self.x+1)*25,(self.y+1)*25)
        if direction == "N":
            grille.create_polygon(self.x*25,(self.y+1)*25,(self.x+0.5)*25,(self.y)*25,(self.x+1)*25,(self.y+1)*25)
    
    def avancer(self,direction,maze,fenetre):
        if direction == "N" and maze[self.y-1][self.x] != CellState.WALL:
            self.y-=1
        elif direction == "E" and maze[self.y][self.x+1] != CellState.WALL:
            self.x+=1
        elif direction == "S" and maze[self.y+1][self.x] != CellState.WALL:
            self.y+=1
        elif direction == "W" and maze[self.y][self.x-1] != CellState.WALL:
            self.x-=1
        if maze[self.y][self.x] == CellState.EXIT:
            print("Gagner")
            fenetre.quit()