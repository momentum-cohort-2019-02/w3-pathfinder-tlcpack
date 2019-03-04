from PIL import ImageColor, ImageDraw, Image

# # class notes: class ElevationMap:

#     def __init__(self, filename):
#         self.elevations = []
#         with open(filename) as file:
#             for line in file:
#                 self.elevations.append([int(e) for e in line.split()])


#         # max_elevations = []
#         # for row in self.elevations:
#         #     max_elevations.append(max(row))
#         # self.max_elevations = max(max_elevations)

#         self.max_elevation = max(max(row) for row in self.elevations)
#         self.min_elevation = min(min(row) for row in self.elevations)
#     def ele_print(self, max_elevation, min_elevation):
#         print(min_elevation)
#     def get_elevation(self, x, y):
#         return self.elevations[y][x]

#     def get_intensity(self, x, y):
#         return (self.get_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255

# ❸ >>> for x in range(100):
#            for y in range(50):
# ❹             im.putpixel((x, y), (210, 210, 210))

class Map:

    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(elev) for elev in line.split(" ")])
        
        # finding highest and lowest points on map
        self.max_overall_elev = max(max(row) for row in self.elevations)
        self.min_overall_elev = min(min(row) for row in self.elevations)
        print(self.max_overall_elev)
        print(self.min_overall_elev)

    def get_elevation(self, x, y):
        """flipping the coordinates so they're easier to read"""
        return self.elevations[y][x]

    def get_intensity(self, x, y):
        """determine intensity of pixel for map"""
        return int((self.get_elevation(x, y) - self.min_overall_elev) / (self.max_overall_elev - self.min_overall_elev) * 255)

class DrawMap:
    

    def __init__(self, map):
        self.map = map
        self.picture = Image.new('RGBA', (len(self.map.elevations[0]), len(self.map.elevations)))
        self.drawing = ImageDraw.Draw(self.picture)

    def draw(self):
        """Drawing the map"""
        for x in range(len(self.map.elevations[0])):
            for y in range(len(self.map.elevations)):
                self.picture.putpixel((x, y), (self.map.get_intensity(x, y), self.map.get_intensity(x, y), self.map.get_intensity(x, y)))
        
        
    def draw_line(self):
        """Drawing the line"""
        self.drawing.line([(20, 0), (100, 275)], fill='black')    

        self.picture.save('elevation_draw_example.png')


# couldn't get image to save with separate drawing class
# class DrawLine:

#     def __init__(self, canvas):
#         self.canvas = Image.new('RGBA', (len(example.map.elevations[0]), len(example.map.elevations)))
#         self.draw = ImageDraw.Draw(self.canvas)

#     def draw_line(self):
#         """Drawing the line"""
#         self.draw.line([(0, 0), (50, 75)], fill='black')

#         self.draw.save('pic_with_line.png')

class Path:

    def __init__(self, field, x_start, y_start):
        self.field = field
        self.x_start = x_start
        self.y_start = y_start
        self.picture = Image.new('RGBA', (len(self.field.elevations[0]), len(self.field.elevations))) 
        self.path = ImageDraw.Draw(self.picture)
        

    def draw_path(self):
        total_path = []
        x_path = [self.x_start]
        possible_y_path = [self.y_start, self.y_start - 1, self.y_start + 1]

        up_choice = abs(self.field.elevations[self.x_start + 1][possible_y_path[1]] - self.field.elevations[self.x_start][self.y_start])
        straight_choice = abs(self.field.elevations[self.x_start + 1][possible_y_path[0]] - self.field.elevations[self.x_start][self.y_start])
        down_choice = abs(self.field.elevations[self.x_start + 1][possible_y_path[2]] - self.field.elevations[self.x_start][self.y_start])
        diffs = {"up": up_choice, "straight": straight_choice, "down": down_choice}
        up = diffs["up"]
        straight = diffs["straight"]
        down = diffs["down"]
        next_step = 0

        if up < down and up < straight:
            next_step = possible_y_path[1]
        elif down < up and down < straight:
            next_step = possible_y_path[2]
        elif down == up and down < straight:
            next step = possible_y_path[2] # ignoring instruction to randomly choose path, just picking the down path
        else:
            next_step = possible_y_path[0]


if __name__ == "__main__":

    
    small = Map('elevation_small.txt')
    example = DrawMap(small)
    example.draw()
    example.draw_line()
    # line.draw_line()