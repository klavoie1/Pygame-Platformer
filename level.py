import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.level_setup(level_data)
        self.world_shift = 0

    # Loops through and displays the tile in each part of the level map from settings
    def level_setup(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == '1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(world_shift)
        self.tiles.draw(self.display_surface)