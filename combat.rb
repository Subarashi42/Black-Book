class Combat
  attr_reader :player, :enemy, :log

  def initialize(player, enemy)
    @player = player
    @enemy = enemy
    @log = []  # To keep a log of actions for feedback
  end

  def start_combat
    @log.clear
    @log << "Combat started between #{@player.name} and #{@enemy.name}."
    while @player.health > 0 && @enemy.health > 0
      player_turn
      break if @enemy.health <= 0
      enemy_turn
    end
    end_combat
  end

  def player_turn
    action = @player.choose_action
    case action
    when 'attack'
      damage = calculate_damage(@player.attack, @enemy.defense)
      @enemy.take_damage(damage)
      @log << "#{@player.name} attacks #{@enemy.name} for #{damage} damage."
    when 'defend'
      @player.defend
      @log << "#{@player.name} defends."
    when 'use_item'
      item = @player.use_item
      @log << "#{@player.name} uses #{item.name}."
    end
  end

  def enemy_turn
    action = @enemy.choose_action
    case action
    when 'attack'
      damage = calculate_damage(@enemy.attack, @player.defense)
      @player.take_damage(damage)
      @log << "#{@enemy.name} attacks #{@player.name} for #{damage} damage."
    when 'defend'
      @enemy.defend
      @log << "#{@enemy.name} defends."
    end
  end

  def calculate_damage(attack, defense)
    # Simple damage formula (you can make this more complex depending on game mechanics)
    [attack - defense, 0].max
  end

  def end_combat
    if @player.health <= 0
      @log << "#{@enemy.name} wins the battle!"
    elsif @enemy.health <= 0
      @log << "#{@player.name} wins the battle!"
    end
  end
end

class Player
  attr_accessor :name, :health, :attack, :defense, :inventory

  def initialize(name, health, attack, defense)
    @name = name
    @health = health
    @attack = attack
    @defense = defense
    @inventory = []
  end

  def choose_action
    # Placeholder for player input handling, e.g., 'attack', 'defend', 'use_item'
    ['attack', 'defend', 'use_item'].sample
  end

  def take_damage(damage)
    @health -= damage
  end

  def defend
    @defense *= 2  # Example of defense buff (simplified)
  end

  def use_item
    item = @inventory.sample
    # Apply item effects (simplified)
    @health += 20
    item
  end
end

class Enemy
  attr_accessor :name, :health, :attack, :defense

  def initialize(name, health, attack, defense)
    @name = name
    @health = health
    @attack = attack
    @defense = defense
  end

  def choose_action
    # Placeholder for enemy AI (could be based on health, strength, etc.)
    ['attack', 'defend'].sample
  end

  def take_damage(damage)
    @health -= damage
  end

  def defend
    @defense *= 2  # Example of enemy defense buff (simplified)
  end
end
