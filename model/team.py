from enum import Enum

class TEAM(Enum):
    PLAYER = 0
    ENEMY = 1
    HOSTILE = 2
    DEAD = 3

    def get_enemies(value) -> list:
        match value:
            case TEAM.PLAYER:
                return [TEAM.ENEMY, TEAM.HOSTILE]
            case TEAM.ENEMY: 
                return [TEAM.PLAYER, TEAM.HOSTILE]
            case TEAM.HOSTILE:
                return [TEAM.PLAYER, TEAM.ENEMY, TEAM.HOSTILE]
            case TEAM.DEAD:
                return []
            
    def is_enemy(this, other) -> bool:
        match this:
            case TEAM.PLAYER:
                match other:
                    case TEAM.PLAYER:
                        return False
                    case TEAM.ENEMY:
                        return True
                    case TEAM.HOSTILE:
                        return True
                    case TEAM.DEAD:
                        return False
            case TEAM.ENEMY: 
                match other:
                    case TEAM.PLAYER:
                        return True
                    case TEAM.ENEMY:
                        return False
                    case TEAM.HOSTILE:
                        return True
                    case TEAM.DEAD:
                        return False
            case TEAM.HOSTILE:
                match other:
                    case TEAM.PLAYER:
                        return True
                    case TEAM.ENEMY:
                        return True
                    case TEAM.HOSTILE:
                        return True
                    case TEAM.DEAD:
                        return False
            case TEAM.DEAD:
                match other:
                    case TEAM.PLAYER:
                        return False
                    case TEAM.ENEMY:
                        return False
                    case TEAM.HOSTILE:
                        return False
                    case TEAM.DEAD:
                        return False
