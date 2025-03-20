require 'sinatra'
require 'json'

# Basic game state
GAME_STATE = {
  player: {
    name: nil,
    class: nil,
    health: 100,
    inventory: [],
    gold: 50,
    experience: 0,
    level: 1,
    attack: 10,
    defense: 5
  },
  story: {
    current_scene: 'character_creation',
  }
}

# Method to level up the player
def level_up
  if GAME_STATE[:player][:experience] >= 100
    GAME_STATE[:player][:level] += 1
    GAME_STATE[:player][:experience] = 0
    GAME_STATE[:player][:health] += 20
    GAME_STATE[:player][:attack] += 5
    GAME_STATE[:player][:defense] += 2
  end
end

# Game scenes
SCENES = {
  'character_creation' => {
    text: "Welcome, adventurer! What is your name?",
    choices: {}
  },
  'choose_class' => {
    text: "Choose your class: Warrior (High attack), Mage (High magic), or Rogue (High speed).",
    choices: {
      'warrior' => 'start',
      'mage' => 'start',
      'rogue' => 'start'
    }
  },
  'start' => {
    text: "You stand at the gates of the forsaken Kingdom of Eldoria. The land reeks of blood and decay. Before you lies a path of carnage and conquest.",
    choices: {
      'enter' => 'city_gates'
    }
  },
  'city_gates' => {
    text: "The massive iron gates creak open, revealing a ruined city littered with corpses. A knight in bloodstained armor blocks your way.",
    choices: {
      'fight' => 'fight_gatekeeper',
      'sneak' => 'marketplace'
    }
  },
  'fight_gatekeeper' => {
    text: "The gatekeeper charges at you, his sword thirsting for your flesh!",
    effect: -> {
      GAME_STATE[:player][:health] -= 30
      GAME_STATE[:player][:experience] += 50
      level_up
    },
    choices: {
      'victory' => 'marketplace'
    }
  },
  'marketplace' => {
    text: "The marketplace is filled with looted shops and burning stalls. A monstrous butcher stands before you, cleaver in hand, surrounded by hacked limbs.",
    choices: {
      'fight' => 'fight_butcher',
      'run' => 'castle_bridge'
    }
  },
  'fight_butcher' => {
    text: "The Butcher lets out a guttural laugh before lunging at you, his cleaver seeking your skull!",
    effect: -> {
      GAME_STATE[:player][:health] -= 40
      GAME_STATE[:player][:experience] += 70
      level_up
    },
    choices: {
      'victory' => 'castle_bridge'
    }
  },
  'castle_bridge' => {
    text: "You cross a bloodstained bridge leading to the royal castle. The last of Adrieth’s lieutenants, a towering executioner wielding a flaming axe, blocks your path.",
    choices: {
      'fight' => 'fight_executioner',
      'try to negotiate' => 'executioner_betrayal'
    }
  },
  'fight_executioner' => {
    text: "The Executioner swings his massive axe, its flames singing the air around you!",
    effect: -> {
      GAME_STATE[:player][:health] -= 50
      GAME_STATE[:player][:experience] += 100
      level_up
    },
    choices: {
      'victory' => 'castle_hall'
    }
  },
  'executioner_betrayal' => {
    text: "You attempt to reason with the Executioner, but he laughs and buries his axe in your chest. The world fades to black.",
    choices: {
      'death' => 'game_over'
    }
  },
  'castle_hall' => {
    text: "You step into the grand castle hall, where shadows dance along bloodstained banners. A corrupted sorcerer looms at the far end, whispering dark incantations.",
    choices: {
      'fight' => 'fight_sorcerer',
      'sneak past' => 'dungeon'
    }
  },
  'fight_sorcerer' => {
    text: "The sorcerer cackles and unleashes a wave of black fire, scorching the walls and floor!",
    effect: -> {
      GAME_STATE[:player][:health] -= 60
      GAME_STATE[:player][:experience] += 120
      level_up
    },
    choices: {
      'victory' => 'dungeon'
    }
  },
  'dungeon' => {
    text: "You descend into the dungeon, where tortured souls scream from rusted cages. A monstrous jailer, his flesh stitched with agony, lumbers toward you.",
    choices: {
      'fight' => 'fight_jailer',
      'run' => 'throne_room'
    }
  },
  'fight_jailer' => {
    text: "The Jailer drags a massive chain, its hooks dripping with fresh blood. He swings it toward you!",
    effect: -> {
      GAME_STATE[:player][:health] -= 50
      GAME_STATE[:player][:experience] += 150
      level_up
    },
    choices: {
      'victory' => 'throne_room'
    }
  },
  'throne_room' => {
    text: "The grand doors of the throne room open. The Great Knight Adrieth sits upon a throne of bones, his eyes burning with fury. He rises, drawing his cursed greatsword.",
    choices: {
      'fight' => 'fight_adrieth'
    }
  },
  'fight_adrieth' => {
    text: "Adrieth moves with terrifying speed, his blade singing through the air as he aims to carve you in half!",
    effect: -> {
      GAME_STATE[:player][:health] -= 70
      GAME_STATE[:player][:experience] += 200
      level_up
    },
    choices: {
      'victory' => 'win_game',
      'defeat' => 'game_over'
    }
  },
  'game_over' => {
    text: "Your body falls to the ground, lifeless. Adrieth stands victorious. The kingdom remains cursed forever. Game Over.",
    choices: {}
  },
  'win_game' => {
    text: "With a final strike, you slay Adrieth! His armor crumbles into dust, and the curse is lifted from Eldoria. You have triumphed!",
    effect: -> { GAME_STATE[:player][:inventory] << 'Cursed Blade of Adrieth' },
    choices: {}
  }
}

# Start the server
set :bind, '0.0.0.0'
set :port, 4567