require 'net/http'
require 'json'
require 'uri'

SERVER_URL = 'http://localhost:4567'

def send_request(endpoint, data = {})
  uri = URI("#{SERVER_URL}/#{endpoint}")
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Post.new(uri, 'Content-Type' => 'application/json')
  request.body = data.to_json unless data.empty?
  response = http.request(request)
  JSON.parse(response.body) rescue response.body
end

# Test server connection
puts "Testing connection to server..."
response = send_request('status')
puts "Server Response: #{response}"

# Character creation test
puts "Creating character..."
response = send_request('character_creation', { name: 'TestHero' })
puts "Character Creation Response: #{response}"

# Choose class test
puts "Choosing Warrior class..."
response = send_request('choose_class', { class: 'warrior' })
puts "Class Selection Response: #{response}"

# Check initial level
puts "Checking initial level..."
response = send_request('player_status')
puts "Player Status: #{response}"

# Progressing through the game
puts "Entering the kingdom..."
response = send_request('progress', { choice: 'enter' })
puts "Response: #{response}"

puts "Fighting the gatekeeper..."
response = send_request('progress', { choice: 'fight' })
puts "Response: #{response}"

# Check level after experience gain
puts "Checking level after battle..."
response = send_request('player_status')
puts "Player Status: #{response}"

puts "Entering the marketplace..."
response = send_request('progress', { choice: 'victory' })
puts "Response: #{response}"

puts "Fighting the butcher..."
response = send_request('progress', { choice: 'fight' })
puts "Response: #{response}"

# Check level after another battle
puts "Checking level again..."
response = send_request('player_status')
puts "Player Status: #{response}"

puts "Crossing the bridge to the castle..."
response = send_request('progress', { choice: 'victory' })
puts "Response: #{response}"

puts "Fighting the executioner..."
response = send_request('progress', { choice: 'fight' })
puts "Response: #{response}"

# Checking level before final boss
puts "Checking level before final boss..."
response = send_request('player_status')
puts "Player Status: #{response}"

puts "Reaching the throne room..."
response = send_request('progress', { choice: 'victory' })
puts "Response: #{response}"

puts "Facing Adrieth, the final boss..."
response = send_request('progress', { choice: 'fight' })
puts "Final Boss Fight Response: #{response}"

# Final level check
puts "Checking final level..."
response = send_request('player_status')
puts "Final Player Status: #{response}"

puts "Test complete!"
