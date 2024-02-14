from direct.showbase.ShowBase import ShowBase
import sys


class SpaceJam(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

        self.accept('escape', self.quit)


    def SetupScene(self):
        #load universe model, reparent to camera, set scale
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)

        #load planet1 model, reparent to camera, set position and scale
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-12000, 5000, 67)
        self.Planet1.setScale(1500)

        #load planet2 model, reparent to camera, set position and scale
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(-6000, 5000, 10000)
        self.Planet2.setScale(1500)

        #load planet3 model, reparent to camera, set position and scale
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(6000, 5000, 10000)
        self.Planet3.setScale(1500)

        #load planet4 model, reparent to camera, set position and scale
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(12000, 5000, 67)
        self.Planet4.setScale(1500)

        #load planet5 model, reparent to camera, set position and scale
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(6000, 5000, -10000)
        self.Planet5.setScale(1500)

        #load planet6 model, reparent to camera, set position and scale
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(-6000, 5000, -10000)
        self.Planet6.setScale(1500)

        #load spaceship model, reparent to camera, set position and scale
        self.Spaceship = self.loader.loadModel("./Assets/Spaceships/Khan/Khan.x")
        self.Spaceship.reparentTo(self.render)
        self.Spaceship.setPos(-3500, 5000, 9000)
        self.Spaceship.setScale(5)

        #load space station model, reparent to camera, set position and scale
        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/SpaceStation/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(3000, 5000, -7500)
        self.SpaceStation.setScale(90)

        #load universe texture, set texture
        universetex = self.loader.loadTexture("./Assets/Universe/universe.jpg")
        self.Universe.setTexture(universetex, 1)

        #load planet1 texture, set texture
        planet1tex = self.loader.loadTexture("./Assets/Planets/planet1.jpg")
        self.Planet1.setTexture(planet1tex, 1)

        #load planet2 texture, set texture
        planet2tex = self.loader.loadTexture("./Assets/Planets/planet2.jpg")
        self.Planet2.setTexture(planet2tex, 1)

        #load planet3 texture, set texture
        planet3tex = self.loader.loadTexture("./Assets/Planets/planet3.jpg")
        self.Planet3.setTexture(planet3tex, 1)

        #load planet4 texture, set texture
        planet4tex = self.loader.loadTexture("./Assets/Planets/planet4.jpg")
        self.Planet4.setTexture(planet4tex, 1)

        #load planet5 texture, set texture
        planet5tex = self.loader.loadTexture("./Assets/Planets/planet5.jpg")
        self.Planet5.setTexture(planet5tex, 1)

        #load planet6 texture, set texture
        planet6tex = self.loader.loadTexture("./Assets/Planets/planet6.jpg")
        self.Planet6.setTexture(planet6tex, 1)


    def quit(self):
        sys.exit()


app = SpaceJam()
app.run()