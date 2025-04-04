class LevelManager:
    def __init__(self):
        self.current_level = 1
        self.accumulated_score = 0
        self.levels = {
            1: {
                'enemy_speed_range': (2, 5),
                'spawn_delay': 1000,
                'score_threshold': 100,
                'player_lives': 3
            },
            2: {
                'enemy_speed_range': (3, 6),
                'spawn_delay': 800,
                'score_threshold': 200,
                'player_lives': 3
            },
            3: {
                'enemy_speed_range': (4, 7),
                'spawn_delay': 600,
                'score_threshold': 300,
                'player_lives': 4
            }
        }

    def get_current_speed_range(self):
         return self.levels[self.current_level]['enemy_speed_range']
    
    def get_current_spawn_delay(self):
         return self.levels[self.current_level]['spawn_delay']

    def get_current_level_config(self):
        return self.levels[self.current_level]

    def check_level_up(self, score):
            config = self.get_current_level_config()
            currebt_threshold = self.accumulated_score + config['score_threshold']

            if score >= currebt_threshold and self.current_level < len(self.levels):
                self.accumulated_score += config['score_threshold']
                self.current_level += 1
                return True
            return False
    
    def calculate_progress(self, current_score):
        if self.current_level > len(self.levels):
             return 1.0
        config = self.get_current_level_config()
        required = config['score_threshold']
        progress = (current_score - self.accumulated_score) / required
        return max(0.0, min(progress, 1.0))
